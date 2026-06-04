from socio import Socio
from materiales import Libro, Revista
from biblioteca import Biblioteca

def main():
    biblioteca = Biblioteca()

    while True:
        print("\n=== MENÚ BIBLIOTECA ===")
        print("1. Agregar socio")
        print("2. Agregar libro")
        print("3. Agregar revista")
        print("4. Listar socios")
        print("5. Listar materiales")
        print("6. Prestar material")
        print("7. Devolver material")
        print("8. Salir")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            dni = input("DNI: ")
            socio = Socio(nombre, dni)
            biblioteca.agregar_socio(socio)

        elif opcion == "2":
            id = len(biblioteca.materiales) + 1
            titulo = input("Título: ")
            autor = input("Autor: ")
            editorial = input("Editorial: ")
            genero = input("Género: ")
            libro = Libro(id, titulo, autor, editorial, genero)
            biblioteca.agregar_material(libro)

        elif opcion == "3":
            id = len(biblioteca.materiales) + 1
            titulo = input("Título: ")
            autor = input("Autor: ")
            editorial = input("Editorial: ")
            numero = input("Número de edición: ")
            revista = Revista(id, titulo, autor, editorial, numero)
            biblioteca.agregar_material(revista)

        elif opcion == "4":
            biblioteca.listar_socios()

        elif opcion == "5":
            biblioteca.listar_materiales()

        elif opcion == "6":
            socio_id = int(input("ID del socio: "))
            material_id = int(input("ID del material: "))
            biblioteca.prestar_material(socio_id, material_id)

        elif opcion == "7":
            material_id = int(input("ID del material: "))
            biblioteca.devolver_material(material_id)

        elif opcion == "8":
            print("Saliendo...")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()