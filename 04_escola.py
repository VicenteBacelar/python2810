""" Escola Nota Dez """

nomeAluno = input("Qual o nome do aluno ?")
mediaAluno = int(input("Qual a média do "+ nomeAluno + "?: "))
tipoEscola = input("Em que escola o "+nomeAluno + " estuda \n[1] Publico\n[2] Particular\n")
freqAluno = int(input("Qual a frequencia do aluno " + nomeAluno +  "?:")) 
''' Diferentes tipos de testes 
!= diferente
== igual
<= menor ou igual
>= maior ou igual
> maior
< menor
'''


if tipoEscola == "2" :
    print("-----------Escola Particular-----------")
    if mediaAluno >= 7 and freqAluno >= 70:
        print("Aprovado")
    else :
        print("Reprovado")
if tipoEscola == "1" :
    print("-----------Escola Publica-------------")
    if mediaAluno >= 7 or freqAluno >= 70 :
        print("Aprovado")
    else :
        print("Reprovado")
print("------------- Fim do Boletim-------")
