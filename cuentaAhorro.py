from cuenta import cuenta


class CuentaAhorro(cuenta):
    def _init_(self, numero, nombre_propietario, saldo, interes: float = None):
        super()._init_(numero, nombre_propietario, saldo)
        self._interes = interes

    @property
    def interes(self):
        return self._interes

    @interes.setter
    def interes(self, nuevo_interes):
        self._interes = nuevo_interes

    def credito(self, cantidad):
        self.saldo += cantidad

    def debito(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print("Fondos insuficientes")

    def mostrar_saldo(self):
        print(f"Saldo de la cuenta de ahorros {self.numero}: ${self.saldo}")

    def pagar_interes(self):
        interes_ganado = self.saldo * (self.interes / 100)
        self.saldo += interes_ganado



cuenta_pr = CuentaAhorro(numero='147628', nombre_propietario='Eileen', saldo=4716.00, interes=2.3)
cuenta_pr.credito(325.00)
cuenta_pr.debito(160.00)
cuenta_pr.mostrar_saldo()
cuenta_pr.pagar_interes()