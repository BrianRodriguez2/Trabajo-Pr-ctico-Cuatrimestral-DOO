class Material:
    def __init__(self, id, titulo):
        self.id = id
        self.titulo = titulo
        self.disponible = True

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"ID: {self.id}, Título: {self.titulo}, Estado: {estado}"


class Libro(Material):
    def __init__(self, id, titulo, autor, editorial, genero):
        super().__init__(id, titulo)
        self.autor = autor
        self.editorial = editorial
        self.genero = genero

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"[Libro] ID: {self.id}, Título: {self.titulo}, Autor: {self.autor}, Editorial: {self.editorial}, Género: {self.genero}, Estado: {estado}"


class Revista(Material):
    def __init__(self, id, titulo, editorial, categoria):
        super().__init__(id, titulo)
        self.editorial = editorial
        self.categoria = categoria

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"[Revista] ID: {self.id}, Título: {self.titulo}, Editorial: {self.editorial}, Categoría: {self.categoria}, Estado: {estado}"
