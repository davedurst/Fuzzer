"""
    Fuzzer Project
    SWEN-331
    Group 4
"""

def parse(urls):
    #dictionary of dictionaries (Key: url; Value: Parameter dictionary)
    param_dict = dict()
    
    """ for each url see if we have parameters """
    for curr_url in urls:
        print("\nFinding parameters for url: " + curr_url)
        base, curr_url_params = parse_url(curr_url)
        param_dict[base] = curr_url_params

    return param_dict
   
def parse_url(url):
    url_params = dict()
    sub_divide = url.split('?')
        
    """ if we have url parameters """
    if(len(sub_divide) > 1):
        """ get param key/value pairs """
        if '#' in sub_divide[1]: 
            #case where there are additional url fragments after params
            parameters = sub_divide[1].split('#')
            url_parameters = parameters[0].split('&')
        else:
            url_parameters = sub_divide[1].split('&')

        for key_val in url_parameters:
            if(len(key_val.split('=')) == 2):
                key, val = key_val.split('=')
                url_params[key] = val
                print("Parameter: " + key + "; Value: " + val)
    else:
        print("No parameters found")
    
    #return the base url and the parameter dictionary
    return sub_divide[0], url_params
    
#some tests
def main():
    """ Try url with no query parameters """
    parse(["https://github.com/davedurst/Fuzzer/edit/master/app/parse_url.py"])
    
    """ Try url with query parameters """
    parse(["https://mycourses.rit.edu/d2l/lp/profile/profile_edit.d2l?ou=587073"])
    
    """ Try url with additional shit (fragments) """
    parse(["abc://username:password@example.com:123/path/data?key=value#fragid1"])

if __name__ == '__main__':
    main()
