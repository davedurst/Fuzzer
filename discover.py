"""
    Fuzzer Project
    SWEN-331
    Group 4
"""

import sys
import utils.requests as requests
from app import link_discovery, link_guessing, parse_url

session = requests.Session()

def discover(args):
	
    """ Global session to store history of our discovery """
    global session	
	
    """ Set up custom_auth """
    if args.custom_auth != None:
        if args.custom_auth.lower() == "dvwa":
            """ Login and set security level to low """
            session.post("http://127.0.0.1/dvwa/login.php", data={'Login': '1', 'username': 'admin', 'password': 'password'})
            session.post("http://127.0.0.1/dvwa/security.php", data={'seclev_submit' : '1', 'security' : 'low'})
        elif args.custom_auth.lower() == "bwapp":
            """ Login """
            session.post("http://127.0.0.1:8080/bodgeit/login.jsp", data={'username': 'test@thebodgeitstore.com', 'password': 'password'})
        elif args.custom_auth.lower() == "test":
            """ Login to test site (mycourses) """
            session.post("https://mycourses.rit.edu/", data={'username': 'dnd7249', 'password': 'thisisnotmypassword'})
        else:
            """ Invalid auth """
            print(args.custom_auth + " is an invalid authentication input. Available options inlude: [dvwa, bwapp]\n")
            sys.exit()
    
    print("\n*** Link Discovery ***\n")
    discovered_links = link_discovery.crawl(args.url, session)
    
    print("\n*** Guessing Links ***\n")
    guessed_links = link_guessing.guess(discovered_links, session, args.common_words)
    final_urls = discovered_links + guessed_links
	
    print("\n*** Parsing URLS ***\n")
    parse_url.parse(final_urls)

    print("*** Discovering Form Parameters ***")
	
    """ probably some api call """
	
    print("*** Discovering Cookies ***")
