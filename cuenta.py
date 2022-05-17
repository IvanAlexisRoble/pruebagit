class Cuenta:
  def __init__(self, titular, cantidad):
    self.titular = titular
    self.cantidad = cantidad
  def mostrar(self):
    print("El titular de la cuenta es", self.titular,",el saldo actual en la misma es", self.cantidad,"pesos.")
  def ingresar(self, ingresado):
    self.ingresado = ingresado
    if ingresado >= 0:
      self.cantidad += self.ingresado
      print("Se han ingresado a la cuenta", self.ingresado,"pesos, el saldo actual de la misma es", self.cantidad,"pesos.")
    else:
      pass
  def retirar(self, retirado):
    self.retirado = retirado
    self.cantidad -= self.retirado
    print("Se han retirado", self.retirado,"pesos, el saldo actual de la cuenta es", self.cantidad,"pesos.")
cuenta1=Cuenta("Iván Alexis Roble", 100.60)
cuenta1.mostrar()
cuenta1.ingresar(-20)
cuenta1.retirar(10.60)
cuenta1.ingresar(500)
cuenta1.retirar(600.50)
cuenta1.mostrar()