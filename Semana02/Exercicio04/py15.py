import csv #biblioteca para lidar com csv files



with open('names.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file) #objeto para leitura de csv
    
    with open('new_names.csv', 'w') as new_file: #abrindo outro arquivo no formato escrita
        fieldnames = ['first_name', 'last_name']
        csv_writer = csv.DictWriter(new_file, fieldnames= fieldnames, delimiter='\t') #criando objeto escritor dicionario que separa cada elemento (antes era por virgula) por tab
        
        csv_writer.writeheader() #objeto escritor
        
        for line in csv_reader: #iterando linhas no objeto csv_reader
            del line['email'] #excluindo valores de chave email do dicionario
            csv_writer.writerow(line) #escrever no arquivo as linhas do dicionario
