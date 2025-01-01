class Dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
    
    # Method (behaviour)
    def bark(self):
        print(f"{self.name} says woof!")

    def get_breed(self):
        return self.breed

# Create Object with initialize attributes
dog1 = Dog("Rex", "Lebrador")
dog2 = Dog("Bella", "Bulldog")

# access attributes
print(dog1.name)
print(dog2.breed)

# calling methods
dog1.bark()
dog2.bark()