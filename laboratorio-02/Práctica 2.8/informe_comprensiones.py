ventas = [
    {"producto": "Teclado", "categoria": "Periféricos", "total": 150000},
    {"producto": "Mouse", "categoria": "Periféricos", "total": 70000},
    {"producto": "Disco SSD", "categoria": "Componentes", "total": 280000},
    {"producto": "Memoria USB", "categoria": "Accesorios", "total": 45000}
]

altos_for = []
for v in ventas:
    if v["total"] > 100000:
        altos_for.append(v["producto"])

altos = [v["producto"] for v in ventas if v["total"] > 100000]
categorias = {v["categoria"] for v in ventas}
producto_valor = {v["producto"]: v["total"] for v in ventas}
suma_total = sum([v["total"] for v in ventas])

print("Ventas > 100000 (for):", altos_for)
print("Ventas > 100000 (comprensión):", altos)
print("Categorías:", categorias)
print("Producto -> valor:", producto_valor)
print("Total de ventas:", suma_total)   # 545000
