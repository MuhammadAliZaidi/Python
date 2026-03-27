"""
argv Practice Program
---------------------
This file demonstrates two ways of handling command-line arguments (sys.argv):

1. Basic loop with manual skipping
2. Pythonic slicing (sys.argv[1:])
"""

import sys


# -----------------------------
# Version 1: Basic Approach
# -----------------------------
def basic_version():
    print("=== Basic Version ===")

    # Check if at least one argument is provided
    if len(sys.argv) < 2:
        sys.exit("Too few arguments")

    # Loop through all arguments
    for arg in sys.argv:
        # Skip the first element (file name)
        if arg == sys.argv[0]:
            continue

        print("My name is", arg)


# -----------------------------
# Version 2: Pythonic Approach
# -----------------------------
def pythonic_version():
    print("\n=== Pythonic Version ===")

    # Check again (good practice if function is reused)
    if len(sys.argv) < 2:
        sys.exit("Too few arguments")

    # sys.argv[1:] skips the filename automatically
    for arg in sys.argv[1:]:
        print("My name is", arg)


# -----------------------------
# Main Function
# -----------------------------
def main():
    basic_version()
    pythonic_version()


# Run program
if __name__ == "__main__":
    main()
