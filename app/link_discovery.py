"""
    Fuzzer Project
    
    This file is responsible for crawling all visible links
    within a webpage
"""

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
            print("Crawling: " + curr_url)
            
            """ Regular expression to find urls """
            urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', request.text)
            
            """ Make sure we dont go surfing the web (rit is for testing) """
            for link in urls:
                if link not in discovered_links:
                    if "localhost" in link or "127.0.0.1" in link or "www.rit.edu" in link:
                        url_stack.add(link)
                        discovered_links.add(link)
                        print("Found: " + link)
    
    return discovered_links
