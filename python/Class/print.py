class Car:
    def __init__(self, brand, model, year):
        self.brand = brand # Initialize attributes
        self.model = model
        self.year = year                              

# Create Objects with attributes initialized
car1 = Car("Toyota", "Corolla", 2022)
car2 = Car("Tesla", "Model S", 2023)                             

print(car1.brand, car1.model, car1.year)
 # output: Toyota Corolla 2022
print(car2.brand, car2.model, car2.year)
 # output: Tesla Model S 2023                        