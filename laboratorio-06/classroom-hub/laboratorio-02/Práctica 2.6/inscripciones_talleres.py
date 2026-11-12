python = {"Ana", "Carlos", "Laura", "Sara", "Mateo"}
java = {"Laura", "Sara", "David", "Pablo"}

print("En al menos uno:", python | java)
print("En ambos:", python & java)
print("Solo Python:", python - java)
print("Solo Java:", java - python)
print("En uno solo de los talleres:", python ^ java)
