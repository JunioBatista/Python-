from account import Conta
from client import Cliente


cliente1 = Cliente(123 , 'joao' , 'Rua 1')
cliente2 = Cliente(345, 'Maria','Rua 2')

conta1 = Conta([cliente1,cliente2], 1,0) 
conta1.depositar(1500)
conta1.sacar(500)
#conta1.gerarsaldo()

conta1.extrato.extrato(conta1.numero)

#Sugestão: altere o programa do código anterior a fim de criar mais uma conta para dois clientes diferentes. Como desafio, tente, por meio do objeto conta, imprimir o nome e o endereço dos clientes associados às contas.
c_wedson = Cliente(12341, 'Wedson', 'rua das palmeiras')
c_joaquina = Cliente(12341, 'joaquina', 'rua das palmeiras')


conta_casal = Conta([c_wedson, c_joaquina], 2, 1000)

nome_homem = conta_casal.clientes[0].nome
nome_mulher = conta_casal.clientes[1].nome
print(f'Os titulares da conta são: {nome_homem} e {nome_mulher}')