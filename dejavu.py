#!/usr/bin/python

import os
import sys
import json
import warnings
import argparse

from dejavu import Dejavu
from argparse import RawTextHelpFormatter

warnings.filterwarnings("ignore")

def init():
    return Dejavu()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Dejavu: Audio Fingerprinting library",
        formatter_class=RawTextHelpFormatter)
    parser.add_argument('-f', '--fingerprint', nargs='*',
                        help='Fingerprint files in a directory\n'
                             'Usages: \n'
                             '--fingerprint /path/to/directory extension /path/to/fingerprint_directory\n'
                             '--fingerprint /path/to/file path/to/fingerprint_directory')
    args = parser.parse_args()

    if not args.fingerprint:
        parser.print_help()
        sys.exit(0)

    djv = init()
    if args.fingerprint:
        # Fingerprint all files in a directory
        if len(args.fingerprint) == 3:
            directory = args.fingerprint[0]
            extension = args.fingerprint[1]
            dest_directory = args.fingerprint[2]
            print("Fingerprinting all .%s files in the %s directory"
                  % (extension, directory))
            djv.fingerprint_directory(path=directory, extensions=["." + extension], 
                                        output_dir=dest_directory, nprocesses=4)

        elif len(args.fingerprint) == 2:
            filepath = args.fingerprint[0]
            dest_directory = args.fingerprint[1]
            if os.path.isdir(filepath):
                print("Please specify an extension if you'd like to fingerprint a directory!")
                sys.exit(1)
            djv.fingerprint_file(filepath=filepath, output_dir=dest_directory)
        elif len(args.fingerprint) == 1:
            print "The input has wrong fromat. Please follow the signature below.\n\n"
            parser.print_help()
            sys.exit(0)

    sys.exit(0)
