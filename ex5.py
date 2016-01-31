name = 'Liam Edwards'
age = 20 # not a lie
height = 72 # inches
weight = 170 # lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Dirty blonde'

print "Lets talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight,
age + height + weight)
