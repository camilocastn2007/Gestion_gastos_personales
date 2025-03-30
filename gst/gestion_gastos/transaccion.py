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

    @property
    def monto(self) -> float:
        return self.__monto if self.__tipo == "Ingreso" else -self.__monto

    @property
    def categoria(self) -> str:
        return self.__categoria

    @property
    def tipo(self) -> str:
        return self.__tipo

    @property
    def fecha(self) -> str:
        return self.__fecha

    def __str__(self):
        return f"[{self.fecha}] {self.tipo}: ${self.monto} - {self.categoria}"
