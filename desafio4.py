class Contacto:
    def __init__(self, nombre, telefono, email=None):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return f"Nombre: {self.nombre}, Teléfono: {self.telefono}, Email: {self.email if self.email else 'No disponible'}"
    
    def __setitem__(self, key, value):
        if key == 'telefono':
            self.telefono = value
        elif key == 'email':
            self.email = value
        else:
            raise KeyError(f"El atributo '{key}' no se puede modificar.")
    
# Ejemplo de uso
if __name__ == "__main__":
    contacto1 = Contacto("Franco", "3516006677", "franco@example.com")
    print(contacto1)  # Imprime los detalles del contacto

    # Modificar el número de teléfono usando la sintaxis de diccionario
    contacto1['telefono'] = "3517008899"
    print(contacto1)  # Imprime los detalles actualizados

    # Modificar el email
    contacto1['email'] = "nuevoemail@example.com"
    print(contacto1)  # Imprime los detalles actualizados
