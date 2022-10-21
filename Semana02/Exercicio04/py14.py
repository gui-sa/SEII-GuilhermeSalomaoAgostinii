import os #queremos manipular arquivos... precisaremos do auxilio do modulo do sistema operacional


os.chdir('/home/salomao/Desktop/Teste') #movemos o ponteiro para a pasta onde tem os arquivos

num = 0

for f in os.listdir(): #f assumira o nome de cada arquivo no diretorio, em cada iteracao
    file_name, file_ext = os.path.splitext(f) #a saida da funcao splittext e um tupla onde o primeiro elemento e o path com o arquivo e o segundo eh a extensao
    #print(file_name)
    new_name = file_name.replace(file_name.split('/')[-1], str(num)) #pegamos somente o nome no final do caminho, e trocamos ele pela string do numero desejado
    os.rename(file_name + file_ext, new_name + file_ext) #por fim, renomeamos o antigo para o novo mantendo a extensao
    num += 1 



