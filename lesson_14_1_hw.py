class Dog:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def jump(self):
        print(f'{self.name} is jumping')

    def run(self):
        print(f'{self.name} is running')

    def bark(self):
        print(f'{self.name} is barking')

    def change_name(self, new_name):
        self.name = new_name


dog = Dog('Max', 5, 0.5, 15)
dog.jump()
dog.run()
dog.jump()
dog.__dict__

print(f"Dog's name is {dog.name.capitalize()}")
dog.change_name(input(f'Enter a new name for the dog: ').capitalize())
print(f"Dog's new name is {dog.name.capitalize()}")
