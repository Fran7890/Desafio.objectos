class Cartas:
    def __init__(self,palo,valor):
        self.palo = palo
        self.valor = valor  
    
    def get_mostrar(self):
        return self.palo
    
    def __str__(self):
        return (f"el palo de la carta es{self.palo} y el valor es: {self.valor}")
    
if __name__ == "__main__":  
    carta1 = Cartas("Espada", "5")

print(carta1.get_mostrar()) 
print(carta1 )   