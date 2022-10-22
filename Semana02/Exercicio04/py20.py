



try: #ele tenta rodar seu codigo... se nao rolar ele usa a excecao. Isso para esconder os erros zuados do usuario
#    with open('testee.txt','r') as f: #vai dar erro porque errei o nome do arquivo
#        pass
#    var = bad_var #Ele esconde esse tipo de erro tambem... E outros.
#    a = 10
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else: #Vai rodar se der certo. nao precisa existir... eh so para deixar mais especifico.
    print(a, "fluxo que segue meu chapa.")
finally: #Sempre roda kkkkk No erro ou no sucesso.
    print("Ele sempre roda.")