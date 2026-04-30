import sys
import os  # This is unsorted; 'os' should come after 'sys'

def main():
    unused_var = 10  # This variable is defined but not used anywhere
    print("Hello, world!")  # No trailing whitespace here

if __name__ == "__main__":
    main()  # This should be fine, no violations here
