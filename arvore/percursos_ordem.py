# raiz -> esquerda -> direita.
def VisitaPreOrdem(raiz):
   if (raiz):
      print(raiz.chave)
      VisitaPreOrdem(raiz.esquerda)
      VisitaPreOrdem(raiz.direita)



# esquerda -> raiz -> direita
def VisitaInOrdem(raiz):
   if (raiz):
      VisitaInOrdem(raiz.esquerda)
      print(raiz.chave)
      VisitaInOrdem(raiz.direita)



# esquerda -> direita -> raiz
def VisitaPosOrdem(raiz):
   if (raiz):
      VisitaPosOrdem(raiz.esquerda)
      VisitaPosOrdem(raiz.direita)
      print(raiz.chave) 