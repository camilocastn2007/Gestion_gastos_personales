from .transaccion import Transaccion

class Usuario:
    def __init__(self, nombre: str):
        if not nombre.strip():
            raise ValueError("El nombre del usuario no puede estar vacío")
        
        self.__nombre = nombre
        self.__transacciones = []

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre: str):
        if not nuevo_nombre.strip():
            raise ValueError("El nombre del usuario no puede estar vacío")
        self.__nombre = nuevo_nombre

    @property
    def transacciones(self):
        return self.__transacciones

    def agregar_transaccion(self, monto: float, categoria: str, tipo: str):
        nueva_transaccion = Transaccion(monto, categoria, tipo)
        self.__transacciones.append(nueva_transaccion)

    @property
    def balance(self) -> float:
        return sum(t.monto for t in self.__transacciones)

    def __str__(self):
        return f"Usuario: {self.__nombre}, Balance: ${self.balance}"
