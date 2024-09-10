class Tarea:
    def __init__(self,informacion,tareaspendientes):
        self.informacion=informacion
        self.tareaspendientes=tareaspendientes
    
    def __str__(self):
        return(f"{self.informacion} de las tareas pendientes {self.tareaspendientes}")
    
    def __len__(self):
        return len(self.tareaspendientes)
# Crear una instancia de Tarea
mi_tarea = Tarea("Revisión de código", ["Fix bugs"])

# Imprimir la representación en cadena de la tarea
print(mi_tarea)  # Salida: Revisión de código de las tareas pendientes: ['Fix bugs', 'Write tests', 'Update documentation']

# Obtener la cantidad de tareas pendientes
print(len(mi_tarea))  

    