import requests
from bs4 import BeautifulSoup


def spider(max_pages):
    page = 1
    while page <= max_pages:
        url = "https://www.lindaikejisblog.com/page/" + str(page)
        source_code = requests.get(url)
        plaintext_source_code = source_code.text
        formatted_source_code = BeautifulSoup(plaintext_source_code, features="html.parser")
        for links in formatted_source_code.findAll('a', {'class': 'story_title'}):
            href = links.get('href')
            title = links.string
            print(title)
            print(href, "\n")
    page += 1


spider(2)
