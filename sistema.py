from estudiante import Estudiante
from lista_enlazada import ListaEnlazada
from cola import Cola
from cola_lista import ColaLista
from arbol_bst import ArbolBST
from grafo import Grafo

lista = ListaEnlazada()
cola = ColaLista()
arbol = ArbolBST()

grafo = Grafo()

grafo.agregar_vertice("Registro Académico")
grafo.agregar_vertice("Secretaría")
grafo.agregar_vertice("Tesorería")

grafo.agregar_conexion("Registro Académico", "Secretaría")
grafo.agregar_conexion("Secretaría", "Tesorería")

def registrar_estudiante():
    
    codigo = int(input("Código del estudiante: "))



    resultado = lista.buscar(codigo)

    
    

    if resultado is not None:
        print("\nEl código ya existe.")
        return

    nombre = input("Nombre del estudiante: ")
    motivo = input("Motivo de la atención: ")
    dependencia = input("Dependencia: ")

    estudiante = Estudiante(codigo, nombre, motivo, dependencia)

    lista.insertar(estudiante)
    arbol.insertar(codigo, estudiante)

    print("\nEstudiante registrado correctamente.")

def mostrar_estudiantes():
    print("\n===== ESTUDIANTES REGISTRADOS =====")
    lista.recorrer()

def buscar_en_arbol():
    codigo = int(input("Código que desea buscar en el árbol: "))

    estudiante = arbol.buscar(codigo)

    if estudiante is not None:
        print("\nEstudiante encontrado en el árbol:")
        print(estudiante)
    else:
        print("\nNo se encontró el estudiante en el árbol.")

def mostrar_recorridos():
    if arbol.raiz is None:
        print("\nEl árbol está vacío.")
        return

    print("\n===== RECORRIDOS DEL ÁRBOL BST =====")

    print("Preorden:")
    arbol.preorden(arbol.raiz)

    print("\nInorden:")
    arbol.inorden(arbol.raiz)

    print("\nPostorden:")
    arbol.postorden(arbol.raiz)

    print()


def consultar_grafo():
    print("\n===== CONSULTA DEL GRAFO =====")

    grafo.mostrar_conexiones("Secretaría")

    print("\n¿Existe conexión entre Registro Académico y Secretaría?")

    if grafo.existe_conexion("Registro Académico", "Secretaría"):
        print("Sí existe conexión.")
    else:
        print("No existe conexión.")  

def buscar_estudiante():
    codigo = int(input("Código que desea buscar: "))

    estudiante = lista.buscar(codigo)

    if estudiante is not None:
        print("\nEstudiante encontrado:")
        print(estudiante)
    else:
        print("\nNo se encontró el estudiante.")

def eliminar_estudiante():
    codigo = int(input("Código del estudiante que desea eliminar: "))

    estudiante = lista.buscar(codigo)

    if estudiante is None:
        print("\nNo se encontró el estudiante.")
        return

    lista.eliminar(codigo)
    arbol.eliminar(codigo)

    print("\nEstudiante eliminado correctamente.")


def agregar_a_cola():
    codigo = int(input("Código del estudiante: "))

    estudiante = lista.buscar(codigo)

    if estudiante is None:
        print("\nNo se encontró el estudiante.")
        return

    cola.encolar(estudiante)


def atender_estudiante():
    cola.desencolar()


def mostrar_cola():
    cola.mostrar()


def menu():
    while True:
        print("\n==============================")
        print(" SISTEMA DE TURNOS")
        print("==============================")
        print("1. Registrar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Buscar estudiante")
        print("4. Eliminar estudiante")
        print("5. Agregar estudiante a la cola")
        print("6. Atender estudiante")
        print("7. Mostrar cola")
        print("8. Buscar en árbol BST")
        print("9. Mostrar recorridos del árbol")
        print("10. Consultar grafo")
        print("11. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            registrar_estudiante()

        elif opcion == "2":
            mostrar_estudiantes()

        elif opcion == "3":
            buscar_estudiante()

        elif opcion == "4":
            eliminar_estudiante()

        elif opcion == "5":
            agregar_a_cola()

        elif opcion == "6":
            atender_estudiante()

        elif opcion == "7":
            mostrar_cola()

        elif opcion == "8":
            buscar_en_arbol()

        elif opcion == "9":
            mostrar_recorridos()

        elif opcion == "10":
            consultar_grafo()

        elif opcion == "11":
            print("\nPrograma finalizado.")
            break
        else:
            print("\nOpción no válida.")

menu() 