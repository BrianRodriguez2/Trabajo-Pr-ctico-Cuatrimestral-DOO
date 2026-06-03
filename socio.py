class Socio:
    _next_id = 0

    def __init__(self, nombre, dni):
        self.id = Socio._next_id
        self.nombre = nombre
        self.dni = dni
        Socio._next_id += 1

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, DNI: {self.dni}"