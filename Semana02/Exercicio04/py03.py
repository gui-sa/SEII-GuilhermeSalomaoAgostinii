
num = 3 #declarando um valor 

print(type(num)) #verificando seu tipo: int 

num = 3.14

print(type(num)) #verificando seu tipo: float

print(3 + 2) #soma
print(3 - 2) #subtracao
print(3 * 2) #multiplicacao
print(3 / 2) #divisao
print("floor division: " + str(3 // 2)) #divisao pegando somente a divisao sem o resto
print(3 ** 2) #elevado
print(3 % 2) #resto da divisao

#Podemos usar o resto da divisao por 2 para averiguar a paridade
print(str(2%2) + " Par")
print(str(3%2) + " Impar")
print(str(4%2)  + " Par")
print(str(5%2) + " Impar")

#Efeito do parenteses nas contas
print(3 * 2 + 1)
print(3 * (2 + 1))

#Somando com ele mesmo
num = 1 
num = num + 1
print(num)

#Simplificando a soma com ele mesmo.
num += 1
print(num)

#Multiplicacao com ele mesmo
num = 1
num *= 10
print(num)

print(abs(-3)) #funcao absoluto
print(round(3.75, 1)) #funcao arredondamento com uma casa decimal

num_1 = 3
num_2 = 2

print(num_1 == num_2) #1 eh igual a 2?
print(num_1 != num_2) #1 eh diferente a 2?
print(num_1 > num_2) #1 eh maior a 2?
print(num_1 < num_2) #1 eh menor a 2?
print(num_1 <= num_2) #1 eh menor ou igual a 2?
print(num_1 >= num_2) #1 eh maior ou igual a 2?

#Cuidado com soma de numero em strings
num_1 = '100'
num_2 = '200'
print(num_1 + num_2) 

#Quando for string, devemos forcar a tipagem usando o cast
num_1 = int('100')
num_2 = int('200')
print(num_1 + num_2)