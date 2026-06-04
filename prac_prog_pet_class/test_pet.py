from pet_class import Pet

class TestPet:
    def run(self):
        pet1 = Pet()
        print("INPUT PET DETAILS:")

        name = str(input("Enter pet's name: "))
        type_of_animal = str(input("Enter pet's type of animal: "))
        age = int(input("Enter pet's age: "))

        pet1.set_name(name)
        pet1.set_animal_type(type_of_animal)
        pet1.set_age(age)