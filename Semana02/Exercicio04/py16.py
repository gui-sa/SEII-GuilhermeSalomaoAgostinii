import csv #importando modulo para csv

html_output = '' #html output string starting empty
names = [] #

with open('patrons.csv', 'r') as data_file:
    csv_data = csv.DictReader(data_file) #criando objeto para leitura do arquivo patrons.csv

    next(csv_data) #Retorna a primeira linha da csv_data -- nesse caso ele vai mover o ponteiro do arquivo para fora dela

    for line in csv_data: #iterando line pelo restante das linhas no arquivo:
        if line['FirstName'] == 'No Reward': #Se o valor for 'no reward', finaliza a iteracao.. Para sair da parte sem informacao util.
            break
        names.append(f"{line['FirstName']} {line['LastName']}") #Unindo o primeiro e ultimo nome em uma mesma string e salvando na lista names

html_output += f'<p>There are currently {len(names)} public contributors. Thank You!</p>' #concatena na variavel que esta armazenando a string usando F-Strings (permite colocar objetos e funcoes dentro de strings).

html_output += '\n<ul>' #colocando tag ul -- lista sem ordenamento

for name in names:
    html_output += f'\n\t<li>{name}</li>' #repete o elemento li colocando os nomes ate finalizar.

html_output += '\n</ul>' #fecha a tag ul

print(html_output) #printa essa variavel ja formatada em html_output.