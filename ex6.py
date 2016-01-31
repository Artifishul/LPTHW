# craetes a variable and uses formatters to insert the number 10
x = "There are %d types of people." % 10
# assigns a string to a variable
binary = "binary"
# assigns a s tring to a variable
do_not = "don't"
# assigns a string to a variable  that has two formatters referencing two variables
y = "Those who know %s and those who %s." % (binary, do_not)
# prints a variable
print x
# prints a variable
print y
# prints a string and a variable that is inserted via a formatter
print "I said: %r." % x
# same again
print "I also said: '%s'." % y
# assigns a boolean to a variable
hilarious = False
# assigns a string and a formatter to a variable
joke_evaluation = "Isn't that joke so funny?! %r"
# prints two variables
print joke_evaluation % hilarious
# assigns a string to a variable
w = "This is the left side of..."
# assigns a string to a variable
e = "a string with a right side."
# prints two variables that are concentenated (using "+" sign)
print w + e
