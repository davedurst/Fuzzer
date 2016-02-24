"""
    Fuzzer Project
    SWEN-331
    Group 4
"""

import sys
import utils.requests as requests

def discover(args):
	
    """ Global session to store history of our discovery """
    global session;	
	
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
		    
    print(session.cookies)
	sys.exit()
	print("*** Link Discovery ***")
	
	""" Basic crawler (utilize a stack) """
	
	print("*** Guessing Links ***")
	
	""" append common words with common urls to a base url """
		words = []
		with open(args.common_words, 'r') as f:
			words.append(f.read().strip())
		f.closed
		for s in words:
			if args.custom_auth.lower() == "dvwa":
				response = requests.get('http://127.0.0.1/dvwa/' + s + '.php')
				print(response)
				response = requests.get('http://127.0.0.1/dvwa/' + s + '.jsp')
				print(response)
			elif args.custom_auth.lower() == "bwapp":
				response = requests.get('http://127.0.0.1/bWapp/' + s + '.php')
				print(response)
				response = requests.get('http://127.0.0.1/bWapp/' + s + '.jsp')
				print(response)
	
	print("*** Parsing URLS ***")
	
	""" split the urls """
	
	print("*** Discovering Form Parameters ***")
	
	""" probably some api call """
	
	print("*** Discovering Cookies ***")
	
	""" probably some api call """
