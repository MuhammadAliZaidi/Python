import sys
if len(sys.argv)<2:
    sys.exit(print('Too few arguments'))
elif len(sys.argv)>2:
    sys.exit(print('Too many arguments'))
else:
    print('My name is ',sys.argv[1])
