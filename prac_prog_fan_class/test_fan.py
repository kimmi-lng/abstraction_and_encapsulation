from fan_class import Fan

class TestFan:

    def run(self):
        #For the first object, assign the maximum speed, radius 10, color yellow, and turn it on.
        fan1 = Fan(Fan.FAST, True, 10, 'yellow')

        #Assign medium speed, radius 5, color blue, and turn it off for the second object.
        fan2 = Fan(Fan.MEDIUM, False, 5, 'blue')

        #Display each object’s speed, radius, color, and on properties.
        print('Fan 1 properties:')
        print(f'Speed: {fan1.get_speed()}')
        print(f'Radius: {fan1.get_radius()}')
        print(f'Color: {fan1.get_color()}')
        print(f'On: {fan1.get_on()}')

        print('\nFan 2 properties:')
        print(f'Speed: {fan2.get_speed()}')
        print(f'Radius: {fan2.get_radius()}')
        print(f'Color: {fan2.get_color()}')
        print(f'On: {fan2.get_on()}')
