#some todos os números pares da lista.
numeros = [10,2,7,5,3,6]
soma_dos_pares= 0

for i in numeros:
    if (i%2)==0:
        soma_dos_pares +=i 
    
print(soma_dos_pares)

while True:
    palavra = input('Entre com uma palavra: \n')
    if palavra == 'sair':
        break
print('Você digitou sair e agora está fora do laço')


#break interrompe o laço.
#continue, interrompe a iteração ATUAL(somente) de um laço for ou while. EX:
for num in range(1, 11):
    if num == 5:
        continue
    else:
        print(num)
print('Laço encerrado')

s = 0
for i in range(5):
    s += 3*i
print(s)

0
s = 0 +3*0