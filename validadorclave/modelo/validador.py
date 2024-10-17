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
    def __init__(self, longitud_esperada: int):
        self._longitud_esperada = longitud_esperada

    def _validar_longitud(self, clave: str):
        if len(clave) <= self._longitud_esperada:
            raise NoCumpleLongitudMinimaError(
                f"La clave debe tener una longitud de más de {self._longitud_esperada} caracteres")

    def _contiene_mayuscula(self, clave: str):
        if not any(c.isupper() for c in clave):
            raise NoTieneLetraMayusculaError("La clave debe contener al menos una letra mayúscula")

    def _contiene_minuscula(self, clave: str):
        if not any(c.islower() for c in clave):
            raise NoTieneLetraMinusculaError("La clave debe contener al menos una letra minúscula")

    def _contiene_numero(self, clave: str):
        if not any(c.isdigit() for c in clave):
            raise NoTieneNumeroError("La clave debe contener al menos un número")

    @abstractmethod
    def es_valida(self, clave):
        pass


class ReglaValidacionGanimedes(ReglaValidacion):
    def __init__(self):
        super().__init__(8)

    def contiene_caracter_especial(self, clave: str):
        caracteres_especiales = '@_#$%'
        if not any(c in caracteres_especiales for c in clave):
            raise NoTieneCaracterEspecialError(
                "La clave debe contener al menos uno de los caracteres especiales @, _, #, $ o %")

    def es_valida(self, clave):
        self._validar_longitud(clave)
        self._contiene_mayuscula(clave)
        self._contiene_minuscula(clave)
        self._contiene_numero(clave)
        self.contiene_caracter_especial(clave)
        return True
