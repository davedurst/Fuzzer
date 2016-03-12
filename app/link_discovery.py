"""
    Fuzzer Project
    SWEN-331
    Group 4
    
    This file is responsible for crawling all visible links
    within a webpage
"""

from app.packages.bs4 import BeautifulSoup, SoupStrainer
from urllib.parse import urljoin
import re

def crawl(url, session):
    
    """ initialize url stack """
    url_stack = set()
    url_stack.add(url)
    discovered_links = set()
    discovered_links.add(url)
    
    while(len(url_stack) > 0):
        curr_url = url_stack.pop()
        
        if "logout" in curr_url:
            """ Dont visit a logout link """
        else:
            """ Visit link and find urls within """
            request = session.get(curr_url)
            print("\nCrawling: " + curr_url)
 
            """ make partial link full """
            soup = BeautifulSoup(request.text)
            all_links = soup.findAll('a')
            for link in all_links:
                curr_link = urljoin(curr_url, link.get('href'))

                if curr_link not in discovered_links:
                    #should make this check base url but for this example
                    if "127.0.0.1" in curr_link and "logout" not in curr_link:
                        url_stack.add(curr_link)
                        discovered_links.add(curr_link)
                        print("Discovered: " + curr_link)
						
            # """ Regular expression to find urls """
            # urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', request.text)
            
            # """ Make sure we dont go surfing the web (rit is for testing) """
            # for link in urls:
                # if link not in discovered_links:
                    # if "localhost" in link or "127.0.0.1" in link or "www.rit.edu" in link:
                        # url_stack.add(link)
                        # discovered_links.add(link)
                        # print("Found: " + link)
    
    return discovered_links
