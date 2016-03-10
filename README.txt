Fuzzer
SWEN 331
Team 4: David Durst, Kris Brown, Kaicheng Guo
---------------------------------------------

---------------------------------------------
Dependencies:
---------------------------------------------

Python 3.4.3
Beautiful Soup 4
Python Requests Package

---------------------------------------------
How to run:
---------------------------------------------

This project can be run from the terminal inside of the Fuzzer directory.
All output will be printed to sdtout

---------------------------------------------
DISCOVER:
---------------------------------------------

Generic run:
python fuzzer.py discover [url] --custon-auth=[dvwa, bwapp] --common-words=[filename]

Example run:
python fuzzer.py discover http://127.0.0.1/dvwa/ --custom-auth=dvwa --common-words=common-words.txt

---------------------------------------------
TEST:
---------------------------------------------

Generic run:
python fuzzer.py test [url] --custom-auth=[dvwa, bwapp] --common-words=[filename] --vectors=[filename] --sensitive=[filename] [--random] --slow=[milliseconds]

Example run:
python fuzzer.py test http://127.0.0.1/dvwa/ --custom-auth=dvwa --common-words=words.txt --vectors=vectors.txt --sensitive=sensitive.txt --random --slow=500
