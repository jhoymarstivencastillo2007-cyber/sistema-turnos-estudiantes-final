class NodoCola:
    def __init__(self, estudiante):
        self.estudiante = estudiante
        self.siguiente = None


class ColaLista:
    def __init__(self, capacidad=5):
        self.capacidad = capacidad
        self.cantidad = 0
        self.frente = None
        self.final = None

    def encolar(self, estudiante):
        if self.cantidad >= self.capacidad:
            print("La cola está llena. No se puede agregar otro estudiante.")
            return False

        nuevo = NodoCola(estudiante)

        if self.frente is None:
            self.frente = nuevo
            self.final = nuevo
        else:
            self.final.siguiente = nuevo
            self.final = nuevo

        self.cantidad += 1
        print(f"{estudiante.nombre} fue agregado a la cola.")
        return True

    def desencolar(self):
        if self.frente is None:
            print("La cola está vacía. No hay estudiantes para atender.")
            return None

        estudiante = self.frente.estudiante
        self.frente = self.frente.siguiente

        if self.frente is None:
            self.final = None

        self.cantidad -= 1

        print(f"Atendiendo a: {estudiante.nombre}")
        return estudiante

    def mostrar(self):
        if self.frente is None:
            print("La cola está vacía.")
            return

        print("\n===== ESTUDIANTES EN ESPERA =====")

        actual = self.frente
        posicion = 1

        while actual is not None:
            print(
                f"{posicion}. "
                f"{actual.estudiante.nombre} - "
                f"{actual.estudiante.motivo}"
            )

            actual = actual.siguiente
            posicion += 1