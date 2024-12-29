class Animal:
    """Base class for all animals."""
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def speak(self):
        """Default behavior for speak. Can be overridden in subclasses."""
        return f"{self.name} makes a sound."
    
    def eat(self):
        """Default behavior for eating."""
        return f"{self.name} is eating."

class Lion(Animal):
    """Lion class, inherits from Animal."""
    
    def __init__(self, name):
        super().__init__(name, species="Lion")
    
    def speak(self):
        return f"{self.name} roars!"
    
    def eat(self):
        return f"{self.name} is devouring a carcass."

class Elephant(Animal):
    """Elephant class, inherits from Animal."""
    
    def __init__(self, name):
        super().__init__(name, species="Elephant")
    
    def speak(self):
        return f"{self.name} trumpets!"
    
    def eat(self):
        return f"{self.name} is munching on grass."

class Zebra(Animal):
    """Zebra class, inherits from Animal."""
    
    def __init__(self, name):
        super().__init__(name, species="Zebra")
    
    def speak(self):
        return f"{self.name} makes a whinny sound!"
    
    def eat(self):
        return f"{self.name} is grazing on some plants."

class Monkey(Animal):
    """Monkey class, inherits from Animal."""
    
    def __init__(self, name):
        super().__init__(name, species="Monkey")
    
    def speak(self):
        return f"{self.name} screeches!"
    
    def eat(self):
        return f"{self.name} is eating some fruit."

class Zoo:
    """Zoo class to manage different animals."""
    
    def __init__(self):
        self.animals = []
    
    def add_animal(self, animal):
        self.animals.append(animal)
    
    def show_animals(self):
        """Display all the animals and their actions."""
        for animal in self.animals:
            print(f"{animal.species} - {animal.name}")
            print(f"Speak: {animal.speak()}")
            print(f"Eating: {animal.eat()}")
            print("-" * 40)

my_zoo = Zoo()

lion = Lion("Leo")
elephant = Elephant("Dumbo")
zebra = Zebra("Zara")
monkey = Monkey("Milo")

my_zoo.add_animal(lion)
my_zoo.add_animal(elephant)
my_zoo.add_animal(zebra)
my_zoo.add_animal(monkey)

my_zoo.show_animals()
