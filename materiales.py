from abc import ABC

class Material(ABC):
    def __init__(self, id, titulo, autor, editorial, estado="Disponible"):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.estado = estado

    def __str__(self):
        return f"ID: {self.id}, Título: {self.titulo}, Autor: {self.autor}, Editorial: {self.editorial}, Estado: {self.estado}"

class Libro(Material):
    def __init__(self, id, titulo, autor, editorial, genero, estado="Disponible"):
        super().__init__(id, titulo, autor, editorial, estado)
        self.genero = genero

class Revista(Material):
    def __init__(self, id, titulo, autor, editorial, numero, estado="Disponible"):
        super().__init__(id, titulo, autor, editorial, estado)
        self.numero = numero