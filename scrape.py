import requests
from bs4 import BeautifulSoup
from robotexclusionrulesparser import RobotFileParserLookalike as RobotParser

BASE_URL = 'https://www.mycomicshop.com/search?TID=25730429'

def is_allowed_to_scrape(url, user_agent):
    rp = RobotParser()
    rp.set_url(url + "robots.txt")
    rp.read()
    return rp.can_fetch(user_agent, url)

def scrape_mycomicshop():
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'

    if not is_allowed_to_scrape(BASE_URL, user_agent):
        print("We're not allowed to scrape this website based on its robots.txt.")
        return

    headers = {
        'User-Agent': user_agent
    }

    response = requests.get(BASE_URL, headers=headers)

    if response.status_code != 200:
        print("Failed to retrieve the webpage.")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    #print(soup)

    # Assuming the comic titles are in an 'h2' tag (this might change depending on the website's structure)
    #comic_titles = soup.find_all('li', class_='issue').find('div',class_='title') # This class might need adjustment based on the site's structure
    comic_titles = soup.select('li.issue div.title')
    comic_issues = soup.select('li.issue')

    for issue in comic_issues:
        title = issue.find('div', class_ ='title')
        publisher_date = issue.find('div', class_='othercolright')

        if title and publisher_date:
            print("Title:", title.text.strip())
            print("Publisher & Date:", publisher_date.text.rstrip().replace('Published',''))
            print("-" * 50)

    # for index, title in enumerate(comic_titles, 1):
    #     print(f"{index}. {title.text.strip()}")

if __name__ == '__main__':
    scrape_mycomicshop()