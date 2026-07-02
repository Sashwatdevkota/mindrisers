# polymorphism: poly: multiple


a = 1
b = 1

x = "hello"
y = "world"

print(a.__add__(b))
print(x.__add__(y))


class Dog:
    def move(self):
        print("Dog move with legs")


class Bird:
    def move(self):
        print("Bird move using wings.")


class Fish:
    def move(self):
        print("Fish move using fins.")


d1 = Dog()
b1 = Bird()
f1 = Fish()

d1.move()
b1.move()
f1.move()
