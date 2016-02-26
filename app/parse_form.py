"""
    Fuzzer Project
    SWEN-331
    Group 4
"""

import utils.bs4 as bSoup

def parse(urls, session):
    
    for url in urls:
        print("Parsing form inputs for url: " + url)
        
        req = session.get(url)
        parse = bSoup(req.text)
        forms = parse.findAll('form')
        
        if len(forms) == 0:
            print("No forms found on page")
        
        for form in forms:
            print("Form name:   " + form["name"])
            print("Form method: " + form["name"])
            
            for tag in form.recursiveChildGenerator():
                if(tag.name == "input"):
                    if("name" in tag.attrs and "value" in tag.attrs):
                        print("Input tag name: " + tag["name"])
                        print("Input tag value: " + tag["value"])

def main():
    parse(["https://mycourses.rit.edu/"])

if __name__ == "__main__":
    main()
