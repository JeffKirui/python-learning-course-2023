import sys

from Sayings import hello

if len(sys.agrv) == 2:
    hello(sys.agrv[1])