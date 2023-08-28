import requests
import difflib
from models.comic_issue import ComicIssue
from bs4 import BeautifulSoup
from robotexclusionrulesparser import RobotFileParserLookalike as RobotParser
from constants import BASE_SEARCH_URL, BASE_PUBID, BASE_PUBRNG, PUBLISHER, PUBRNG, DISPLAY

BASE_URL = 'https://www.mycomicshop.com/search?TID=25730429'

def is_allowed_to_scrape(url, user_agent):
    rp = RobotParser()
    rp.set_url(url + "robots.txt")
    rp.read()
    return rp.can_fetch(user_agent, url)

def scrape_mycomicshop(url):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'

    if not is_allowed_to_scrape(url, user_agent):
        print("We're not allowed to scrape this website based on its robots.txt.")
        return

    headers = {
        'User-Agent': user_agent
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Failed to retrieve the webpage.")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup)
    display_type = soup.find('select', class_='setdisplayas').find('option').text

    if display_type == DISPLAY['titlelist']:
        return_titles(soup)
    elif display_type == DISPLAY['issuelist']:
        return_issues(soup)

    return soup


#URL Builder based off of search criteria
def url_builder(title, issue_num=None, publisher=None, published=None):
    #URL Example with search criteria
    #https://www.mycomicshop.com/search?q=wicked+and+the+divine&pubid=9661&PubRng=2000-2023
    url = BASE_SEARCH_URL
    
    title_fragments = title.split();

    #appending title to base search string url
    for index,value in enumerate(title_fragments):
        if index != len(title_fragments)-1:
            url += value + '+'
        else:
            url += value
    
    #appending issue number
    if issue_num != None:
        url += '+' + str(issue_num)

    #appending publisher name to search url
    if publisher != None:
        url += BASE_PUBID + publisher
    else:
        url += BASE_PUBID

    #appending date range to search url (user input not yet supported)
    if published != None:
        url += BASE_PUBRNG + published
    else:
        url += BASE_PUBRNG

    return url

def return_issues(soup):
    issues = []
    comic_titles = soup.select('li.issue div.title')
    comic_issues = soup.select('li.issue')

    for index, issue in enumerate(comic_issues, 1):
        title_issue_num = issue.find('div', class_ ='title').text.split('#')
        print(title_issue_num)
        title = title_issue_num[0].strip()
        issue_num = title_issue_num[1].strip()
        publisher_date = issue.find('div', class_='othercolright').text.rstrip('\n').replace('Published','').split('by')
        date = publisher_date[0].rstrip('\n').strip()
        publisher = publisher_date[1].strip().replace('.','')

        if title and publisher_date:
            issues.append(ComicIssue(title,issue_num,date,publisher))
            #print(f"{index}. {title} #{issue_num} {publisher} {date}")
            # print("Title: " + title)
            # print("Publisher: "+ publisher)
            # print('Date: '+ date)
            print("-" * 50)
    print(str(issues))
    
    for index, title in enumerate(comic_titles, 1):
        print(f"{index}. {title.text.strip()}")

def return_titles(soup):
    # Getting a tuple of the search href of the title and the text asscoiated witht the tag
    comic_hrefs = [(a['href'],a.text) for a in soup.select('table.results td.title a') if 'href' in a.attrs]
    
    for index, title in enumerate(comic_hrefs, 1):
        print(f"{index}. Link: https://www.mycomicshop.com/{title[0]} Title: {title[1]}")


def comic_page_type(html_page):
    set_displays = html_page.find('select', class_='setdisplayas', selected=True)
    if set_displays:
        print(set_displays.text)



if __name__ == '__main__':
    # print(url_builder(title='wicked and the divine',issue_num=1, publisher=PUBLISHER['image'], published=PUBRNG['2000-2023']))
    # print(url_builder(title='wicked and the divine', publisher=PUBLISHER['image']))
    # print(url_builder(title='wicked and the divine',issue_num=16))

    url = url_builder(title='wicked and the divine')
    url2 = url_builder(title='wicked and the divine', issue_num=16, publisher=PUBLISHER['image'])

    print(url)
    print(url2)


    scrape_mycomicshop(url)
    scrape_mycomicshop(url2)

    # text1 = soup1.text
    # text2 = soup2.text

    # print('----------------------------')
    # link1_display = comic_page_type(soup1)
    # link2_display = comic_page_type(soup2)
    # print('----------------------------')

    # # Convert each text into a set of lines
    # set1 = set(text1.splitlines())
    # set2 = set(text2.splitlines())

    # # Find lines that are only in text1 and not in text2
    # unique_lines = set1 - set2

    # print('\n'.join(unique_lines))