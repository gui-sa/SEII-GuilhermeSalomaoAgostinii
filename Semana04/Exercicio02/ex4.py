
class pet:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old! \n\n")

    def speak(self):
        print("Animals usually dont speak..")

class cat(pet):

    def __init__(self, name, age, color):
        super().__init__(name, age) # chama o construtor da classe pai
        self.color = color

    def meow(self):
        print("Meow")

    def show(self): #As classes com mesmo nome se sobrescrevem, ganhando a mais especifica
        print(f"I am {self.name} and I am {self.age} years old! I am {self.color}! \n\n")


class dog(pet):
    
    def bark(self):
        print("Bark")


p = pet("Tim",19)
p.show()
c = cat("Catarine",22 , "yellow")
c.show()
c.meow()
d = dog("Cata",22)
d.show()
d.bark()