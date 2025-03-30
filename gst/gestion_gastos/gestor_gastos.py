from .usuario import Usuario
from .categoria import Categoria

class GestorGastos:
    """
        Representa el gestor de gastos de las transacciones.

    """
    def __init__(self):
        """
        inicializa una instancia del gestor de gastos.

        Args:
            usuarios(dict): Los usuarios.
            categorias(list): las categorias de los usuarios.
        """


        self.__usuarios = {}
        self.__categorias = []

    def registrar_usuario(self, nombre: str):
        """
        Agrega un nuevo usuario|
        
        """
        if nombre not in self.__usuarios:
            self.__usuarios[nombre] = Usuario(nombre)
        

    def obtener_usuarios(self):
        return list(self.__usuarios.keys())

    def agregar_categoria(self, nombre: str):
        if nombre not in [c.get_nombre() for c in self.__categorias]:
            self.__categorias.append(Categoria(nombre))

    def agregar_transaccion(self, usuario: str, monto: float, categoria: str, tipo: str):
        if usuario not in self.__usuarios:
            raise ValueError("El usuario no está registrado")

        if categoria not in [c.get_nombre() for c in self.__categorias]:
            raise ValueError("La categoría no existe")

        if monto <= 0:
            raise ValueError("El monto debe ser mayor a cero")

        self.__usuarios[usuario].agregar_transaccion(monto, categoria, tipo)

    def obtener_balance(self, usuario: str) -> float:
        usuario_obj = self.__usuarios.get(usuario)
        
        if usuario_obj is None:
            raise ValueError(f"El usuario '{usuario}' no está registrado")

        balance = sum(transaccion.get_monto() for transaccion in usuario_obj.obtener_transacciones())
        return balance
