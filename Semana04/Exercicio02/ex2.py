

class dog:
    def __init__(self, name, age): #Constructor
        self.name = name
        self.age = age

    def math_dog(self,x):
        return x+1
    def bark(self):
        print("WoooF")

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_name(self,name):
        self.name = name

    def set_age(self,age):
        self.age = age


d = dog("Totó",12)
print(type(d))

d.bark()
print(type(d.bark()))

print(d.math_dog(5))
print(d.name)

d2 = dog("Luluzinha",30)
print(d2.name)

print(d.get_name())
print(d2.get_name())
print(d2.get_age())

d.set_name( "Camperio" ) 
print(d.get_name())
