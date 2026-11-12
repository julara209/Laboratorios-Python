codigos = [" p001 ", "P002", "", " p003", "  "]

limpios = [c.strip().upper() for c in codigos if c.strip() != ""]
print(limpios)
