# TODO: Implementa el código del ejercicio aquí

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
            return False
        if len(clave) >= self._longitud_esperada:
            return True

    def _contiene_mayuscula(self, clave: str):
        return any(c.isupper() for c in clave)

    def _contiene_minuscula(self, clave: str):
        return any(c.islower() for c in clave)


    def _contiene_numero(self, clave: str):
        return any(c.isdigit() for c in clave)

    @abstractmethod
    def es_valida(self, clave):
        pass


class ReglaValidacionGanimedes(ReglaValidacion):
    def __init__(self):
        super().__init__(8)

    def contiene_caracter_especial(self, clave: str):
        caracteres_especiales = '@_#$%'
        return any(c in caracteres_especiales for c in clave)

    def es_valida(self, clave) -> bool:
        if not self._validar_longitud(clave):
            raise NoCumpleLongitudMinimaError(f"La clave debe tener una longitud de más de {self._longitud_esperada} caracteres")
        if not self._contiene_mayuscula(clave):
            raise NoTieneLetraMayusculaError("La clave debe contener al menos una letra mayúscula")
        if not self._contiene_minuscula(clave):
            raise NoTieneLetraMinusculaError("La clave debe contener al menos una letra minuscula")
        if not self._contiene_numero(clave):
            raise NoTieneNumeroError("La clave debe contener al menos un número")
        if not self.contiene_caracter_especial(clave):
            raise NoTieneCaracterEspecialError("La clave debe contener al menos uno de los caracteres especiales @, _, #, $ o %")
        return True


class ReglaValidacionCalisto(ReglaValidacion):
    def __init__(self):
        super().__init__(6)

    def contiene_calisto(self, clave):
        clave_lower = clave.lower()
        if 'calisto' not in clave_lower:
            return False
        calisto_index = clave_lower.index('calisto')
        calisto_word = clave[calisto_index:calisto_index + 7]
        mayuscula = sum(1 for c in calisto_word if c.isupper())
        return 2 <= mayuscula < 7


    def es_valida(self, clave):
        if not self._validar_longitud(clave):
            raise NoCumpleLongitudMinimaError(
                f"La clave debe tener una longitud de más de {self._longitud_esperada} caracteres")
        if not self._contiene_numero(clave):
            raise NoTieneNumeroError("La clave debe contener al menos un número")
        if not self.contiene_calisto(clave):
            raise NoTienePalabraSecretaError("La clave debe contener la palabra 'calisto'")

        return True


class Validador:
    def __init__(self, regla):
        self._regla = regla

    def es_valida(self, clave):
        return self._regla.es_valida(clave)
