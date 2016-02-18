"""
    Fuzzer Project
    SWEN-331
    Group 4
"""
import utils.requests as requests
from utils.requests.auth import HTTPBasicAuth

def discover(args):
	
	""" Set up custom_auth """
	"""
	Psuedo: 
	"""
	if args.custom_auth != None:
		if args.custom_auth.lower() == "dvwa":
			response = requests.get('http://127.0.0.1/dvwa/login.php', auth=HTTPBasicAuth('admin', 'password'))
			print(response)
		elif args.custom_auth.lower() == "bwapp":
			#visit bodgeit with proper credentials
			response = requests.get('http://127.0.0.1/bWapp/login.php', auth=HTTPBasicAuth('bee', 'bug'))
			print(response)
		else:
			#invalid auth
			print(args.custom_auth + " is an invalid authentication input. Please choose from the following [dvwa, bwapp]")
	
	
	print("*** Link Discovery ***")
	
	""" Basic crawler (utilize a stack) """
	
	print("*** Guessing Links ***")
	
	""" append common words with common urls to a base url """
	
	print("*** Parsing URLS ***")
	
	""" split the urls """
	
	print("*** Discovering Form Parameters ***")
	
	""" probably some api call """
	
	print("*** Discovering Cookies ***")
	
	""" probably some api call """
