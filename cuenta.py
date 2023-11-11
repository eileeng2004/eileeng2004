from abc import ABC, abstractmethod


class cuenta(ABC):
    def _init_(self, numero: str = None, nombre_propietario: str = None, saldo: float = None):
        self._numero = numero
        self._nombre_propietario = nombre_propietario
        self._saldo = saldo

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, numero):
        self._numero = numero

    @property
    def nombrePropietario(self):
        return self._nombrePropietario

    @nombrePropietario.setter
    def nombrePropietario(self, nombre):
        self._nombrePropietario = nombre

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, nuevo_saldo):
        self._saldo = nuevo_saldo

    @abstractmethod
    def credito(self, cantidad):
        pass

    @abstractmethod
    def debito(self, cantidad):
        pass

    def mostrar_saldo(self):
        print(f"Saldo de la cuenta {self.numero}: ${self.saldo}")