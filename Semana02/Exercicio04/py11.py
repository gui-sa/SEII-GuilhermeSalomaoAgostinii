
f = open('teste.txt','r') #abrindo o arquivo na forma de leitura padrao
#f = open('texte.txt','w') #abrindo o arquivo no formato escrita padrao (ele gera um novo se nao tiver, e sobrescreve se tiver)
#f = open('texte.txt','a') #abrindo o arquivo no formato escrita, porem sem sobrescreve-lo
#f = open('texte.txt','r+') #abrindo arquivo formato escrita e leitura.

print(f.name) #printa o nome do arquivo
print(f.mode) #printa o modo de leitura
f.close() #Se voce nao fecha o arquivo, isso caracteriza um memory leak

#Para evitar memory leak:
with open('teste.txt','r') as f: #quando voce sair do with, ele automaticamente fecha o arquivo e libera a memoria
    f_content = f.read() #le todo o conteudo do arquivo
    print(f_content)

print(f.name) #printa o nome do arquivo apesar do arquivo ja estar fechado
print(f.mode) #printa o modo de leitura apesar do arquivo ja estar fechado
#mas ele nao consegue acessa-lo mais....

print("\n\n\n")
with open('teste.txt','r') as f: #quando voce sair do with, ele automaticamente fecha o arquivo e libera a memoria
    f_content = f.readlines() #retorna lista onde cada linhas eh um elemento dela.
    print(f_content)

print("\n\n\n")
with open('teste.txt','r') as f: #quando voce sair do with, ele automaticamente fecha o arquivo e libera a memoria
    f_content = f.readline() #le a linha e coloca o ponteiro na proxima
    print(f_content, end="")
    f_content = f.readline() #le a linha e coloca o ponteiro na proxima
    print(f_content, end="")

print("\n\n\n")
with open('teste.txt','r') as f: #quando voce sair do with, ele automaticamente fecha o arquivo e libera a memoria
    for line in f: #itera as linhas do arquivo.. desta forma voce economiza memoria... lendo uma linha por vez.
        print(line, end="")

print("\n\n\n")
with open('teste.txt','r') as f: #quando voce sair do with, ele automaticamente fecha o arquivo e libera a memoria
    f_content = f.read(100) #le os primeiro 100 characteres.
    print(f_content, end = '---')
    #ele desloca o ponteiro na leitura de cada char.
    f_content = f.read(100) #le os primeiro 100 characteres.
    print(f_content, end = '----')
    #quando ele chega no fim, ele retornara uma string vazia


print("\n\n\n")
#Automatizando o trecho anterior.
with open('teste.txt','r') as f: #quando voce sair do with, ele automaticamente fecha o arquivo e libera a memoria
    size_to_read = 100
    f_content = f.read(size_to_read) #le os primeiro 100 characteres.
    while len(f_content) > 0:
        print(f_content, end = '')
        f_content = f.read(size_to_read) #le os primeiro 100 characteres.

print("\n\n\n")
with open('teste.txt','r') as f: #quando voce sair do with, ele automaticamente fecha o arquivo e libera a memoria
    f_content = f.read(10)
    print(f.tell()) #me mostra onde o ponteiro esta dentro do arquivo
    print(f_content)
    print("\n\n\n")
    f.seek(0) #colocamos o ponteiro na posicao zero.
    print(f_content)


#print("\n\n\n") #vai dar erro porque nao posso escrever em modo leitura.
#with open('teste.txt','r') as f: #quando voce sair do with, ele automaticamente fecha o arquivo e libera a memoria
#    f.write('YEAH')

print("\n\n\n")
with open('teste2.txt','w') as f: #Ele vai criar um arquivo de nome teste2.txt (criar ou sobrescrever)
    f.write("teste1") #ele escreve e anda com o ponteiro.
    f.write("teste2")


print("\n\n\n")
with open('teste2.txt','w') as f: #Ele vai criar um arquivo de nome teste2.txt (criar ou sobrescrever)
    f.write("teste1") #ele escreve e anda com o ponteiro.
    f.seek(0) 
    f.write("PA:") #ele reescreve ate onde o ponteiro for

#Para copiar teste em teste2:
print("\n\n\n")
with open('teste.txt','r') as rf: 
    with open('teste2.txt','w') as wf: 
        for line in rf:
            wf.write(line)

#Para copiar um arquivo aleatorio, como uma imagem...
with open('../../../../Wolf_HD.jpg','rb') as rf: #Ele vai ler o arquivo em binario
    with open('image_copy.jpg','wb') as wf:  #Ele vai escrever o arquivo em binario
        chunk_size = 4096 #define o tamanho do chunk em char
        rf_chunk = rf.read(chunk_size) #le o tamanho do chunk... o ponteiro vai se deslocar junto com a leitura
        while len(rf_chunk)>0: # rf_chunk recebera valores enquanto existir.
            wf.write(rf_chunk) #escreva o que eu li no novo arquivo
            rf_chunk = rf.read(chunk_size) #leia mais um chunk