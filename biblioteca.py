class Biblioteca:
    def __init__(self):
        self.socios = []
        self.materiales = []
        self.prestamos = []      # lista prestamos
        self.devoluciones = []   # lista devoluciones

    def agregar_socio(self, socio):
        self.socios.append(socio)

    def agregar_material(self, material):
        self.materiales.append(material)

    def mostrar_socios(self):
        print("=== Socios ===")
        for s in self.socios:
            print(s)

    def mostrar_materiales(self):
        print("=== Materiales ===")
        for m in self.materiales:
            print(m)

    def prestar_material(self, socio_id, material_id):
        socio = next((s for s in self.socios if s.id == socio_id), None)
        material = next((m for m in self.materiales if m.id == material_id), None)

        if socio is None or material is None:
            print("Error: socio o material no encontrado.")
            return

        if material.estado == "Prestado":
            print("Error: el material ya está prestado.")
            return

        material.estado = "Prestado"
        self.prestamos.append(f"Socio {socio.nombre} prestó {material.titulo}")
        print(f"Material {material.titulo} prestado a {socio.nombre}.")

    def devolver_material(self, socio_id, material_id):
        socio = next((s for s in self.socios if s.id == socio_id), None)
        material = next((m for m in self.materiales if m.id == material_id), None)

        if socio is None or material is None:
            print("Error: socio o material no encontrado.")
            return

        if material.estado == "Disponible":
            print("Error: el material ya está disponible, no se puede devolver.")
            return

        material.estado = "Disponible"
        self.devoluciones.append(f"Socio {socio.nombre} devolvió {material.titulo}")
        print(f"Material {material.titulo} devuelto por {socio.nombre}.")

    def mostrar_prestamos(self):
        print("=== Registro de préstamos ===")
        for p in self.prestamos:
            print(p)

    def mostrar_devoluciones(self):
        print("=== Registro de devoluciones ===")
        for d in self.devoluciones:
            print(d)
