def calcular_cobro(valor_compra, envio=10000):
    return valor_compra + envio


print("Con envío predeterminado:", calcular_cobro(150000))       
print("Con envío gratuito:", calcular_cobro(150000, envio=0))    