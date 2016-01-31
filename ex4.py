# Assigns the integer 100 to the variable cars
cars = 100
# Assigns the floating point 4.0 to the variable space_in_a_car
space_in_a_car = 4.0
# Assigns the integer 30 to the variable drivers
drivers = 30
# Assigns the integer 90 to the variable passengers
passengers = 90
# Assigns the outcome of cars - drivers to the variable cars_not_driven
cars_not_driven = cars - drivers
# Assigns drivers to cars_driven
cars_driven = drivers
# Assigns the product of cars_driven and space_in_a_car to carpool_capacity
carpool_capacity = cars_driven * space_in_a_car
# Assigns the outcome of passengers divided by cars_driven to average_passengers_per_car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be ", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
