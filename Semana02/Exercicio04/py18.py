
#Local: dentro  da funcao
#Enclosing: funcos de fora de funcoes
#Global:  variaveis que ficam no corpo do codigo.
#Built-in : ja vem por padrao.. Se voce usa-las pode dar erro, ou, voce pode perder uma builtin




x = 'global x' #global porque esta no corpo geral

def test():
    y = 'local y'
    print(y)
    print(x) #local access global scoped variables

test()
#print(y) #Error, y nao existe no global

def test2():
    x = 'local x'
    print(x) #dentro da funcao o x eh sobrescrito

test2()
print(x) #fora ele assume os valores que tinha antes.


def test3():
    global x #estamos dizendo que o x daqui eh o global
    x = 'local x'
    print(x) #dentro da funcao o x eh sobrescrito
test3()
print(x) #fora ele assume os valores que tinha antes.

x = 'global x'

def test4(z): #local
    print(z)

test4('local z')
#print(z) #error porque eh local.

m = min([5,1,4,2,3]) #min is a built in functions
print(m)

import builtins
#print(dir(builtins)) #printa todas as builtins

def min():
    print(m)


min() #voce acabou de quebrar uma builtin


def outer():
    x = 'outer_x' #enclosed variables, que eh local para a global.
    def inner(): #uma funcao que fica dentro da funcao.
        x = 'inner_x' #local scoped
        print(x)
    inner()
    print(x)

outer()

x = 'global_x'
def outer2():
    x = 'outer_x' #enclosed variables, que eh local para a global.
    def inner(): #uma funcao que fica dentro da funcao.
        nonlocal x #voce esta dizendo que ela eh global no contexto da variavel de tras!
        x = 'inner_x' #local scoped
        print(x)
    inner()
    print(x)

outer2()
print(x)

# Se voce dizer que a var da func da func nao e local, e a var da fun outer eh global, o python buga kkkkkk
#x = 'global_x'
#def outer3():
#    global x
#    x = 'outer_x' #enclosed variables, que eh local para a global.
#    def inner(): #uma funcao que fica dentro da funcao.
#        nonlocal x #voce esta dizendo que ela eh global no contexto da variavel de tras!
#        x = 'inner_x' #local scoped
#        print(x)
#    inner()
#    print(x)
#
#outer3()
#print(x)

