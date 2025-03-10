from datetime import datetime

class Transaccion:
    def __init__(self, monto: float, categoria: str, tipo: str):
        if monto <= 0:
            raise ValueError("El monto debe ser mayor a cero")
        if tipo not in ["Ingreso", "Egreso"]:
            raise ValueError("El tipo de transacción debe ser 'Ingreso' o 'Egreso'")

        self.__monto = monto
        self.__categoria = categoria
        self.__tipo = tipo
        self.__fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def get_monto(self) -> float:
        return self.__monto if self.__tipo == "Ingreso" else -self.__monto

    def get_categoria(self) -> str:
        return self.__categoria

    def get_tipo(self) -> str:
        return self.__tipo

    def get_fecha(self) -> str:
        return self.__fecha

    def __str__(self):
        return f"[{self.__fecha}] {self.__tipo}: ${self.__monto} - {self.__categoria}"
