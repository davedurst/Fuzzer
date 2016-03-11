"""
    Fuzzer Project
    SWEN-331
    Group 4
"""

from app.packages.bs4 import BeautifulSoup

def parse(urls, session):
    
    """ form dictionary """
    forms = {}
    
    for url in urls:
        print("Parsing form inputs for url: " + url)
        
        req = session.get(url)
        parse = BeautifulSoup(req.text)
        forms[url] = parse.findAll('form')
        
        if len(forms) == 0:
            print("No forms found on page")
        
        for form in forms:
            print("Form method: " + form["method"])
            
            for tag in form.recursiveChildGenerator():
                if(tag.name == "input"):
                    if("name" in tag.attrs):
                        print("Input tag name: " + tag["name"])
                    if("value" in tag.attrs):
                        print("Input tag value: " + tag["value"])
                        
""" return our forms dictionary (url -> form(s) """
return forms

def main():
    parse(["https://mycourses.rit.edu/"])

if __name__ == "__main__":
    main()
