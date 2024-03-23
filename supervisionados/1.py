def entrada_de_dados():
  coeficiente = quantidade = eval(input("digite o valor do coeficiente"))
  return coeficiente

def culc_delta(a,b,c):
  
  delta=b*b-4*a*c

  return(delta)  
  
import numpy as np
def calcular_raizes(a,b,c,delta):
  if (delta<0):
    resultado:'a equação nao possui raizes nos numeros reais'
  elif (delta==0):
    x=-b/(2*a)
    resultado:'a equação possui apenas a raiz: {x}'
  else:    
    x1=(-b-np.sqrt(delta))//(2*a)
    x2=(-b+np.sqrt(delta))//(2*a)
    resultado=f'a equação possue duas raizes: {x1},{x2}'
  return resultado  

#f(x)ax^2+bx+c

a=entrada_de_dados()
b=entrada_de_dados()
c=entrada_de_dados()

delta=culc_delta(a,b,c)

resultado=calcular_raizes(a,b,c,delta)
print(resultado )