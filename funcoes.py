escolha = input("Escolha uma opção de função: 1 ou 2\n")
if escolha == "1":
    def func1(x):
        return x + 1
    s = func1(10)

else:
    def func2(x):
        return x + 2
    s = func2(10)

print(s)

#multiplicador com valor padrao
def taximetro(distancia, multiplicador=1):
    largada = 3
    km_rodado = 2
    valor = (largada + distancia * 
    km_rodado) * multiplicador
    return valor


pagamento = taximetro(3.5)
print(pagamento)

#----------------------------------------------------------------
def func1(x):
    x = 10
    print(f'Função func1 - x = {x}')


def func2(x):
    x = 20
    print(f'Função func2 - x = {x}')

x = 0
func1(x)
func2(x)
print(f'Programa principal - x = {x}')

#RECURSIVIDADE
def regressiva(x):
    if x <= 0:
        print("Acabou")
    else:
        print(x)
        regressiva(x-1)


#fatorial COM recursividade
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*fatorial(n-1)
    
#fatorial SEM recursividade
def fatorial(n):
    fat = 1
    if n == 0 or n == 1:
        return fat
    else:
        for x in range(2, n + 1):
                fat = fat*x
        return fat

#Fibonacci 
def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)