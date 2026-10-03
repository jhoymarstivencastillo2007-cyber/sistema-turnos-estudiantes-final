class Cola:
    def __init__(self, capacidad=5):
        self.capacidad = capacidad
        self.elementos = []

    def encolar(self, estudiante):
        if len(self.elementos) >= self.capacidad:
            print("La cola está llena. No se puede agregar otro estudiante.")
            return False

        self.elementos.append(estudiante)
        print(f"{estudiante.nombre} fue agregado a la cola.")
        return True

    def desencolar(self):
        if len(self.elementos) == 0:
            print("La cola está vacía. No hay estudiantes para atender.")
            return None

        estudiante = self.elementos.pop(0)
        print(f"Atendiendo a: {estudiante.nombre}")
        return estudiante

    def mostrar(self):
        if len(self.elementos) == 0:
            print("La cola está vacía.")
            return

        print("\n===== ESTUDIANTES EN ESPERA =====")

        for posicion, estudiante in enumerate(self.elementos):
            print(
                f"{posicion + 1}. "
                f"{estudiante.nombre} - {estudiante.motivo}"
            )