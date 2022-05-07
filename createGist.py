#!/usr/local/bin/python

import argparse, os
from decouple import config

def parseargs():
    parser = argparse.ArgumentParser(description='Create a GitHub Gist given a local file.')
    parser.add_argument('-f', '--file', help='A file to create the gist from.', required=True)
    args = parser.parse_args()
    return args.file

def authenticate():
    with open('token.txt', 'w') as f:
        f.write(config('GH_TOKEN'))
    os.system('gh auth login --with-token < token.txt')
    os.remove('token.txt')

def main():
    authenticate()
    os.system('gh gist create --public {}'.format(parseargs()))

if __name__ == "__main__":
    main()