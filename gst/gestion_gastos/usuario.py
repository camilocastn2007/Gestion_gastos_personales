from  gst.gestion_gastos.transaccion import Transaccion

class Usuario:
    def __init__(self, nombre: str):
        if not nombre.strip():
            raise ValueError("El nombre del usuario no puede estar vacío")
        
        self.__nombre = nombre
        self.__transacciones = []

    def get_nombre(self) -> str:
        return self.__nombre

    def agregar_transaccion(self, monto: float, categoria: str, tipo: str):
        nueva_transaccion = Transaccion(monto, categoria, tipo)
        self.__transacciones.append(nueva_transaccion)

    def obtener_balance(self) -> float:
        return sum(t.get_monto() for t in self.__transacciones)

    def obtener_transacciones(self):
        return self.__transacciones

    def __str__(self):
        return f"Usuario: {self.__nombre}, Balance: ${self.obtener_balance()}"
