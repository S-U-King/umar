class Car:
    def __init__(self, brand, model, year):
        self.brand = brand # Initialize attributes
        self.model = model
        self.year = year                                                  

    def get(self):
        print(self.brand)
        print(self.model)
        print(self.year)                                 

# Create Objects with attributes initialized
car1 = Car("Toyota", "Corolla", 2022)
car2 = Car("Tesla", "Model S", 2023)                                   

car1.get()
car2.get()         