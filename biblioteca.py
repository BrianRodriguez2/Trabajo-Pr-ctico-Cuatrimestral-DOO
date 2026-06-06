from socio import Socio
from materiales import Libro, Revista

class Biblioteca:
    def __init__(self):
        self.materiales = []
        self.socios = []
        self.prestamos = {}

    def agregar_material(self, material):
        self.materiales.append(material)

    def agregar_socio(self, socio):
        self.socios.append(socio)

    def listar_materiales(self):
        for m in self.materiales:
            print(m)

    def listar_socios(self):
        for s in self.socios:
            print(s)



    def prestar_material(self, socio_id, material_id):
        socio = next((s for s in self.socios if s.id == socio_id), None)
        material = next((m for m in self.materiales if m.id == material_id), None)
        if socio and material and material.estado == "Disponible":
            material.estado = "Prestado"
            self.prestamos[material.id] = socio.id
            print(f"Material {material.titulo} prestado a {socio.nombre}")
        else:
            print("No se pudo realizar el préstamo.")

    def devolver_material(self, material_id):
        material = next((m for m in self.materiales if m.id == material_id), None)
        if material and material.estado == "Prestado":
            material.estado = "Disponible"
            self.prestamos.pop(material.id, None)
            print(f"Material {material.titulo} devuelto.")
        else:
            print("No se pudo realizar la devolución.")