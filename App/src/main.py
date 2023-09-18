from crawl import crawl_links
from tor_controller import initialize_tor_controller
from utils import load_user_agents

def main():
    num_links_to_crawl = 100
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    start_url = 'http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion'
    keywords = input('Enter a list of keywords to search for, separated by commas: ').split(',')
    
    crawled_links = crawl_links(start_url, num_links_to_crawl, keywords, user_agent)
    
    print('Visited links:')
    for link in crawled_links:
        print(link)
    
if __name__ == "__main__":
    main()
