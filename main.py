from gst.gestion_gastos import GestorGastos

def main():
    sistema = GestorGastos()

    # Agregar categorías
    sistema.agregar_categoria("Alimentación")
    sistema.agregar_categoria("Transporte")
    sistema.agregar_categoria("Salud")

    # Registrar usuario
    sistema.registrar_usuario("Juan")

    # Agregar transacciones
    sistema.agregar_transaccion("Juan", 1500, "Alimentación", "Ingreso")
    sistema.agregar_transaccion("Juan", 500, "Transporte", "Egreso")

    # Mostrar balance
    balance = sistema.obtener_balance_usuario("Juan")
    print(f"Balance de Juan: ${balance}")

    # Mostrar transacciones
    transacciones = sistema.obtener_transacciones_usuario("Juan")
    for t in transacciones:
        print(t)

if __name__ == "__main__":
    main()
