from pet_class import Pet

class TestPet:
    def run(self):
        pet1 = Pet()
        print("INPUT PET DETAILS:\n")

        name = str(input("Enter pet's name: "))
        type_of_animal = str(input("Enter pet's type of animal: "))
        age = int(input("Enter pet's age: "))

        pet1.set_name(name)
        pet1.set_animal_type(type_of_animal)
        pet1.set_age(age)

        print("\nPET PROFILE:")
        print(f"Name: {pet1.get_name()}")
        print(f"Type of animal: {pet1.get_animal_type()}")
        print(f"Age: {pet1.get_age()} years old")   
