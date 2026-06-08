class Socio:
    _next_id = 0

    def __init__(self, nombre, dni):
        #valida el nombre
        if nombre == "" or nombre is None:
            print("Error: el nombre del socio no puede estar vacío. Ingrese un nombre válido.")
            return

        self.id = Socio._next_id
        self.nombre = nombre
        self.dni = dni
        Socio._next_id += 1

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, DNI: {self.dni}"
