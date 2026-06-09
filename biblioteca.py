class Biblioteca:
    def __init__(self):
        self.socios = []
        self.materiales = []
        self.prestamos = []

    # === SOCIOS ===
    def agregar_socio(self, socio):
        #es para verificar si se repite el DNI, si se repite no se agrega el socio y se muestra un mensaje de error
        for s in self.socios:
            if s.dni == socio.dni:
                print(f"Error: ya existe un socio con DNI {socio.dni}.")
                return
        self.socios.append(socio)
        print(f"Socio '{socio.nombre}' agregado correctamente.")

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
        for m in self.materiales:
            if m.id == material.id:
                print(f"Error: ya existe un material con ID {material.id}.")
                return False # Retorna False si no se pudo agregar el material por ID duplicado
        self.materiales.append(material)
        return True # Retorna True si el material se agregó correctamente

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

    def mostrar_prestamos(self):
        if not self.prestamos:
            print("No hay préstamos registrados.")
        else:
            print("=== Préstamos activos ===")
            for socio, material in self.prestamos:
                print(f"Socio: {socio.nombre} (DNI: {socio.dni}) - Material: {material.titulo} (ID: {material.id})")


