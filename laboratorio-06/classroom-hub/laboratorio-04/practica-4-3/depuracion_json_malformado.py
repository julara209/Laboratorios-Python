import json

malo = '''[
  {"codigo": "P001", "nombre": "Teclado"}
  {"codigo": "P002", "nombre": "Mouse"}
]'''
try:
    json.loads(malo)
except json.JSONDecodeError as error:
    print("Inválido:", error)

bueno = '''[
  {"codigo": "P001", "nombre": "Teclado"},
  {"codigo": "P002", "nombre": "Mouse"}
]'''
print("Corregido:", json.loads(bueno))
