
message = 'Hello World' #Declarando um string.

print (message) #imprimindo a string
print (len(message)) #tamanho da string
print (message[0]) #Primeiro char da string
print (message[-1]) #Ultimo char da string
print (message[:5] + "\tincludes the first but not the last") #Do primeiro ao quinto
print (message[6:]) #Do setimo elemento ao ultimosetimo
print (message.lower()) #Tudo mundo minisculo
print (message.upper()) #Todo mundo maiusculo
print (message.count('Hello')) #Contar quantas vezes a string Hello aparece na mensagem
print (message.count('l'))  #Contar quantas vezes o char l aparece na mensagem
print (message.find('World')) #Devolve a posicao na string que comeca a palavra World
print (message.find('Universe')) # Se nao tiver ele retorna -1

new_msg = message.replace('World', 'Universe') #Retorna uma string que substitui World por Universe

print(new_msg) 

greeting = 'Hello'
Name = 'Guilherme'

msg = greeting + ", " + Name #Concatenando Strings
print (msg)


msg = '{}, {}. Welcome!'.format(greeting,Name) #Organizando a concatenacao de forma distinta
print(msg)

msg = f'{greeting}, {Name}. Welcome!' #concatenando de forma a possibilitar manipulacao do objeto string
print(msg)

msg = f'{greeting.upper()}, {Name}. Welcome!' #concatenando de forma a possibilitar manipulacao do objeto string
print(msg)

print(dir(Name)) #metodos existentes
#print(help(str)) #informacao de todo a superclasse str
#print(help(str.lower())) #informacao de um metodo da classe