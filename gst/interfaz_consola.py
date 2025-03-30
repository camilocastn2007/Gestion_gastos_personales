
from gestion_gastos.gestor_gastos import GestorGastos

def mostrar_menu():
    """Muestra el menú de opciones en la consola."""
    print("\n-- Gestión de Gastos Personales ---")
    print("1. Registrar usuario")
    print("2. Agregar categoría")
    print("3. Agregar transacción")
    print("4. Consultar balance de usuario")
    print("5. Ver transacciones de usuario")
    print("6. Ver categorías")
    print("7. Salir")

def main():
    gestor = GestorGastos()
    usuario = None  

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            nombre_usuario = input("Ingrese el nombre del usuario: ").strip()
            if nombre_usuario:
                gestor.registrar_usuario(nombre_usuario)
                usuario = nombre_usuario
                print(f"Usuario '{nombre_usuario}' registrado")
            else:
                print(" El nombre del usuario no puede estar vacío.")

        elif opcion in ["2", "3", "4", "5"] and usuario is None:
            print(" Primero debe registrar un usuario antes de realizar esta operación.")

        elif opcion == "2":
            nombre_categoria = input("Ingrese el nombre de la categoría: ").strip()
            if nombre_categoria:
                gestor.agregar_categoria(nombre_categoria)
                print(f" Categoría '{nombre_categoria}' agregada con éxito.")
            else:
                print(" El nombre de la categoría no puede estar vacío.")

        elif opcion == "3":
            monto = input("Ingrese el monto: ").strip()
            categoria = input("Ingrese la categoría: ").strip()
            tipo = input("Ingrese el tipo (Ingreso/Egreso): ").strip().capitalize()

            if not monto.isdigit() or float(monto) <= 0:
                print(" El monto debe ser un número positivo.")
            elif tipo not in ["Ingreso", "Egreso"]:
                print(" El tipo de transacción debe ser 'Ingreso' o 'Egreso'.")
            else:
                gestor.agregar_transaccion(usuario, float(monto), categoria, tipo)
                print(f"Transacción de ${monto} como '{tipo}' en '{categoria}' agregada.")

        elif opcion == "4":
            balance = gestor.obtener_balance_usuario(usuario)
            print(f" Balance de {usuario}: ${balance:.2f}")

        elif opcion == "5":
            transacciones = gestor.obtener_transacciones_usuario(usuario)
            if transacciones:
                print(f"Transacciones de {usuario}:")
                for t in transacciones:
                    print(f"  - {t}")
            else:
                print(" No hay transacciones registradas.")

        elif opcion == "6":
            categorias = gestor.obtener_categorias()
            if categorias:
                print(" Categorías registradas:")
                for c in categorias:
                    print(f"  - {c}")
            else:
                print(" No hay categorías registradas.")

        elif opcion == "7":
            print(" Saliendo.")
            break

        else:
            print(" Opción no válida.")

if __name__ == "__main__":
    main()
