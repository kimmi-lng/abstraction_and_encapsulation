class Fan:
    #constants
    SLOW = 1
    MEDIUM = 2
    FAST = 3
    #instance variables
    def __init__(self, speed=SLOW, is_on=False, radius=5, color='blue'):
        self.__speed = int(speed)
        self.__is_on = bool(is_on)
        self.__radius = float(radius)
        self.__color = str(color)
    #getter method
    #setter method