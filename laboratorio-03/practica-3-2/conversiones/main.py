import unidades

km = float(input("Kilómetros: "))
print(km, "km =", unidades.kilometros_a_metros(km), "m")

c = float(input("Grados Celsius: "))
print(c, "°C =", unidades.celsius_a_fahrenheit(c), "°F")
