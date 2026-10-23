class ReporteTexto:
    def generar(self, datos):
        return "Datos: " + ", ".join(str(d) for d in datos)


class ReporteResumen:
    def generar(self, datos):
        return f"Se recibieron {len(datos)} registros."


datos = ["Teclado", "Mouse", "Monitor"]
for reporte in [ReporteTexto(), ReporteResumen()]:
    print(reporte.generar(datos))
