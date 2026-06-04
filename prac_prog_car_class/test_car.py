from car_class import Car

class TestCar:

    def run(self):
        car = Car(1992, "McLaren F1")
        print(f'TESTING CAR: {car.get_year_model()}{car.get_make()}')
        
        print("ACCELERATING--")
        for i in range(1, 6):
            car.accelerate()
            print(f"Car current speed after accelerating {i}: {car.get_speed()} Kph")

        print("BRAKING--")
        for i in range(1, 6):
            car.brake()
            print(f"Car current speed after braking {i}: {car.get_speed()} Kph")