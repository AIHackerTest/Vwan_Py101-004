#! python2
cars=100
space_in_a_car=4 ## replace float with int to make a meaningful whole number of carpool_capacity
drivers=30
passengers=90
cars_not_driven=cars-drivers
cars_driven=drivers
carpool_capacity=cars_driven * space_in_a_car
average_passengers_per_car=passengers/cars_driven


print ('There are ",cars,"cars available"，"There are only", drivers, "drivers available.' )
print ('There will be", cars_not_driven, "empty cars today.' )
print ('We can transport", carpool_capacity, "people today.')
print ('We have", passengers, "to carpool today.')
print ('We need to put about", average_passengers_per_car, "in each car.')
