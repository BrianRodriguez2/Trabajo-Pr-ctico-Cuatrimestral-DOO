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
        print("6. Listar préstamos")
        print("7. Listar materiales")
        print("8. Prestar material")
        print("9. Devolver material")
        print("10. Salir")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            nombre = input("Nombre del socio: ")
            dni = input("DNI del socio: ")

            if not nombre:
                print("Error: el nombre no puede estar vacío.")
            elif not dni.isdigit():
                print("Error: el DNI debe ser numérico.")
            else:
                socio = Socio(nombre, dni)
                if biblioteca.agregar_socio(socio):
                 #si el socio se agregó correctamente, se muestra el mensaje de éxito
                 print(f"Socio {nombre} agregado correctamente.")
            input("\nPresioná Enter para volver al menú...")

        elif opcion == "2":
            id_libro_input = input("ID del libro: ")
            if not id_libro_input.isdigit():
                print("Error: el ID debe ser un número.")
                input("\nPresioná Enter para volver al menú...")
                continue
            id_libro = int(id_libro_input)

            titulo = input("Título del libro: ")
            autor = input("Autor: ")
            editorial = input("Editorial: ")
            genero = input("Género: ")

            libro = Libro(id_libro, titulo, autor, editorial, genero)
            if biblioteca.agregar_material(libro):
                print(f"Libro '{titulo}' agregado correctamente.")
            input("\nPresioná Enter para volver al menú...")

        elif opcion == "3":
            id_revista_input = input("ID de la revista: ")
            if not id_revista_input.isdigit():
                print("Error: el ID debe ser un número.")
                input("\nPresioná Enter para volver al menú...")
                continue
            id_revista = int(id_revista_input)

            titulo = input("Título de la revista: ")
            editorial = input("Editorial: ")
            categoria = input("Categoría: ")

            revista = Revista(id_revista, titulo, editorial, categoria)
            if biblioteca.agregar_material(revista): 
                print(f"Revista '{titulo}' agregada correctamente.")
            input("\nPresioná Enter para volver al menú...")

        elif opcion == "4":
            print("\n=== Socios ===")
            biblioteca.mostrar_socios()
            input("\nPresioná Enter para volver al menú...")

        elif opcion == "5":
            dni = input("DNI del socio a borrar: ")
            if not dni.isdigit():
                print("Error: el DNI debe ser numérico.")
            else:
                biblioteca.borrar_socio(dni)
            input("\nPresioná Enter para volver al menú...")

        elif opcion == "6":
            biblioteca.mostrar_prestamos()
            input("\nPresioná Enter para volver al menú...")

        elif opcion == "7":
            print("\n=== Materiales ===")
            biblioteca.mostrar_materiales()
            input("\nPresioná Enter para volver al menú...")

        elif opcion == "8":
            dni = input("DNI del socio: ")
            id_material_input = input("ID del material: ")
            if not dni.isdigit() or not id_material_input.isdigit():
                print("Error: DNI e ID deben ser numéricos.")
            else:
                id_material = int(id_material_input)
                biblioteca.prestar_material(dni, id_material)
            input("\nPresioná Enter para volver al menú...")

        elif opcion == "9":
            dni = input("DNI del socio: ")
            id_material_input = input("ID del material: ")
            if not dni.isdigit() or not id_material_input.isdigit():
                print("Error: DNI e ID deben ser numéricos.")
            else:
                id_material = int(id_material_input)
                biblioteca.devolver_material(dni, id_material)
            input("\nPresioná Enter para volver al menú...")

        elif opcion == "10":
            print("Hasta luego.")
            break

        else:
            print("Opción inválida. Intentá de nuevo.")
            input("\nPresioná Enter para volver al menú...")

if __name__ == "__main__":
    main()
