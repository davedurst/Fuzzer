"""
    Fuzzer Project
    SWEN-331
    Group 4
"""

def parse(urls):
    
    """ for each url see if we have parameters """
    for curr_url in urls:
        print("Parameters found for url: " + curr_url)
        sub_divide = curr_url.split('?')
        
        """ if we have url parameters """
        if(len(sub_divide) > 1):
            """ get param key/value pairs """
            url_parameters = sub_divide[1].split('&')
            
            for key_val in url_parameters:
                key, val = key_val.split('=')
                print("Parameter: " + key + "; Value: " + val)
        else:
            print("No parameters found")
            
# test sequence
parse(["https://github.com/davedurst/Fuzzer/edit/master/app/parse_url.py"])
pares(["https://support.google.com/webmasters/answer/6080550?hl=en", "https://www.google.com/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=print%20all%20cookies%20for%20a%20session%20requests%20python"]
