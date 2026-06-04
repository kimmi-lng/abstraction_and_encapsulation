class Pet:
    def __init__(self):
        self.__name = "" #name of pet
        self.__animal_type = "" #type of animal
        self.__age = 0 #for pets age

    #setter method
    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    #getter method
    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age
