"""
    Fuzzer Project
    SWEN-331
    Group 4
"""

import argparse
import sys
import app.discover as disc
import app.test as test

# This is the entry point for the application

def main():
    
    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument('--custom-auth', nargs='?', type=str)
    parent_parser.add_argument('url')

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(title='Commands', description='The commands the app can run', dest='cmd')

    """ Discover options """
    discover_parser = subparsers.add_parser('discover', parents=[parent_parser])
    discover_parser.add_argument('--common-words', nargs='?', type=str, required=True)

    """ Test options """
    test_parser = subparsers.add_parser('test', parents=[parent_parser])
    test_parser.add_argument('--common-words', nargs='?', type=str, required=True)
    test_parser.add_argument('--vectors', nargs='?', type=str, required=True)
    test_parser.add_argument('--sensitive', nargs='?', type=str, required=True)
    test_parser.add_argument('--random', action='store_true', default=False, required=False)
    test_parser.add_argument('--slow', nargs='?', type=int, default=500, required=False)
    
    if len(sys.argv) == 1:
        parser.print_help()
    else:
        args = parser.parse_args()

        if args.cmd == 'discover':
            print("Running discover on base url: " + args.url + "\n")
            disc.discover(args)
			
        elif args.cmd == 'test':
            print("Running discover and test on base url: " + args.url + "\n")
            param_dict, form_dict, session = disc.discover(args)
            test.test(param_dict, form_dict, args, session)

if __name__ == '__main__':
    main()
