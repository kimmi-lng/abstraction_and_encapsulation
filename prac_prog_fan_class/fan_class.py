class Fan:

    #constants
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    #instance variables
    def __init__(self, speed=SLOW, on=False, radius=5, color='blue'):
        self.__speed = int(speed)
        self.__on = bool(on)
        self.__radius = float(radius)
        self.__color = str(color)
    #getter method
    def get_speed(self):
        return self.__speed
    def get_on(self):
        return self.__on
    def get_radius(self):
        return self.__radius
    def get_color(self):
        return self.__color

    #setter method
    def set_speed(self, speed):
        self.__speed = int(speed)
    def set_on(self, on):
        self.__on = bool(on)
    def set_radius(self, radius):
        self.__radius = float(radius)
    def set_color(self, color):
        self.__color = str(color)