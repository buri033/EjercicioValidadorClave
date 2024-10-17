# TODO: Implementa el código del ejercicio aquí
# validador.py
from abc import ABC, abstractmethod
from .errores import (
    NoCumpleLongitudMinimaError,
    NoTieneCaracterEspecialError,
    NoTieneLetraMayusculaError,
    NoTieneLetraMinusculaError,
    NoTieneNumeroError,
    NoTienePalabraSecretaError
)

class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada):
        self._longitud_esperada = longitud_esperada

    def _validar_longitud(self, clave):
        if len(clave) <= self._longitud_esperada:
            raise NoCumpleLongitudMinimaError(f"La clave debe tener una longitud de más de {self._longitud_esperada} caracteres")

    def _contiene_mayuscula(self, clave):
        if not any(c.isupper() for c in clave):
            raise NoTieneLetraMayusculaError("La clave debe contener al menos una letra mayúscula")

    def _contiene_minuscula(self, clave):
        if not any(c.islower() for c in clave):
            raise NoTieneLetraMinusculaError("La clave debe contener al menos una letra minúscula")

    def _contiene_numero(self, clave):
        if not any(c.isdigit() for c in clave):
            raise NoTieneNumeroError("La clave debe contener al menos un número")

    @abstractmethod
    def es_valida(self, clave):
        pass

