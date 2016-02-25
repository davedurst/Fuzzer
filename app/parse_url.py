"""
    Fuzzer Project
    SWEN-331
    Group 4
"""

def parse(urls):
    
    """ for each url see if we have parameters """
    for curr_url in urls:
        print("\nFinding parameters for url: " + curr_url)
        sub_divide = curr_url.split('?')
        
        """ if we have url parameters """
        if(len(sub_divide) > 1):
            """ get param key/value pairs """
            if '#' in sub_divide[1]:
                parameters = sub_divide[1].split['#']
                url_parameters = parameters[0].split('&')
            else:
                url_parameters = sub_divide[1].split('&')

            for key_val in url_parameters:
                if(len(key_val.split('=')) == 2):
                    key, val = key_val.split('=')
                    print("Parameter: " + key + "; Value: " + val)
        else:
            print("No parameters found")

def test_parse():
    """ Try url with no query parameters """
    parse(["https://github.com/davedurst/Fuzzer/edit/master/app/parse_url.py"])
    
    """ Try url with query parameters """
    parse(["https://mycourses.rit.edu/d2l/lp/profile/profile_edit.d2l?ou=587073"])
    
    """ Try url with additional shit (fragments) """
    parse(["abc://username:password@example.com:123/path/data?key=value#fragid1"])
    
def main():
    test_parse()
    
