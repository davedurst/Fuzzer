"""
    Fuzzer Project
    SWEN-331
    Group 4
"""

def get_cookies(session):
    for cookie in session.cookies:
        print(cookie)
