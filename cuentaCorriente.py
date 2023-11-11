from cuenta import cuenta


class CuentaCorriente(cuenta):
    def _init_(self, numero, nombre_propietario, saldo, tieneChequera: bool = None):
        super()._init_(numero, nombre_propietario, saldo)
        self._tieneChequera = tieneChequera

    @property
    def tieneChequera(self):
        return self._tieneChequera

    @tieneChequera.setter
    def tieneChequera(self, tiene_chequera):
        self._tieneChequera = tiene_chequera

    def credito(self, cantidad):
        self.saldo += cantidad

    def debito(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print("Fondos insuficientes")

    def mostrar_saldo(self):
        print(f"Saldo de la cuenta corriente {self.numero}: ${self.saldo}")

    def pagar_cheque(self, cantidad):
        if self.tieneChequera:
            self.debito(cantidad)
            print(f"Se pagó un cheque por ${cantidad}")
        else:
            print("Esta cuenta corriente no tiene chequera")


cuenta_pr = CuentaCorriente('497822', 'Eileen Gonzalez', 1454.00, True)
cuenta_pr.credito(954.00)
cuenta_pr.debito(541.00)
cuenta_pr.mostrar_saldo()
cuenta_pr.pagar_cheque(360.00)
cuenta_pr.mostrar_saldo()