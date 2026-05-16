from abc import ABC, abstractmethod

class Material():
    def __init__(self,titulo,autor,editorial):
        self.titulo = titulo
        self.editorial = editorial
        self.autor = autor
        self.disponible = True

    def __str__(self):
        return f"Titulo: {self.titulo}, Editorial: {self.editorial}, Autor: {self.autor}"
    

class Libro(Material):
    def __init__(self,titulo, autor, editorial, genero,id):
        super().__init__(titulo, autor, editorial)
        self.genero = genero
        self.id = id

class Revistas(Material):
    def __init__(self,titulo, autor, editorial,numero):
        super().__init__(titulo, autor, editorial)
        self.numero = numero

print(Revistas)