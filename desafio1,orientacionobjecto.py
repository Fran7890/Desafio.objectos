import random 

class Dado:
    def __init__(self,caras=6):
        self.caras=caras
                  
    def lanzar(self):
        return random.randint(1, self.caras)
dado = Dado()
resultado = dado.lanzar()
print (f"Resultado del lanzamiento {resultado }")