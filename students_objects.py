class Student:
    pass

    def __init__(self, name, object):
        self.name = name
        self.object = object

    def greet(self):
        print(f'Hello, I\'m {self.name}. My favorite subjects are: {self.object[0]} {self.object[1]}')

ivan = Student("Ivan Ivanov", ["maths", "phisics"])
alex = Student("Alex Petrov", ["arts", "music"])
maria = Student("Maria Popova", ["chemistry", "biology"])

print(ivan.greet())
print(alex.greet())
print(maria.greet())
