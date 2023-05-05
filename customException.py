#declaração da istancia customizada de Exception
class ExcecaoCustomizada(Exception): 
    pass
    

#throw
def throws():
    raise ExcecaoCustomizada
    try: 
        throws()
    except ExcecaoCustomizada as ex:
        print ("Excecao lançada")


#Ao final da execução, será impressa a “Exceção lançada” pela captura da exceção, a qual, por sua vez, é lançada pelo método throws().