class Billetera:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0

    def registrar_ingreso(self, monto):
        if monto <= 0:
            return False
        self.saldo += monto
        return True

    def registrar_gasto(self, monto):
        if monto <= 0 or monto > self.saldo:
            return False
        self.saldo -= monto
        return True

    def consultar_saldo(self):
        return self.saldo


ana = Billetera("Ana")
luis = Billetera("Luis")

print("Ingreso Ana 50000:", ana.registrar_ingreso(50000))   
print("Gasto Ana 20000:", ana.registrar_gasto(20000))       
print("Gasto Ana 100000:", ana.registrar_gasto(100000))     
print("Ingreso Ana -5:", ana.registrar_ingreso(-5))        
print("Ingreso Luis 10000:", luis.registrar_ingreso(10000)) 

print("Saldo de Ana:", ana.consultar_saldo())     
print("Saldo de Luis:", luis.consultar_saldo())   
