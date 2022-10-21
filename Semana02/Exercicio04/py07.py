nums = [1,2,3,4,5]

for num in nums: #num vai assumir a cada iteracao um dos valores do nums
    print(num)


for num in nums: #num vai assumir a cada iteracao quando num valor 3, ele vai sair do primeiro loop.
    if num == 3:
        print("Found!")
        break
    print(num)




for num in nums: #num vai assumir a cada iteracao quando ele encontrar num=3 ele vai finalizar essa unidade de iteracao e ir para a proxima.
    if num == 3:
        print("Found!")
        continue
    print(num)




for num in nums: #num vai assumir a cada iteracao um dos valores do nums
    for letter in 'abc': #Para cada valor de num iterado, letter vai assumir todos os valores da string passada.
        print(num, letter)



for i in range(10): #comeca do zero e vai ate o 10, 10 nao incluso.
    print(i)



for i in range(1,11): #comeca do um e vai ate o 11, 11 nao incluso.
    print(i)




x= 0
while x < 10: #vai iterar enquanto x for menor que 10
    print(x)
    x += 1 


x= 0
while x < 10: #vai iterar enquanto x for menor que 10
    if x==5: # quando x for 5, ele sai do ultimo loop
        break
    print(x)
    x += 1 


x= 0
while x < 10: #vai iterar enquanto x for menor que 10
    if x==5: # quando x for 5, ele termina essa unidade de iteracao e comeca de novo no while.
        print("Aqui ele fez outra coisa")
        x += 1 
        continue
    print(x)
    x += 1 


#cuidado com loops que nunca finalizam!
