class Dog:
    def __init__(self, Name, Breed):
        self.Name = Name
        self.Breed = Breed

    def __str__(self):
        return f"{self.Name} is a {self.Breed}" 

    def __repr__(self):
        return f"Dog('{self.Name}', '{self.Breed}')"

# creating an instance
dog = Dog("Rex", "Labrador")

# Usin print, which calls __str__
print(dog) # output: Rex is a labrador 

# Using repr, which is often used for debugging
print(repr(dog)) # Output: Dog('Rex', 'Labrador')