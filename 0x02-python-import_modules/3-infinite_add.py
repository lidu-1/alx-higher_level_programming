#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    num_arg = 0
    for i in argv[1:]:
        num_arg = num_arg + int(i)
    print(num_arg)
