import requests
from bs4 import BeautifulSoup


def web_crawler(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://littlerock.craigslist.org/search/ofc' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        for link in soup.findAll('a', {'class': 'result-title hdrlnk'}):
            href = 'https://littlerock.craigslist.org/search/ofc' + link.get('href')
            title = link.string
            print(href)
            print(title)
        page += 1

web_crawler(1)
