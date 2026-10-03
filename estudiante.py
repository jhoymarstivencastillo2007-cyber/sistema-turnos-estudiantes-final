class Estudiante:
    def __init__(self, codigo, nombre, motivo, dependencia):
        self.codigo = codigo
        self.nombre = nombre
        self.motivo = motivo
        self.dependencia = dependencia

    def __str__(self):
        return (
            f"Código: {self.codigo} | "
            f"Nombre: {self.nombre} | "
            f"Motivo: {self.motivo} | "
            f"Dependencia: {self.dependencia}"
        )