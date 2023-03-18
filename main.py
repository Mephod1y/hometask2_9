import json
import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'

def parser(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes_ = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')
    tags = soup.find_all('div', class_='tags')

    quotes = []
    for i in range(0, len(quotes_)):
        tagsforquotes = tags[i].find_all('a', class_='tag')
        tags_ = [tagforquote.text for tagforquote in tagsforquotes]

        quotes.append({
            "tags": tags_,
            "author": authors[i].text.strip(),
            "quote": quotes_[i].text.strip().replace(chr(8220),"").replace(chr(8221),"")})
    return quotes

def parser_a(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    authors_about = []
    authors_url = []
    about = soup.find_all('a', href=True)
    for a in about:
        if a['href'].startswith("/author"):
            authors_about.append(a['href'])
    for a in authors_about:
        authors_url.append(f'https://quotes.toscrape.com{a}')

    authors = []
    for author in authors_url:
        response = requests.get(author)
        soup = BeautifulSoup(response.text, 'lxml')
        author_title = soup.find_all('h3', class_='author-title')
        born = soup.find_all('span', class_='author-born-date')
        born_location = soup.find_all('span', class_='author-born-location')
        descr = soup.find_all('div', class_='author-description')

        authors.append({
            "fullname": author_title[0].text.strip(),
            "born": born[0].text.strip(),
            "born_location": born_location[0].text.strip(),
            "description": descr[0].text.strip()})
    return authors

if __name__ == '__main__':
    q = parser(url)
    a = parser_a(url)
    with open('quotes.json', 'w', encoding='utf-8') as fd:
        json.dump(q, fd, ensure_ascii=False)
    with open('authors.json', 'w', encoding='utf-8') as fd:
        json.dump(a, fd, ensure_ascii=False)