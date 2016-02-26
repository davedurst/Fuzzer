Fuzzer
SWEN 331
Team 4: David Durst, Kris Brown, Kaicheng Guo
---------------------------------------------

---------------------------------------------
Dependencies:
---------------------------------------------

Python 3.2
Beautiful Soup 4
Python Requests Package

---------------------------------------------
How to run:
---------------------------------------------

This project can be run from the terminal inside of the Fuzzer directory.

Generic run:
python fuzzer.py discover [url] --custon-auth=[dvwa, bwapp] --common-words=[filename]

Example run:
python fuzzer.py discover http://127.0.0.1/dvwa/ --custom-auth=dvwa --common-words=common-words.txt
