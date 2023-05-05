# script funcao2.py
valor = 20

def multiplica(valor, fator):
    valor = valor * fator
    return valor

def main():
    numero = int(input())
    print("Resultado", multiplica(valor, numero))
    print("Resultado", multiplica(valor, numero))

if __name__ == "__main__":
    main()

#########################################################
# script funcao3.py
# captando os valores do campo Input
valores = input() 
# separando os valores pelo espaço em branco e 
# transformando-os em uma lista de inteiros
valores = [int(i) for i in valores.split()]

def altera_lista(lista):
    lista[2] = lista[2] + 10
    return lista

def main():
    print("Nova lista", altera_lista(valores))
    print("Nova lista", altera_lista(valores))

if __name__ == "__main__":
    main()


############################################################################# 
# script funcao4.py
# captando os valores do campo Input
valores = input()
# separando os valores pelo espaço em branco e
# transformando-os em uma lista de inteiros
valores = [int(i) for i in valores.split()]

def altera_lista(lista):
    nova_lista = list(lista)
    nova_lista[2] = nova_lista[2] + 10
    return lista

def main():
        print("Nova lista", altera_lista(valores))
        print("Nova lista", altera_lista(valores))

if __name__ == "__main__":
        main()

#############################################################################

# script funcao5.py
def multiplicar_por(multiplicador):
    def multi(multiplicando):
        return multiplicando * multiplicador
    return multi

def main():
    multiplicar_por_10 = multiplicar_por(10)
    print(multiplicar_por_10(1))
    print(multiplicar_por_10(2))
 
    multiplicar_por_5 = multiplicar_por(5)
    print(multiplicar_por_5(1))
    print(multiplicar_por_5(2))

if __name__ == "__main__":
    main()

################################################################
# script anonima.py (versão alterada do script funcao5.py)
def multiplicar_por(multiplicador):
    return lambda multiplicando: multiplicando * multiplicador

def main():
    multiplicar_por_10 = multiplicar_por(10)
    print(multiplicar_por_10(1))
    print(multiplicar_por_10(2))
 
    multiplicar_por_5 = multiplicar_por(5)
    print(multiplicar_por_5(1))
    print(multiplicar_por_5(2))

if __name__ == "__main__":
    main()

