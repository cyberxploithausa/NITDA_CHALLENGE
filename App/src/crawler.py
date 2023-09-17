import requests
import time
from stem import Signal
from stem.control import Controller
from bs4 import BeautifulSoup


def initialize_tor_controller(password):
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password=password)
        return controller


def get_links_from_url(url, headers):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a')
    return [a.get('href') for a in links]


def crawl_links(start_url, num_links_to_crawl, keywords, user_agent):
    visited = set()
    queue = [start_url]
    headers = {'User-Agent': user_agent}

    with initialize_tor_controller('mypassword') as controller:
        while queue:
            link = queue.pop(0)

            if link in visited:
                continue

            controller.signal(Signal.NEWNYM)
            links = get_links_from_url(link, headers)

            for href in links:
                if any(keyword in href for keyword in keywords):
                    queue.append(href)

            visited.add(link)
            print(f'Title: {get_page_title(link)}\nURL: {link}')

            if len(visited) >= num_links_to_crawl:
                break

    return visited


def get_page_title(url, headers):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.title.string


if __name__ == "__main__":
    num_links_to_crawl = 100
    # user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    start_url = 'http://http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion'
    keywords = input(
        'Enter a list of keywords to search for, separated by commas: ').split(',')

    crawled_links = crawl_links(
        start_url, num_links_to_crawl, keywords, user_agent)

    print('Visited links:')
    for link in crawled_links:
        print(link)
