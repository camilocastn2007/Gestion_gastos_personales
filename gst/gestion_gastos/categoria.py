class Categoria:
    def __init__(self, nombre: str):
        if not nombre.strip():
            raise ValueError("El nombre de la categoría no puede estar vacío")
        self.__nombre = nombre

    @property
    def nombre(self) -> str:
        return self.__nombre

    def __str__(self):
        return self.nombre
