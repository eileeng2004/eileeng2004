from cuentaAhorro import CuentaAhorro
from cuentaCorriente import CuentaCorriente


class Test(CuentaAhorro, CuentaCorriente):
    def _init_(self, numero, nombre_propietario, saldo, interes, tieneChequera):
        CuentaAhorro._init_(self, numero, nombre_propietario, saldo, interes)
        CuentaCorriente._init_(self, numero, nombre_propietario, saldo, tieneChequera)


# Ejemplo
cuenta_pr = Test('20040709', 'Lauren Jauregui', 6549.72, 8.0, True)

# Acceder a propiedades y métodos de ambas clases base
print("Saldo de la cuenta de ahorros:")
print(cuenta_pr.saldo)
print("Tiene chequera en la cuenta corriente:")
print(cuenta_pr.tieneChequera)

# Realizar transacciones
cuenta_pr.credito(205.0)
cuenta_pr.debito(462.0)
cuenta_pr.pagar_cheque(194.0)

# Mostrar saldos después de las transacciones
print("Saldo después de las transacciones:")
print(cuenta_pr.saldo)