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
    #setter method