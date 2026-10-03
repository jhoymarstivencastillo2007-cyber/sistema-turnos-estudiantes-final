class Nodo:
    def __init__(self, estudiante):
        self.estudiante = estudiante
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar(self, estudiante):
        nuevo = Nodo(estudiante)

        if self.cabeza is None:
            self.cabeza = nuevo
            return

        actual = self.cabeza

        while actual.siguiente is not None:
            actual = actual.siguiente

        actual.siguiente = nuevo

    def recorrer(self):
        if self.cabeza is None:
            print("La lista está vacía.")
            return

        actual = self.cabeza

        while actual is not None:
            print(actual.estudiante)
            actual = actual.siguiente

    def buscar(self, codigo):
        actual = self.cabeza

        while actual is not None:
            if actual.estudiante.codigo == codigo:
                return actual.estudiante

            actual = actual.siguiente

        return None

    def eliminar(self, codigo):
        if self.cabeza is None:
            print("La lista está vacía.")
            return False

        if self.cabeza.estudiante.codigo == codigo:
            self.cabeza = self.cabeza.siguiente
            return True

        anterior = self.cabeza
        actual = self.cabeza.siguiente

        while actual is not None:
            if actual.estudiante.codigo == codigo:
                anterior.siguiente = actual.siguiente
                return True

            anterior = actual
            actual = actual.siguiente

        return False