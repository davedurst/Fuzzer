"""
    Fuzzer Project
    SWEN-331
    Group 4
"""

from app.packages.bs4 import BeautifulSoup

def parse(urls, session):
    
    for url in urls:
        print("Parsing form inputs for url: " + url)
        
        req = session.get(url)
        parse = BeautifulSoup(req.text)
        forms = parse.findAll('form')
        
        if len(forms) == 0:
            print("No forms found on page")
        
        for form in forms:
            print("Form method: " + form["method"])
            
            for tag in form.recursiveChildGenerator():
                if(tag.name == "input"):
                    if("name" in tag.attrs and "value" in tag.attrs):
                        print("Input tag name: " + tag["name"])
                        print("Input tag value: " + tag["value"])

def main():
    parse(["https://mycourses.rit.edu/"])

if __name__ == "__main__":
    main()
