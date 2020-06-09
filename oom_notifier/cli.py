import sys
import os

def fork():
    if os.fork():
        sys.exit()

def main():
    fork()
