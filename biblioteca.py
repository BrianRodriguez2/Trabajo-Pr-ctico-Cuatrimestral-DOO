class Biblioteca:
    def __init__(self):
        self.socios = []
        self.materiales = []
        self.prestamos = []

    # === SOCIOS ===
    def agregar_socio(self, socio):
        self.socios.append(socio)

    def mostrar_socios(self):
        if not self.socios:
            print("No hay socios registrados.")
        else:
            for socio in self.socios:
                print(f"Nombre: {socio.nombre}, DNI: {socio.dni}")

    def borrar_socio(self, dni):
        for socio in self.socios:
            if socio.dni == dni:
                self.socios.remove(socio)
                print(f"Socio con DNI {dni} eliminado correctamente.")
                return
        print(f"No se encontró un socio con DNI {dni}.")

    # === MATERIALES ===
    def agregar_material(self, material):
        self.materiales.append(material)

    def mostrar_materiales(self):
        if not self.materiales:
            print("No hay materiales registrados.")
        else:
            for material in self.materiales:
                print(material)

    # === PRÉSTAMOS ===
    def prestar_material(self, dni, id_material):
        socio = next((s for s in self.socios if s.dni == dni), None)
        material = next((m for m in self.materiales if m.id == id_material), None)

        if socio and material:
            if material.disponible:
                material.disponible = False
                self.prestamos.append((socio, material))
                print(f"Material '{material.titulo}' prestado a {socio.nombre}.")
            else:
                print("El material no está disponible.")
        else:
            print("Socio o material no encontrado.")

    def devolver_material(self, dni, id_material):
        for prestamo in self.prestamos:
            socio, material = prestamo
            if socio.dni == dni and material.id == id_material:
                material.disponible = True
                self.prestamos.remove(prestamo)
                print(f"Material '{material.titulo}' devuelto por {socio.nombre}.")
                return
        print("No se encontró el préstamo correspondiente.")
