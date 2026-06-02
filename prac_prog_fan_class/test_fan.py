from fan_class import Fan

def TestFan():

#For the first object, assign the maximum speed, radius 10, color yellow, and turn it on.
    fan1 = Fan(Fan.FAST, True, 10, 'yellow')

#Assign medium speed, radius 5, color blue, and turn it off for the second object.
    fan2 = Fan(Fan.MEDIUM, False, 5, 'blue')

#Display each object’s speed, radius, color, and on properties.
