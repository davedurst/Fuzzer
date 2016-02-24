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
    
    while(len(url_stack) > 0):
        curr_url = url_stack.pop()
        discovered_links.add(curr_url)
        
        if "logout" in curr_url:
            """ Dont visit a logout link """
        else:
            """ Visit link and find urls within """
            request = session.get(curr_url)
            print("Crawling: " + curr_url)
            
            """ Regular expression to find urls """
            urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', request.text)
            
            """ Make sure we dont go surfing the web (rit is for testing) """
            for url in urls:
                if "localhost" in url or "127.0.0.1" in url or "www.rit.edu" in url:
                    url_stack.push()
                    print("Found: " + url)
    
    return discovered_links
