"""
    Fuzzer Project
    SWEN-331
    Group 4
"""

import random

# Returns a string representing the response code (only common codes)
def get_status_code(code):
    if code == 200:
        return "200 --> Successful (OK)"
    if code == 303:
        return "303 --> Redirection (See Other)"
    if code == 400:
        return "400 --> Client Error (Bad Request)"
    if code == 401:
        return "401 --> Client Error (Unauthorized)"
    if code == 403:
        return "403 --> Client Error (Forbidden)"
    if code == 404:
        return "404 --> Client Error (Not Found)"
    if code >= 500:
        return code.__str__() + " --> Server Error"
    else:
        return code.__str__() + " --> Unknown Code" 

# Detects responses that take longer than expected
def analyze_response_time(response, timeout):
    load_time = response.elapsed.total_seconds() * 1000
    if load_time > timeout:
        print("Response took " + load_time + " ms.")
        print("Potential Denial Of Service Vulnerability")
            
# Detects unusual response codes and reports them
def analyze_status_code(response):
    if response.status_code != 200:
        print("Unexpected return code: " + get_status_code(response.status_code))

# Detects if sensitive data may have been leaked on a page
def analyze_sensitive_data(response, sensitive_words):
    for sensitive_word in sensitive_words:
        if sensitive_word in response.text:
            print("Response contained the following sensitive word: " + sensitive_word)

# Detects if vector was sanitized properly (only testing basic XSS attack)
def analyze_sanitization(response, vector):
    if '<' in vector and '>' in vector:
        if vector in response.text:
            print("The following vector wasn't sanititzed correctly: " + vector)
            print("This page may be vulnerable to cross site scripting")

# attack all inputs with vectors
def test_forms(form_dict, vectors, session, rand, timeout, sensitive_words):
    
    key_list = list(form_dict.keys())
    
    # if we want a random attack
    if rand:
        random.shuffle(key_list)
    
    # for each url & corresponding form list
    for url in key_list:
        
        print("Testing forms on: " + url)
        forms = form_dict[url]
        
        # for each form
        for form in forms:
            form_method = str(form['method']).lower()
            inputs = form.findAll('input')
            
            for vector in vectors:
                #dict of inputs -> vectors
                request_params = {}
                
                for _input in inputs:
                    if 'name' in _input.attrs:
                        name = _input['name']
                    elif 'type' in _input.attrs:
                        name = _input['type']
                        
                    if name.lower().strip() == 'submit':
                        request_params[name] = "Submit"
                    else:
                        request_params[name] = vector
                
                if form_method == "post":
                    post_response = session.post(url, params=request_params)
                    
                    analyze_response_time(post_response, timeout)
                    analyze_status_code(post_response)
                    analyze_sensitive_data(post_response, sensitive_words)
                    analyze_sanitization(post_response, vector)
                    
                elif form_method == "get":
                    get_response = session.get(url, params=post_params)
                    
                    analyze_response_time(post_response, timeout)
                    analyze_status_code(post_response)
                    analyze_sensitive_data(post_response, sensitive_words)
                    analyze_sanitization(post_response, vector)
  
def test_url_param(param_dict, vectors, session, rand, timeout, sensitive_words):
    #attack all url params with vectors
    return
   
def test(param_dict, form_dict, args, session):
    # read vectors
    vectors = open(args.vectors).readlines()
    sensitive_words = open(args.sensitive).readlines()
    
    print("\n*** Testing Vectors Against Forms ***\n")
    test_forms(form_dict, vectors, session, args.random, args.slow, sensitive_words)
    
    print("\n*** Testing Vectors Against URL Parameters ***\n")
    test_url_param(param_dict, vectors, session, args.random, args.slow, sensitive_words)
