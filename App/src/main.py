# import requests
# import time
# from stem import Signal
# from stem.control import Controller
# from bs4 import BeautifulSoup


# def initialize_tor_controller(password):
#     with Controller.from_port(port=9051) as controller:
#         controller.authenticate(password='cyberxploithausa')
#         return controller


# def get_links_from_url(url, headers):
#     response = requests.get(url, headers=headers)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     links = soup.find_all('a')
#     return [a.get('href') for a in links]


# def crawl_links(start_url, num_links_to_crawl, keywords, user_agent):
#     visited = set()
#     queue = [start_url]
#     headers = {'User-Agent': user_agent}

#     with initialize_tor_controller('cyberxploithausa') as controller:
#         while queue:
#             link = queue.pop(0)

#             if link in visited:
#                 continue

#             controller.signal(Signal.NEWNYM)
#             links = get_links_from_url(link, headers)

#             for href in links:
#                 if any(keyword in href for keyword in keywords):
#                     queue.append(href)

#             visited.add(link)
#             print(f'Title: {get_page_title(link)}\nURL: {link}')

#             if len(visited) >= num_links_to_crawl:
#                 break

#     return visited


# def get_page_title(url, headers):
#     response = requests.get(url, headers=headers)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     return soup.title.string


# if __name__ == "__main__":
#     num_links_to_crawl = 100
#     # user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
#     user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
#     start_url = 'http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion'
#     keywords = input(
#         'Enter a list of keywords to search for, separated by commas: ').split(',')

#     crawled_links = crawl_links(
#         start_url, num_links_to_crawl, keywords, user_agent)

#     print('Visited links:')
#     for link in crawled_links:
#         print(link)


import requests
import random
import crawler
from tor_config import torCon
import time
from bs4 import BeautifulSoup
import re
#from setup import start_tor # type: ignore

#SLEEP = time.sleep(1)

def browse():
    #lets set up some fake user agents
    user_agents = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19577" \
                ,"Mozilla/5.0 (X11) AppleWebKit/62.41 (KHTML, like Gecko) Edge/17.10859 Safari/452.6" \
                    , "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2656.18 Safari/537.36" \
                    ,"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/44.0.2403.155 Safari/537.36",\
                    "Mozilla/5.0 (Linux; U; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13",\
                    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",\
                    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_8; zh-cn) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27", \
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"]
    user_agent = random.choice(user_agents)
    HEADER = {'User-Agent': user_agent}
    proxies = torCon()
    URLS = f"{ahmia}/search/?q={search}"    
    response = requests.get(url=URLS, proxies=proxies, headers=HEADER)
    if response.status_code == 200:
        #content = response.content.decode()
        content = response.text
        #soup = BeautifulSoup(content, 'html.parser')
        #links = soup.find_all('a')
        #all_links = [a.get('href') for a in links]
        #print(all_links)
        regex = "\w+\.onion"
        minedate = re.findall(regex, content)
        import numpy as N
        res = N.array(minedate)
        unique = N.unique(res)
        print(unique)
        #print(minedate)
        



if __name__ == "__main__":
    #start_tor()
    ahmia = 'http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion'
    #check_for_vpn()
    #SLEEP
    time.sleep(1)
    print("Starting to Access The Dark Web...")
    #SLEEP
    time.sleep(1)
    search = input("What are you looking for: ").split()
    time.sleep(1)
    print("Surfing to Dark Web as Requested...")

    browse()
    
 



""" 
Search Engines

torch = http://torchdeedp3i2jigzjdmfpn5ttjhthh5wbmda2rr3jvqjg5p77c54dqd.onion/
haystak = http://haystak5njsmn2hqkewecpaxetahtwhsbsa64jom2k22z5afxhnpxfid.onion/
not evil = http://hss3uro2hsxfogfq.onion.to/index.php


Hacking Forum

1. http://hacktowns3sba2xavxecm23aoocvzciaxirh3vekg2ovzdjgjxedfvqd.onion/
2. http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/
3. http://dreadytofatroptsdj6io7l3xptbet6onoyno2yv7jicoxknyazubrad.onion/
"""