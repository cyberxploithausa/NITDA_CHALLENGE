import requests
import random
import crawler
from tor_config import torCon
import time
from bs4 import BeautifulSoup
import re
import csv
import os
#from setup import start_tor # type: ignore

#SLEEP = time.sleep(1)

def main():
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
        minedata = re.findall(regex, content)
        import numpy as N
        res = N.array(minedata)
        unique = N.unique(res)
        confirm_data = unique.tolist()
        #print(type(confirm_data))
        # data_column = []
        # for item in confirm_data:
        #     data_column.append(item)
        # with open('search_links.csv', 'w', newline="") as data:
        #     csv_writer = csv.writer(data)
        #     for item in data_column:
        #         csv_writer.writerow([item])
        #         print('[+] All links are saved')
        # path = os.mkdir('C:\Users\cyberxploit\Desktop\NITDA_CHALLENGE\App\Results')

        data_column = []
        for item in confirm_data:
            data_column.append(item)
        output_folder = "../Results"
        output_file = "links.csv"

        if not os.path.exists(output_folder):
            os.mkdir(output_folder)
        output_path = os.path.join(output_folder, output_file)

        with open(output_path, 'w', newline="") as data:
            csv_writer = csv.writer(data)
            for item in data_column:
                csv_writer.writerow([item])
            print('[+] All links are saved')
    elif response.status_code == 404:
        print("Search Not Found!!!")
    else:
        print("Search Not Reachable!!!")



if __name__ == "__main__":
    #start_tor()
    ahmia = 'http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion'
    #check_for_vpn()
    #SLEEP
    time.sleep(1)
    print("[+] Starting to Access The Dark Web...")
    #SLEEP
    time.sleep(1)
    search = input("What are you looking for: ").split()
    time.sleep(1)
    print("[+] Surfing to Dark Web as Requested...")

    main()
    
 



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