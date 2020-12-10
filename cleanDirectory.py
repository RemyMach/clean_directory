#! /usr/bin/env python3
import sys, argparse
from moveFile import moveFile
from pathlib import Path

def getArgsForMoving():

    parser = argparse.ArgumentParser(description='Move file from source directory to destination directory with a name that correspond to regex')
    parser.add_argument('-s', '--source', help='directory where the files are, path from ~')
    parser.add_argument('-r', '--regex', help='name regex file')
    parser.add_argument('-d', '--destination', help='directory where the file are going, path from ~')
    args = parser.parse_args()

    if args.source is None or args.regex is None:
        print('Options -s -r -d is mandatory. Exiting...')
        parser.print_help()
        sys.exit(1)

    return args

if __name__ == "__main__":
    args = getArgsForMoving()
    source_directory = Path.home() / args.source
    if source_directory.is_dir() != True:
        raise Exception("Sorry the directory " + str(source_directory) + " doesn't exist")
    moveFile(source_directory, args)