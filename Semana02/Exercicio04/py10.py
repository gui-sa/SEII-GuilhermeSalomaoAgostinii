import os #modulo interno para lidar com sistema.

#print(dir(os)) #mostra todos os detalhes do modulo

print(os.getcwd()) #printa o caminho para a sua pasta pai por padrao

os.chdir('/home/salomao/Desktop') #troca o ponteiro da cwd para o caminho escrito
print(os.getcwd()) #mostra onde o ponteiro esta.

print(os.listdir()) #printa todos os arquivos e diretorio do cwd

os.makedirs('teste/teste') #cria diretorios no cwd
print(os.listdir())

os.rename("arq3", "arq_teste") #altera o nome de arquivos no cwd
print(os.listdir())

os.rename( "arq_teste", "arq3")
print(os.listdir())

os.removedirs('teste/teste') #remove os diretorios
print(os.listdir())

print(os.stat("arq3")) #Pega dados temporais sobre o arquivo.

#for dirpath, dirnames, filenames, in os.walk('/home/salomao/Desktop'): #Ele cria uma arvore de arquivos e diretorios de todos os locais
#    print('Current Path: ', dirpath)
#    print('Directories: ', dirnames)
#    print('Files:', filenames)

print(os.environ.get('HOME')) #pega o endereco da variavel de ambiente

file_path = os.environ.get('HOME') + '/test.txt'
print(file_path)

file_path = os.path.join(os.environ.get('HOME'), 'test.txt') #junta os diretorios para ti, gerando uma string.
print(file_path)

print(os.path.basename ('/home/salomao/Desktop/arq3')) # retorna somente o nome do arquivo no final da string.
print(os.path.split ('/home/salomao/Desktop/arq3')) # retorna uma lista com o nome do diretorio pai e do arquivo nele.
print(os.path.exists ('/home/asalomao/Desktop/arq3')) # checa se existe
print(os.path.isdir ('/home/salomao/Desktop/arq3')) # checa se e um diretorio
print(os.path.isfile ('/home/salomao/Desktop/arq3')) # checa se e um arquivo
print(os.path.splitext ('/home/salomao/Desktop/arq3.txt')) # te passa uma lista com o diretorio e a extensao do arquivo

