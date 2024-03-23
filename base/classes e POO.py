class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo

        def depositar(self, valor):
            self.saldo += valor

        def sacar(self, valor):
            if self.saldo < valor:
                return False
            else:
                self.saldo -= valor
                return True

        def gerar_extrato(self):
            print(f"numero: {self.numero} \n cpf: {self.cpf}\nsaldo: {self.saldo}")     

        def transfereValor(self,contaDestino,valor):
            if self.saldo < valor:
                return ("Não existe saldo suficiente")
            else:
                contaDestino.depositar(valor)
                self.saldo -= valor
                return("Transferencia Realizada") 

def main():
    c1 = Conta(1,1,"Joao",0)
    c1.depositar(300)
    saque = c1.sacar(400)
    c1.gerar_extrato()
    print(f"O saque foi realizado? {saque}")


# Quando um script python é executado, a variável reservada
# NAME referente a ele tem valor igual a "__main__".
# Nesse caso, a condição do IF a seguir será TRUE.
# Então o que está no corpo do IF será executado. No caso,
# é um chamado ao método main do script
if __name__ == "__main__": 
    main()

################################################################################

#NÂO é obrigatório um construtor na classe, só quando precisa inserir valores de atributos do obj.
class A():
    def f(self):
        print("foo")


def main():
    obj_A = A() # Objeto sendo instanciado
    obj_A.f()

if __name__ == "__main__": 
    main()

################################################################################

class Circulo:
    _total_circulos = 0

    def __init__(self,pontox, pontoy, raio):
        self.pontox = pontox
        self.pontoy = pontoy
        self.raio = raio
        type(self)._total_circulos +=1

    @classmethod
    def get_total_circulos(cls): 
        return cls._total_circulos
    
    def __gerarsaldo(self):
        print(f"numero: {self.numero}\n saldo:{self.saldo}")

circ1 = Circulo(1,1,10)
circ1._total_circulos

Circulo.total_circulos

