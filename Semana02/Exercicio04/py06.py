if True: #condicional if statement
    print("Verdadeiro")

if False: #condicional
    print("Nunca vai printar")


lang = 'Python'
if lang =='Python': #comparacao de igualdade...
    print("Verdadeiro")

if lang !='Python': #comparacao de diferenca...
    print("Verdadeiro")
else: #Se falhar, ele executa esses comandos
    print("Falso")

lang = 'Java'
if lang =='Python':
    print("Verdadeiro")
elif lang =='Java': #Se o primeiro falhar, tente essa comparacao...
    print("Javinha...")
else:
    print("Falso")

lang = 'Java'
logged_in = True
if lang == 'Java' and logged_in: #Alem do retorno da primeira precisar ser positivo, o retorno da segunda tambem precisa
    print("Permission Granted")

lang = 'Java'
logged_in = False
if lang == 'Java' and logged_in: #Alem do retorno da primeira precisar ser positivo, o retorno da segunda tambem precisa
    print("Permission Granted")
else:
    print("Falhou")

if not logged_in: #Podemos negar o estado...
    print("You need to be logged")


a = [1,2,3]  
b = [1,2,3]  
print(a == b) #Retorna verdadeiro pois os valores sao iguais
print(a is b) #Retorna falso pois os ponteiros sao diferentes
print(id(a)) #Pega o id do objeto
print(id(b)) #Pega o id do objeto

a = [1,2,3]  
b = a
print(a == b) #Retorna verdadeiro pois os valores sao iguais
print(a is b) #Retorna falso pois os ponteiros sao diferentes
print(id(a)) #Pega o id do objeto
print(id(b)) #Pega o id do objeto

#Avaliando o significado booleano das tipagens
condition = False #falso

if condition:
    print("Verdadeiro")
else:
    print("Falso")

condition = None #falso

if condition:
    print("Verdadeiro")
else:
    print("Falso")

condition = 0 #falso

if condition:
    print("Verdadeiro")
else:
    print("Falso")

condition = 15 #verdadeiro

if condition:
    print("Verdadeiro")
else:
    print("Falso")

condition = True #verdadeiro

if condition:
    print("Verdadeiro")
else:
    print("Falso")


condition = 1 #verdadeiro

if condition:
    print("Verdadeiro")
else:
    print("Falso")

condition = [] #falso

if condition:
    print("Verdadeiro")
else:
    print("Falso")

condition = () #falso

if condition:
    print("Verdadeiro")
else:
    print("Falso")

condition = [10,100] #verdadeiro

if condition:
    print("Verdadeiro")
else:
    print("Falso")


condition = "Yeah" #verdadeiro

if condition:
    print("Verdadeiro")
else:
    print("Falso")

condition = "" #falso

if condition:
    print("Verdadeiro")
else:
    print("Falso")