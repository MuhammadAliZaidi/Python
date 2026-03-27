# Import cowsay library (prints messages in a cow speech bubble)
import cowsay

# Import sys to access command-line arguments
import sys

# Check if exactly one argument (name) is provided
if len(sys.argv) == 2:
    # sys.argv[1] is the name passed from terminal
    # Concatenate 'hi ,' with the name
    cowsay.cow('hi, ' + sys.argv[1])

# This will always run (even if no argument is provided)
# So the cow will always say "hello"
cowsay.cow('hello')
cowsay.trex('hello')
