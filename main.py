from biblioteca import Biblioteca
from socio import Socio
from materiales import Libro, Revista

def main():
    biblioteca = Biblioteca()

    while True:
        print("\n=== MENÚ BIBLIOTECA ===")
        print("1. Agregar socio")
        print("2. Agregar libro")
        print("3. Agregar revista")
        print("4. Listar socios")
        print("5. Borrar socio")
        print("6. Listar materiales")
        print("7. Prestar material")
        print("8. Devolver material")
        print("9. Salir")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            nombre = input("Nombre del socio: ").strip()
            dni = input("DNI del socio: ").strip()

            if not nombre or not dni:
                print("Error: el nombre y el DNI son obligatorios.")
            else:
                socio = Socio(nombre, dni)
                biblioteca.agregar_socio(socio)
                print(f"Socio {nombre} agregado correctamente.")
            input("\nPresioná Enter para volver al menú...")

        elif opcion == "2":
            id_libro = int(input("ID del libro: "))
            titulo = input("Título del libro: ")
            autor = input("Autor: ")
            editorial = input("Editorial: ")
            genero = input("Género: ")
            libro = Libro(id_libro, titulo, autor, editorial, genero)
            biblioteca.agregar_material(libro)
            print(f"Libro '{titulo}' agregado correctamente.")
            input("\nPresioná Enter para volver al menú...")

        elif opcion == "3":
            id_revista = int(input("ID de la revista: "))
            titulo = input("Título de la revista: ")
            editorial = input("Editorial: ")
            categoria = input("Categoría: ")
            revista = Revista(id_revista, titulo, editorial, categoria)
            biblioteca.agregar_material(revista)
            print(f"Revista '{titulo}' agregada correctamente.")
            input("\nPresioná Enter para volver al menú...")

        elif opcion == "4":
            print("\n=== Socios ===")
            biblioteca.mostrar_socios()
            input("\nPresioná Enter para volver al menú...")

        elif opcion == "5":
            dni = input("DNI del socio a borrar: ").strip()
            if not dni:
                print("Error: el DNI es obligatorio.")
            else:
                biblioteca.borrar_socio(dni)
            input("\nPresioná Enter para volver al menú...")

        elif opcion == "6":
            print("\n=== Materiales ===")
            biblioteca.mostrar_materiales()
            input("\nPresioná Enter para volver al menú...")

        elif opcion == "7":
            dni = input("DNI del socio: ").strip()
            id_material = int(input("ID del material: "))
            biblioteca.prestar_material(dni, id_material)
            input("\nPresioná Enter para volver al menú...")

        elif opcion == "8":
            dni = input("DNI del socio: ").strip()
            id_material = int(input("ID del material: "))
            biblioteca.devolver_material(dni, id_material)
            input("\nPresioná Enter para volver al menú...")

        elif opcion == "9":
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intentá de nuevo.")
            input("\nPresioná Enter para volver al menú...")

if __name__ == "__main__":
    main()
