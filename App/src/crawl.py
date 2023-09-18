import requests
from bs4 import BeautifulSoup

def get_links_from_url(url, headers):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a')
    return [a.get('href') for a in links]

def crawl_links(start_url, num_links_to_crawl, keywords, user_agent):
    # Your web crawling logic
    pass

def get_page_title(url, headers):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.title.string
