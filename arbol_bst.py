class NodoArbol:
    def __init__(self, codigo, estudiante):
        self.codigo = codigo
        self.estudiante = estudiante
        self.izquierda = None
        self.derecha = None


class ArbolBST:
    def __init__(self):
        self.raiz = None

    def insertar(self, codigo, estudiante):
        nuevo = NodoArbol(codigo, estudiante)

        if self.raiz is None:
            self.raiz = nuevo
            return

        actual = self.raiz

        while True:
            if codigo < actual.codigo:
                if actual.izquierda is None:
                    actual.izquierda = nuevo
                    return
                actual = actual.izquierda

            elif codigo > actual.codigo:
                if actual.derecha is None:
                    actual.derecha = nuevo
                    return
                actual = actual.derecha

            else:
                print("El código ya existe en el árbol.")
                return

    def buscar(self, codigo):
        actual = self.raiz

        while actual is not None:
            if codigo == actual.codigo:
                return actual.estudiante

            if codigo < actual.codigo:
                actual = actual.izquierda
            else:
                actual = actual.derecha

        return None

    def eliminar(self, codigo):
        self.raiz = self._eliminar_recursivo(self.raiz, codigo)

    def _eliminar_recursivo(self, nodo, codigo):
        if nodo is None:
            return None

        if codigo < nodo.codigo:
            nodo.izquierda = self._eliminar_recursivo(
                nodo.izquierda, codigo
            )

        elif codigo > nodo.codigo:
            nodo.derecha = self._eliminar_recursivo(
                nodo.derecha, codigo
            )

        else:
            if nodo.izquierda is None:
                return nodo.derecha

            if nodo.derecha is None:
                return nodo.izquierda

            sucesor = nodo.derecha

            while sucesor.izquierda is not None:
                sucesor = sucesor.izquierda

            nodo.codigo = sucesor.codigo
            nodo.estudiante = sucesor.estudiante

            nodo.derecha = self._eliminar_recursivo(
                nodo.derecha, sucesor.codigo
            )

        return nodo

    def preorden(self, nodo):
        if nodo is not None:
            print(nodo.codigo, end=" ")
            self.preorden(nodo.izquierda)
            self.preorden(nodo.derecha)

    def inorden(self, nodo):
        if nodo is not None:
            self.inorden(nodo.izquierda)
            print(nodo.codigo, end=" ")
            self.inorden(nodo.derecha)

    def postorden(self, nodo):
        if nodo is not None:
            self.postorden(nodo.izquierda)
            self.postorden(nodo.derecha)
            print(nodo.codigo, end=" ")

    def altura(self, nodo):
        if nodo is None:
            return 0

        altura_izquierda = self.altura(nodo.izquierda)
        altura_derecha = self.altura(nodo.derecha)

        return 1 + max(altura_izquierda, altura_derecha)