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
        if "logout" in curr_url:
            """ Dont visit a logout link """
        else:
            """ Visit link and find urls within """
            request = session.get(curr_url)
            print("Crawling: " + curr_url)
            urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', curr_url)
            print(urls)
    
    return discovered_links
