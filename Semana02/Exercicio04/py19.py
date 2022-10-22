
li = [9,1,8,2,7,3,6]

s_li = sorted(li) #retorna uma nova lista ordenada
print(s_li)
li.sort() # Afeta a lista original.. nao retorna nada
print(li) 

s_li = sorted(li, reverse=1) #retorna uma nova lista ordenada
print(s_li)

tup = (9,1,8,2,7,3,6)
#tup.sort() #nao existe
print(tup)

s_tup = sorted(tup) #retorna uma lista dos valores da tupla ordenados
print(s_tup)

di = {'name':"Goba", 'job': "Pedreiro", 'age': 100}
print(di)

s_di = sorted(di) #faz o sort das chaves em ordem alfabetica
print(s_di)

s_di = sorted(di.items()) #faz o sort das chaves, mas mostra os valores.
print(s_di)

li = [-6,-5,-4, 1, 2, 3]
print(li)
s_li = sorted(li, key=abs) #agora ele usa o valor absoluto como criterio para ordenamento
print(s_li)


class Employee():
    def __init__(self,name,age,salary): #construtor da classe
        self.name = name
        self.age = age
        self.salary = salary


    def __repr__(self): #representa o objeto como string, para o caso de querer unir os atributos, como o datetime faz muito...
        return '({},{},${})'.format(self.name, self.age, self.salary)

e1 = Employee('Marcos', 36, 1201)
e2 = Employee('Chiquinha', 70, 5000)
e3 = Employee('Musk Tusk', 30, 12000)


employees = [e1,e2,e3] 
print(employees)

def e_sort(emp):
    return emp.name

s_employees = sorted(employees, key=e_sort) #para fazer sort de uma lista de objetos, de um atributo do objeto, voce pode criar um callback function, que basicamente retorna o atributo que voce quer usar como regra
print(s_employees)

s_employees2 = sorted(employees, key=lambda e: e.name) #podemos usar uma funcao lambda
print(s_employees2)


from operator import attrgetter

s_employees3 = sorted(employees, key=attrgetter('age')) #podemos usar a funcao atribute getter.
print(s_employees3)
