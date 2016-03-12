"""
    Fuzzer Project
    SWEN-331
    Group 4
"""

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
