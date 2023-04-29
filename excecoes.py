num = eval(input("Entre com um número inteiro: "))

#se num não for valido, entra no except
try:
    num = eval(input("Entre com um número inteiro: \n"))
    print(num)
except:
    print("Entre com o valor numérico e não letras")


#except caso a exceção levantada seja de determinado tipo
try:
    num = eval(input("Entre com um número inteiro: \n"))
    print(num)
except NameError:
    print("Entre com o valor numérico e não letras")



#except para multiplos tipos de erro.
try:
    num = eval(input("Entre com um número inteiro: \n"))
    print(num)
except ValueError:
    print("Mensagem 1")
except IndexError:
    print("Mensagem 2")
except:
    print("Mensagem 3")


#geral sobre o uso de try/else
try:
    #Bloco 1
except Exception1:
    #Bloco tratador para Exception1 
except Exception2:
    #Bloco tratador para Exception1
    ...
else:
    #Bloco 2 – executado caso nenhuma exceção seja levantada
finally:
    #Bloco 3 – executado independente do que ocorrer
    #Instrução fora do try/except