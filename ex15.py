# Imports modules
from sys import argv
# Unpacks the argv module using two parameters
script, filename = argv
# specifies a txt file and opens the file specified by the "filename" parameter
txt = open(filename)
# prints a string along with the name of the file being opened
print "Here's your file %r:" % filename
# prints the contents of the txt file
print txt.read()
# Prints a string
print "Type the filename again:"
# Creates a variable and assigns user input to it
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
