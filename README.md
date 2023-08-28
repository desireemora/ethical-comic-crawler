# Ethical Comic Crawler

Using `robotexclusionrulesparser`, I ensure compliance with all the rules defined by the robots.txt file of any website being scraped. I aim to transform this web crawler into an API, allowing users to send requests for comic information they're seeking. Details can include:

- Name
- Publisher
- Issue number
- Publish date
- Cover price
- And eventually... reseller value (based on the average resale price found on websites like eBay).

If you are the owner of [`https://www.mycomicshop.com`](https://www.mycomicshop.com) and this code or the (future) API causes any inconvenience, please contact me, and I will promptly address it.

###  Thank you!

# Instructions

### Packages

`pip install -r requirements.txt`

### Run
`python scrape.py`

### Tests
`python -m unittest test_comic_issue.py`
`python -m unittest test_comic_title.py`
