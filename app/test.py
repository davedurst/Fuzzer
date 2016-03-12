"""
    Fuzzer Project
    SWEN-331
    Group 4
"""

#Returns a string representing the response code (only common codes)
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

#Detects responses that take longer than expected
def analyze_response_time(response, timeout):
    load_time = response.elapsed.total_seconds() * 1000
    if load_time > timeout:
        print("Response took " + load_time + " ms.")
        print("Potential Denial Of Service Vulnerability")
            
#Detects unusual response codes and reports them
def analyze_status_code(response):
    if response.status_code != 200:
        print("Unexpected return code: " + get_status_code(response.status_code))

def analyze_sensitive_data(response):
    return

def analyze_sanitization(response, vector):
    return

def test(param_dict, form_dict, args):
    # access the global session
    global sess
    # read vectors
    vectors = open(args.vectors).readlines()
    # attack forms
    test_forms(form_dict, vectors, sess, args.random, args.timeout)
    # attack url params
    test_url_param(param_dict, vectors, sess, args.random, args.timeout)

def test_forms(form_dict, vectors, session, rand, timeout):
    #attack all inputs with vectors
    return
  
def test_url_param(param_dict, vectors, session, rand, timeout):
    #attack all url params with vectors
   return
