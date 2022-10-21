def hello_funtion(): #def eh a tipagem para definir funcao. entre () estao os inputs
    print("Hello World!")

def function_that_does_nothing_yet(): #quando nao se sabe o que a funcao faz (esta somente planejando), use o pass para nao dar erro.
    pass

hello_funtion()
function_that_does_nothing_yet() #nao vai fazer nada e nao vai dar erro.

print(hello_funtion) #vai retornar o id da funcao
print(hello_funtion()) #vai retornar o que a funcao retornar, nesse caso nada

#funcoes sao usadas para reduzir, modularizar e reutilizar codigos... facilita manutencao.
#DRY : Dont Repeat Yourself.

def hello_funtion2(): #retornando um string
    return "Hello World!"

hello_funtion2() #Nao vai fazer nada pois eh uma string
print(hello_funtion2()) #Agora sim.

#a funcao recebe entradas e retorna uma saida.
print(hello_funtion2().upper()) #podemos mexer com o tipo retornado livremente.

def hello_funtion3(greeting): #retornando um string
    return '{} Yeahh.'.format(greeting)
print(hello_funtion3("Hi")) #Estamos passando o Hi como parametro... uma string. Se nao passarmos vai dar erro pois nao possui valor default.

def hello_funtion4(greeting = "EI EI!!"): #possui um valor padrao
    return '{} Yeahh.'.format(greeting)
print(hello_funtion4("Hi")) #Sobrescreve caso o argumento seja passadp
print(hello_funtion4()) #Caso nao seja, ele usa o default

def hello_funtion5(greeting = "EI EI!!",name="Beutifull?"): #Mais de um argumento
    return '{} Yeahh. How are you, {}'.format(greeting,name)
print(hello_funtion5("Hi","Carolina")) #Sobrescreve caso o argumento seja passadp
print(hello_funtion5()) #Caso nao seja, ele usa o default

#Vale lembrar que os requisitos MINIMOS (Sem default) Precisam vir antes dos que possuem DEFAULT na especificacao da funcao

def student_info(*args,**kwargs):#aceita um numero arbitrario de argumentos posicionais (args) e argumentos chaves (kwargs).. Os nomes nao precisam ser args/kwargs ... o que precisa eh da * e **
    print(args)
    print(kwargs)

student_info("Math", 'Art', name="John", age=22) #chaves: name="John", posicionais: "Math"
#os posicionais se tornam tuplas e os chaves se tornam dicionarios


courses = ['Math', "Art"]
info = { 'name': 'Mah', 'age':22}
student_info(courses, info)  #Apesar de ser no mesmo formato do retorno, ele nao vai interpretar como desejado... Ele vai captar todo mundo como posicional e colocar a lista e o dicionario como elementos de uma tupla.

#Para desenpacotar precisamos informar: * para posicional e ** para chave
student_info(*courses, **info)  #com o simbolo e o tipo correto, ele vai desempacotar corretamente!!


def more_options(num:int, name:str = None)->str: #colocar esse var:type, ajuda a explicar para a pessoa o que esses argumentos sao e apos a setinha, o que e esperado na saida
    """ Isso explica o que a funcao faz """
    return "Voce digitou: " + str(num) + ", " + name

print(more_options(10,"Carlos"))
print(more_options(100,"Marta"))
print(more_options("10","Marta")) #Mas ele nao forca resultado... esses detalhes sao so de legenda mesmo


def is_even(num:int)->bool: #A funcao pode ter varios returns... Assim que voce atingi um deles, a funcao finaliza.
    """Recebe um valor numerico, se for impar recebe true, se for par recebe falso"""
    if (num%2)==0:
        return False
    else:
        return True

print(is_even(200))
print(is_even(201))