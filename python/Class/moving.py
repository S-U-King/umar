class Car:
    def __init__(self, brand, model, year):
        self.brand = brand # Initialize attributes
        self.model = model
        self.year = year   

    def start(self):
        print(f"{self.brand} {self.model} is starting!")                      

    def stop(self):
        print(f"{self.brand} {self.model} is stoping!")                        


# Create an object
my_car = Car("Toyota", "Corolla", 2022)                     
my_car.start() # Output: Toyota Corolla is starting!
my_car.stop()  # Output: Toyota Corolla is stoping! 