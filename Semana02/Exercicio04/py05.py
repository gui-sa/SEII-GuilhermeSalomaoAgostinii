student = {'name': 'John', 'age': 25, 'course': ['Math','CompSci']} #Criando um dicionario... primeiro valor eh a chave e o segundo eh o valor em si
print(student['name']) #Acecando dicionario student pela chave name
print(student['course']) #Acecando dicionario student pela chave course

#Quando voce nao sabe a chave, use o metodo get.
print(student.get('name'))
print(student.get('nama')) #quando voce errar, ao inves de dar erro, vai retornar None
print(student.get('nama','Banana')) #quando voce errar, ao inves de dar erro, vai retornar ou o que voce quiser...

#Para acrescentar novos valores:
student ['phone'] = '00 00000 0000'
print(student.get('phone','Banana')) #quando voce errar, ao inves de dar erro, vai retornar ou o que voce quiser...

student ['name'] = 'John Cina'
print(student.get('name')) #Ele atualiza o valor do dicionario


student.update({'name': 'John Brabo', 'age': 26 }) #Ele atualiza o valor do dicionario
print(student)

student.update({'namo': 'John Brabo', 'age': 26 }) #Se voce errar na escrita, vai aparecer algo novo la no dicionario... cuidado.
print(student) 

#Para excluirmos um elemento de dentro:
del student['namo']
print(student) 

#Podemos dar o pop da caracteristica, tambem...
age = student.pop('age')
print(student) 
print(age) 
student.update({'age':26})
print(student) 


print(len(student))  #Retorna o numero de definicoes do dict.
print(student.keys())  #Retorna todas as chaves
print(student.items())  #Retorna todas as chaves e os valores

for key in student: #Itera a var key por cada valor de student... O primeiro a sair de cada elemento eh a chave
    print(key)

for key,value in student.items(): #Neste caso, o retorno eh duplo e por isso duas vars sao iteradas.
    print(key,value)


