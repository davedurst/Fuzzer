"""
    Fuzzer Project
    SWEN-331
    Group 4
"""

from app.packages import requests

def valid_page(url_guess, session):
    request = session.get(url_guess)
    return (request.status_code == requests.codes.ok)

def guess(discovered_links, session, common_words):
    guessed_links = set()

    """ Read endings into list """
    f = open("common-endings.txt", 'r')
    endings = f.read().split()

    """ Read words into list """
    f = open(common_words, 'r')
    words = f.read().split()

    print(words)
    
    """ for each page that isnt a file """
    for link in discovered_links:
        if link[-1] == '/':
        
            """ for every word/ending combination """
            for word in words:
                for ending in endings:
                    guess = link + word + ending

                    """ if its a page, add it to guessed links list """
                    if(valid_page(guess, session)):
                        guessed_links.add(guess)
                        print("Guessed page: " + guess)
                        
    return guessed_links
