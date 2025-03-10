import pytest
from gst.gestion_gastos.gestor_gastos import GestorGastos


@pytest.fixture
def gestor():
    gestor = GestorGastos()  
    gestor.agregar_categoria("Salario")
    gestor.agregar_categoria("Inversión")
    gestor.agregar_categoria("Gastos pequeños")
    gestor.agregar_categoria("Comida")
    return gestor

def test_registrar_usuario(gestor):
    """Verifica que un usuario se registra correctamente."""
    gestor.registrar_usuario("Maria")
    assert "Maria" in gestor.obtener_usuarios()

def test_agregar_transaccion_ingreso(gestor):
    """Verifica que se puede agregar una transacción de ingreso."""
    gestor.registrar_usuario("Juan")
    gestor.agregar_transaccion("Juan", 200.0, "Salario", "Ingreso")
    assert gestor.obtener_balance("Juan") == 200.0

def test_agregar_transaccion_egreso(gestor):
    """Verifica que se puede agregar una transacción de egreso."""
    gestor.registrar_usuario("Ana")
    gestor.agregar_transaccion("Ana", 50.0, "Comida", "Egreso")
    assert gestor.obtener_balance("Ana") == -50.0


def test_transaccion_monto_maximo(gestor):
    """Verifica que se puede manejar una transacción con un monto muy grande."""
    gestor.registrar_usuario("Carlos")
    gestor.agregar_transaccion("Carlos", 1_000_000_000.0, "Inversión", "Ingreso")
    assert gestor.obtener_balance("Carlos") == 1_000_000_000.0

def test_multiples_transacciones_pequenas(gestor):
    """Verifica que se pueden manejar múltiples transacciones pequeñas."""
    gestor.registrar_usuario("Luis")
    for _ in range(100):  
        gestor.agregar_transaccion("Luis", 10.0, "Gastos pequeños", "Egreso")
    assert gestor.obtener_balance("Luis") == -1000.0  

def test_balance_cero_con_transacciones(gestor):
    """Verifica que el balance es cero si los ingresos y egresos se cancelan."""
    gestor.registrar_usuario("Pedro")
    gestor.agregar_transaccion("Pedro", 100.0, "Salario", "Ingreso")
    gestor.agregar_transaccion("Pedro", 100.0, "Comida", "Egreso")
    assert gestor.obtener_balance("Pedro") == 0.0


def test_transaccion_usuario_inexistente(gestor):
    """Verifica que no se puede agregar una transacción a un usuario no registrado."""
    with pytest.raises(ValueError, match="El usuario no está registrado"):
        gestor.agregar_transaccion("Pedro", 50.0, "Comida", "Egreso")

def test_transaccion_categoria_inexistente(gestor):
    """Verifica que no se puede agregar una transacción con una categoría no existente."""
    gestor.registrar_usuario("Maria")
    with pytest.raises(ValueError, match="La categoría no existe"):
        gestor.agregar_transaccion("Maria", 100.0, "Transporte", "Egreso")

def test_transaccion_monto_invalido(gestor):
    """Verifica que no se puede agregar una transacción con un monto inválido."""
    gestor.registrar_usuario("Juan")
    with pytest.raises(ValueError, match="El monto debe ser mayor a cero"):
        gestor.agregar_transaccion("Juan", -100.0, "Comida", "Egreso")