from fan_class import Fan
def main():
#For the first object, assign the maximum speed, radius 10, color yellow, and turn it on.
    fan1 = Fan(Fan.FAST, True, 10, 'yellow')
#Assign medium speed, radius 5, color blue, and turn it off for the second object.
    fan2 = Fan(Fan.MEDIUM, False, 5, 'blue')
#Display each object’s speed, radius, color, and on properties.
    print("Fan 1:")
    print("Speed:", fan1.get_speed())
    print("On:", fan1.get_on())
    print("Radius:", fan1.get_radius())
    print("Color:", fan1.get_color())

    print("\nFan 2:")
    print("Speed:", fan2.get_speed())
    print("On:", fan2.get_on())
    print("Radius:", fan2.get_radius())
    print("Color:", fan2.get_color())
