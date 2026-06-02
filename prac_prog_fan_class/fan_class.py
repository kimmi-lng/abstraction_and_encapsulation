class Fan:

    #constants
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    #instance variables
    def __init__(self, speed=SLOW, on=False, radius=5, color='blue'):
        self._speed = int(speed)
        self._on = bool(on)
        self._radius = float(radius)
        self._color = str(color)

    #getter method
    def get_speed(self):
        return self._speed
    def get_on(self):
        return self._on
    def get_radius(self):
        return self._radius
    def get_color(self):
        return self._color
    
    #setter method
    def set_speed(self, speed):
        self._speed = int(speed)
    def set_on(self, on):
        self._on = bool(on)
    def set_radius(self, radius):
        self._radius = float(radius)
    def set_color(self, color):
        self._color = str(color)