
class Person:
    number_of_people = 0 #esse não é característica de um objeto, mas da classe
    g = 9.81 #class property, not object property

    def __init__(self,name):
        self.name = name
        Person.addPerson()

    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod #it had access to cls props...
    def addPerson(cls):
        cls.number_of_people += 1

#p1 = Person("Amarante")
#print(Person.number_of_people_())
#p2 = Person("Gill")
#print(Person.number_of_people_())

print(Person.number_of_people_())

