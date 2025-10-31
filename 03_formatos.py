""" Detalhando strings e usando formato """

nomeCompleto = "Vicente Bacelar"
inicio = 5
fim = 11
print (nomeCompleto[5:11])
print (nomeCompleto[inicio:fim])

# Entendendo o campo Input

nome = input("Qual o seu nome ?: ")
sobrenome = input("Informe seu sobrenome: ")
print("Seu nome completo é: "+ nome + " " + sobrenome)


# Calculadora primitiva =)
# o comando input sempre vai gerar em string
valor1 = int(input("Qual o valor 1 ?"))
valor2 = int(input("Qual o valor 2 ?"))
# ou assim : valor = int(valor)
soma   = valor1 + valor2
print (soma)
