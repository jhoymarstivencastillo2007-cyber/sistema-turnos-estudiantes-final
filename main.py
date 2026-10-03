from estudiante import Estudiante
from lista_enlazada import ListaEnlazada
from cola import Cola
from cola_lista import ColaLista
from arbol_bst import ArbolBST
from grafo import Grafo

lista = ListaEnlazada()

maria = Estudiante(
    1001,
    "María",
    "Matrícula",
    "Registro Académico"
)

jose = Estudiante(
    1002,
    "José",
    "Certificado",
    "Secretaría"
)

santiago = Estudiante(
    1003,
    "Santiago",
    "Notas",
    "Registro Académico"
)


lista.insertar(maria)
lista.insertar(jose)
lista.insertar(santiago)


print("===== ESTUDIANTES REGISTRADOS =====")
lista.recorrer()


print("\n===== BÚSQUEDA =====")

resultado = lista.buscar(1002)

if resultado is not None:
    print("Estudiante encontrado:")
    print(resultado)
else:
    print("Estudiante no encontrado.")


    print("\n===== ELIMINAR ESTUDIANTE =====")

eliminado = lista.eliminar(1002)

if eliminado:
    print("Estudiante eliminado correctamente.")
else:
    print("No se encontró el estudiante.")

print("\n===== LISTA DESPUÉS DE ELIMINAR =====")
lista.recorrer()

print("\n===== COLA DE TURNOS =====")

cola = Cola()

cola.encolar(maria)
cola.encolar(jose)
cola.encolar(santiago)

cola.mostrar()

print("\n===== ATENDER ESTUDIANTE =====")

cola.desencolar()

print("\n===== COLA DESPUÉS DE ATENDER =====")
cola.mostrar()

print("\n===== PRUEBA DE COLA LLENA =====")

estudiante4 = Estudiante(
    1004,
    "Laura",
    "Certificado de notas",
    "Secretaría"
)

estudiante5 = Estudiante(
    1005,
    "Carlos",
    "Matrícula",
    "Registro Académico"
)

estudiante6 = Estudiante(
    1006,
    "Andrés",
    "Cambio de programa",
    "Registro Académico"
)

estudiante7 = Estudiante(
    1007,
    "Valentina",
    "Solicitud de certificado",
    "Secretaría"
)

cola.encolar(estudiante4)
cola.encolar(estudiante5)
cola.encolar(estudiante6)
cola.encolar(estudiante7)

cola.mostrar()

print("\n===== PRUEBA DE COLA VACÍA =====")

while cola.desencolar() is not None:
    pass

cola.desencolar()

print("\n===== COLA CON LISTA ENLAZADA =====")

cola_enlazada = ColaLista()

cola_enlazada.encolar(maria)
cola_enlazada.encolar(jose)
cola_enlazada.encolar(santiago)

cola_enlazada.mostrar()

print("\n===== ATENDER CON COLA ENLAZADA =====")

cola_enlazada.desencolar()

print("\n===== COLA DESPUÉS DE ATENDER =====")
cola_enlazada.mostrar()

print("\n===== ÁRBOL BINARIO DE BÚSQUEDA =====")

arbol = ArbolBST()

arbol.insertar(maria.codigo, maria)
arbol.insertar(jose.codigo, jose)
arbol.insertar(santiago.codigo, santiago)

print("\nPreorden:")
arbol.preorden(arbol.raiz)

print("\nInorden:")
arbol.inorden(arbol.raiz)

print("\nPostorden:")
arbol.postorden(arbol.raiz)

print("\n===== BÚSQUEDA EN EL ÁRBOL =====")

resultado_arbol = arbol.buscar(1003)

if resultado_arbol is not None:
    print("Estudiante encontrado:")
    print(resultado_arbol)
else:
    print("Estudiante no encontrado.")


print("\n===== EXPERIMENTO DE ALTURA =====")

codigos = [
    1008, 1003, 1012, 1001, 1005,
    1010, 1015, 1002, 1004, 1006,
    1009, 1011, 1013, 1014, 1007
]

print("Cantidad de códigos:", len(codigos))

altura_actual = arbol.altura(arbol.raiz)

print("Altura del árbol actual:", altura_actual)

print("\n===== ÁRBOL CON 15 CLAVES =====")

arbol_15 = ArbolBST()

for codigo in codigos:
    estudiante_prueba = Estudiante(
        codigo,
        f"Estudiante {codigo}",
        "Prueba",
        "Registro Académico"
    )

    arbol_15.insertar(codigo, estudiante_prueba)

print("Inorden de las 15 claves:")
arbol_15.inorden(arbol_15.raiz)

print("\nAltura del árbol:")
print(arbol_15.altura(arbol_15.raiz))

print("\n===== ÁRBOL CON CLAVES ORDENADAS =====")

arbol_ordenado = ArbolBST()

codigos_ordenados = sorted(codigos)

for codigo in codigos_ordenados:
    estudiante_prueba = Estudiante(
        codigo,
        f"Estudiante {codigo}",
        "Prueba",
        "Registro Académico"
    )

    arbol_ordenado.insertar(codigo, estudiante_prueba)

altura_ordenado = arbol_ordenado.altura(arbol_ordenado.raiz)

print("Claves ordenadas:")
arbol_ordenado.inorden(arbol_ordenado.raiz)

print("\nAltura del árbol ordenado:", altura_ordenado)


print("\n===== TABLA DEL EXPERIMENTO =====")

cantidades = [5, 10, 15]

for cantidad in cantidades:
    arbol_prueba = ArbolBST()

    for codigo in codigos[:cantidad]:
        estudiante_prueba = Estudiante(
            codigo,
            f"Estudiante {codigo}",
            "Prueba",
            "Registro Académico"
        )

        arbol_prueba.insertar(codigo, estudiante_prueba)

    altura = arbol_prueba.altura(arbol_prueba.raiz)

    print(
        f"Cantidad de claves: {cantidad} | "
        f"Altura: {altura}"
    )

    print("\n===== GRAFO DE DEPENDENCIAS =====")

grafo = Grafo()

grafo.agregar_vertice("Registro Académico")
grafo.agregar_vertice("Secretaría")
grafo.agregar_vertice("Tesorería")

grafo.agregar_conexion(
    "Registro Académico",
    "Secretaría"
)

grafo.agregar_conexion(
    "Secretaría",
    "Tesorería"
)

print("\n===== CONSULTA 1 =====")
grafo.mostrar_conexiones("Secretaría")

print("\n===== CONSULTA 2 =====")

if grafo.existe_conexion("Registro Académico", "Secretaría"):
    print("Sí existe conexión entre Registro Académico y Secretaría.")
else:
    print("No existe conexión entre Registro Académico y Secretaría.")

    print("\n===== PRUEBA: ESTUDIANTE INEXISTENTE =====")

resultado = lista.buscar(9999)

if resultado is not None:
    print("Estudiante encontrado:")
    print(resultado)
else:
    print("No se encontró el estudiante con código 9999.")

    print("\n===== PRUEBA: ELIMINAR ESTUDIANTE INEXISTENTE =====")

eliminado = lista.eliminar(9999)

if eliminado:
    print("Estudiante eliminado correctamente.")
else:
    print("No se encontró el estudiante con código 9999.")

    print("\n===== PRUEBA: UN SOLO ESTUDIANTE =====")

lista_prueba = ListaEnlazada()

estudiante_unico = Estudiante(
    2001,
    "Pedro",
    "Consulta",
    "Secretaría"
)

lista_prueba.insertar(estudiante_unico)

print("Antes de eliminar:")
lista_prueba.recorrer()

eliminado = lista_prueba.eliminar(2001)

if eliminado:
    print("\nEl único estudiante fue eliminado correctamente.")

print("\nDespués de eliminar:")
lista_prueba.recorrer()

print("\n===== PRUEBA: CÓDIGO REPETIDO =====")

arbol_repetido = ArbolBST()

arbol_repetido.insertar(3001, maria)
arbol_repetido.insertar(3001, jose)

print("\n===== PRUEBA DE COLA =====")

cola = Cola()

cola.encolar(maria)
cola.encolar(jose)
cola.encolar(santiago)

cola.mostrar()

print("\nAtendiendo estudiante:")
cola.desencolar()

print("\nCola después de atender:")
cola.mostrar()

cola = ColaLista()

print("\n===== PRUEBA: COLA VACÍA =====")

cola_vacia = ColaLista()

cola_vacia.desencolar()