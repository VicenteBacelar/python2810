""" Hora do Exercicio """
# perguntar o ano em que o usuario nasceu
# perguntar o ano em que estamos
# informar a idade

''' Bonus Lógico '''
# Perguntar para o usuario se ele deseja testar novamente
# caso sim refazer o teste
# caso nao fim do programa

# programa desafio
executar = True
while executar:
    nascimento = input('Qual ano nascimento ? ')
    anoAtual = input('Qual o ano atual ? ')
    idade = int(anoAtual) - int(nascimento)
    print(idade)
    print ('Voce tem '+str(idade) + ' anos.')

    opcao = input("\nDeseja testar novamente \nSim ou Nao? ")
    if opcao == "Nao" :
        executar = False

    

