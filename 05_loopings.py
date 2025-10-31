""" Trabalhando com loopings """

cidades = ['Sao Paulo', 'Recife', 'Dubai', 'Poa', 'Vitoria de Santo Antao', 'Goiana']

# Looping : FOR

for cidade in cidades :
    print(cidade)

palavra = "Vicente"
contador = 0
for letra in palavra:
    print(str(contador)+ ' - '+ letra)
    contador = contador + 1

    # Looping : WHILE

botaoExecutar = True
contador = 0

while botaoExecutar :
    print(contador)
    contador = contador + 1
    if contador >= 10 :
        botaoExecutar = False


