"""
    Fuzzer Project

"""

import utils.requests as requests

common_endings = [".jsp", ".php"]

def valid_page(url_guess, session):
    request = session.get(url_guess)
    return (request.status_code == requests.codes.ok)

def guess(discovered_links, session, common_words):
   guessed_links = set()

    """ Read words into list """
    words = []
    with open(args.common_words, 'r') as f:
	    words.append(f.read().strip())
    f.closed
    
    """ for each page that isnt a file """
    for link in discovered_links:
        if link[-1] == '/':
        
            """ for every word/ending combination """
            for word in words:
                for ending in common_endings:
                    guess = link + word + ending
                    
                    """ if its a page, add it to guessed links list """
                    if(valid_page(guess, session)):
                        guessed_links.add(guess)
                        print("Guessed page: " + guess)
                        
    return guessed_links
