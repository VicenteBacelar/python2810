def divisao(a,b):
    try:
        resultado = a/b
        print(f"O Resultado de {a} por {b} é : {resultado}")
    except ZeroDivisionError :
        # Se houver um erro de divisao por zero o codigo dentro do except é executado
        print("Erro: Não é possível dividir por zero !!!")
    except TypeError :
        # Caso os parametros fornecidos nao sejam numeros
        print("Erro: Ambos os valores devem ser numeros. !!!")
    except Exception as erro:
        # Captura qualquer outro tipo de exceção que não tenha sido tratada nos anteriores
        print("Erro inesperado: {erro}")
    else:
        # é executado se o código detro do try for bem-sucedido (sem erros)
        print("Divisao foi realizada com sucesso")
    finally:
        # sempre é executado , independente de erro ou sucesso
        print("O processo de divisao for concluido")

        


    # Teste 01: Divisao Normal
    divisao(10,2)

    # Teste 02: Divisao por zero
    divisao(10,0)

    # Teste 03: Divisao por tipos invalidos
    divisao (10, "dois")


    # Teste 04: Divisao por erro inesperado
    divisao ("dez",2)
