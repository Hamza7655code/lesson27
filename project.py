class Dog:
    species = "carnivores"
    
    def __init__(self, breed, color):
        self.breed = breed
        self.color = color
        
    def display(self):
        print("Species: {Dog.species}")
        print("Breed: {self.breed}")
        print("Color: {self.color}")

def main():
    dog1 = Dog("Golden Retriever", "Golden")
    dog2 = Dog("German Shepherd", "Black and Tan")
    
    print("Details of Dog 1:")
    dog1.display()
    
    print("Details of Dog 2:")
    dog2.display()

if __name__ == "__main__":
    main()