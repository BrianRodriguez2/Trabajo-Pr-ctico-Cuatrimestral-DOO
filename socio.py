class Socio:
    def __init__(self, nombre, dni):
        if not nombre:
            print("Error: el nombre no puede estar vacío")
            self.nombre = None
        else:
            self.nombre = nombre

        if not dni or not dni.isdigit():
            print("Error: el DNI debe ser un número válido")
            self.dni = None
        else:
            self.dni = dni

    def __str__(self):
        if self.nombre:
            if self.dni:
                return f"{self.nombre} (DNI: {self.dni})"
        return "Socio inválido"
