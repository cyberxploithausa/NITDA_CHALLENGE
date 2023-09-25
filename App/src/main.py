"""
import csv
import os
import random
import time
import re
import requests
from bs4 import BeautifulSoup
from tor_config import torCon

def browse(search, output_folder):
    user_agents = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19577",
                  "Mozilla/5.0 (X11) AppleWebKit/62.41 (KHTML, like Gecko) Edge/17.10859 Safari/452.6",
                  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2656.18 Safari/537.36",
                  "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/44.0.2403.155 Safari/537.36",
                  "Mozilla/5.0 (Linux; U; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13",
                  "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
                  "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_8; zh-cn) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
                  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"]
    
    user_agent = random.choice(user_agents)
    HEADER = {'User-Agent': user_agent}
    proxies = torCon()
    URLS = f"{ahmia}/search/?q={search}"
    
    response = requests.get(url=URLS, proxies=proxies, headers=HEADER)
    
    if response.status_code == 200:
        content = response.text
        regex = "\w+\.onion"
        minedata = re.findall(regex, content)
        unique = list(set(minedata))
        
        if not os.path.exists(output_folder):
            os.mkdir(output_folder)
        
        output_file = f"{search}_links.csv"
        output_path = os.path.join(output_folder, output_file)

        with open(output_path, 'a', newline="") as data:
            csv_writer = csv.writer(data)
            for item in unique:
                csv_writer.writerow([item])
        
        print(f'[+] All links for "{search}" are saved to {output_path}')
    
    elif response.status_code == 404:
        print(f"Search for '{search}' Not Found!!!")
    
    else:
        print("Search Not Reachable!!!")


if __name__ == "__main__":
    ahmia = 'http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion'
    time.sleep(1)
    print("[+] Starting to Access The Dark Web...")
    time.sleep(1)
    
    searches = input("Enter a list of keywords to search for, separated by commas: ").split(',')
    
    # Specify the output folder (two directories back from the current directory)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_folder = os.path.abspath(os.path.join(base_dir, '..', '..', 'Results'))
    
    for search in searches:
        print(f"[+] Surfing to Dark Web for '{search}'...")
        browse(search, output_folder)

# [Onniforums] http://envoyyvazgz2wbkq65md7dcqsgmujmgksowhx2446yep7tgnpfvlxbqd.onion/index.php

"""


import csv
import os
import random
import time
import re
import requests
from bs4 import BeautifulSoup
from tor_config import torCon

def browse(search, output_folder):
    user_agents = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19577",
                  "Mozilla/5.0 (X11) AppleWebKit/62.41 (KHTML, like Gecko) Edge/17.10859 Safari/452.6",
                  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2656.18 Safari/537.36",
                  "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/44.0.2403.155 Safari/537.36",
                  "Mozilla/5.0 (Linux; U; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13",
                  "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
                  "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_8; zh-cn) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
                  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"]
    
    user_agent = random.choice(user_agents)
    HEADER = {'User-Agent': user_agent}
    proxies = torCon()
    URLS = f"{ahmia}/search/?q={search}"
    
    response = requests.get(url=URLS, proxies=proxies, headers=HEADER)
    
    if response.status_code == 200:
        content = response.text
        regex = "\w+\.onion"
        minedata = re.findall(regex, content)
        unique = list(set(minedata))
        
        if not os.path.exists(output_folder):
            os.mkdir(output_folder)
        
        output_file = f"{search}_links.csv"
        output_path = os.path.join(output_folder, output_file)

        with open(output_path, 'a', newline="") as data:
            csv_writer = csv.writer(data)
            for item in unique:
                csv_writer.writerow([item])
        
        print(f'[+] All links for "{search}" are saved to {output_path}')
    
    elif response.status_code == 404:
        print(f"Search for '{search}' Not Found!!!")
    
    else:
        print("Search Not Reachable!!!")


if __name__ == "__main__":
    ahmia = 'http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion'
    time.sleep(1)
    print("[+] Starting to Access The Dark Web...")
    time.sleep(1)
    
    searches = input("Enter a list of keywords to search for, separated by commas: ").split(',')
    
    # Specify the output folder (two directories back from the current directory)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_folder = os.path.abspath(os.path.join(base_dir, '..', '..', 'Results'))
    
    for search in searches:
        print(f"[+] Surfing to Dark Web for '{search}'...")
        browse(search, output_folder)

# [Onniforums] http://envoyyvazgz2wbkq65md7dcqsgmujmgksowhx2446yep7tgnpfvlxbqd.onion/index.php