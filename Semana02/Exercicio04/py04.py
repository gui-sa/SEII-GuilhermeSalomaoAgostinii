
courses = ['History', 'Math', 'CompSci'] #Criando uma lista
print(courses) # Vai te mostrar a lista toda
print(len(courses)) # Vai te mostrar quantos elementos a lista possui

print(courses[0]) # Vai te mostrar o primeiro elemento da lista
print(len(courses[0])) # Vai te mostrar quantos elementos o primeiro elemento da lista possui

print(courses[-1]) # Vai te mostrar o ultimo elemento da lista
print(len(courses[-1])) # Vai te mostrar quantos elementos o ultimo elemento da lista possui

print(courses[0:2]) # Vai te mostrar uma lista que comeca do primeiro elemento e vai ate o segundo.
print(courses[:2]) # Vai te mostrar uma lista que comeca do primeiro elemento e vai ate o segundo.
print(courses[2:]) # Vai te mostrar uma lista que comeca do segundo e ir ate o ultimo

courses.append("Art") #Simplesmente coloca o elemento no final da lista (e aumenta o tamanho da lista)
print(courses)

#Para adicionar o elemento onde queremos (index):
courses.insert(2,'Chemist') #Inserting it into the third position.
print(courses)

courses_2 = ['Art', 'Education']

courses.insert(0,courses_2) # E possivel adicionar listas a lista.
print(courses) #Porem, a consulta do elemento da lista dentro da lista e piorado
print(courses[0][0]) 

popped = courses.pop(0) #Retorna o valor da primeira posicao  e remove ele da lista
print(popped)
print(courses)

courses.extend(courses_2) #Adiciona somente os valores da courses_2 dentro da courses
print(courses) #Agora a lista 2 vai se misturar a lista 1, removendo o problema de ter que consultar uma lista dentro de um elemento da lista

courses.remove('Art') #Remove um elemento Art caso exista
print(courses) 

courses.sort() #Ordena os elementos da forma alfabetica
print(courses) 

nums = [1,2,3, 5, 4] #Lista numerica
nums.sort() #Ordenacao acontece de forma crescente
print(nums)
nums.sort(reverse = 1) #Podemos reverter a ordenacao para decrescente ou de z->a para o caso de strings
print(nums)

sorted_courses = sorted(courses, reverse=True) #Retorna a lista ordenada ao inves de ordenar a lista origem.
print(sorted_courses)

print(min(nums)) #Retorna o valor minimo
print(max(nums)) #Retorna o valor maximo
print(sum(nums)) #Retorna o valor da soma de todos elementos

print(courses.index('Math')) #conseguir index do elemento Math caso exista
print(courses[courses.index('Math')])

print('Art' in courses) #Retorna um boolean se o elemento art existir em courses

for item in courses: #Iterando item (que assume cada elemento da lista de courses).
    print(item) 

for index, course in enumerate(courses): #Itera o index (que pode assumir qualquer nome), sendo que o index recebera o valor de enumerate() e o course, que assumira os valores do argumento de enumerate
    print(index, course)

for index, course in enumerate(courses, start=1): #Itera o index (que pode assumir qualquer nome), sendo que o index recebera o valor de enumerate() e o course, que assumira os valores do argumento de enumerate
    print(index, course)

course_str = ' , '.join(courses) #Printa a lista como uma string, e a separacao dos elemento e o ,
print(course_str)

course_str = ' - '.join(courses) #Printa a lista como uma string, e a separacao dos elemento e o -
print(course_str)

new_list = course_str.split(' - ') #Cria uma lista com base em uma string, em que cada elemento da lista e separado com o elemento -
print(new_list)

#Cuidado com igualdade em listas!
list_1 = [1, 2, 3]
list_2 = list_1
print(list_1)
print(list_2)
list_1[0] = "10"
print(list_1)
print(list_2)
print(list_1 is list_2) #Perceba que por tras dos panos, lista 1 e a lista 2.. como se o ponteiro fosse o mesmo.

#A forma correta:
list_1 = [1, 2, 3]
list_2 = list_1.copy()
print(list_1)
print(list_2)
list_1[0] = "10"
print(list_1)
print(list_2)
print(list_1 is list_2) #Agora a lista_1 e diferente da lista_2 por mais que inicialmente tivessem o mesmo valores... Os ponteiros sao diferentes!

#Da mesma forma com as tuplas:
tuple_1 = (1, 2, 3)
tuple_2 = tuple_1
print(tuple_1)
print(tuple_2)
print(tuple_1 is tuple_2)
#tuplas nao possuem metodos para copiar pois elas sao supostas de serem constantes!
#tuple_1[0] = 100 #Vai dar erro

#Sets: sao dicionarios sem chaves
cs_courses = {'History','Art','CompSci','Math','Math'}
art_courses = {'impressionism','Art','abstrata'}
print(cs_courses) #Nao aceita duplicatas

print(cs_courses.intersection(art_courses)) #Retorna os valores em comum
print(cs_courses.union(art_courses)) #Une as listas
print(cs_courses.difference(art_courses)) #Diferenca entre as listas


#Se queremos criar apenas uma lista, tupla e sets vazios
empty_list = []
empty_tuple = ()
empty_set = set() #Se colocamos somente {}, o interpretador vai ler como dicionario

