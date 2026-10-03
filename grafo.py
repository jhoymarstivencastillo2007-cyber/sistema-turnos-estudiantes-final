class Grafo:
    def __init__(self):
        self.vertices = []

    def agregar_vertice(self, nombre):
        for vertice in self.vertices:
            if vertice["nombre"] == nombre:
                return

        nuevo_vertice = {
            "nombre": nombre,
            "adyacentes": []
        }

        self.vertices.append(nuevo_vertice)

    def agregar_conexion(self, origen, destino):
        vertice_origen = self.buscar_vertice(origen)
        vertice_destino = self.buscar_vertice(destino)

        if vertice_origen is None or vertice_destino is None:
            return

        if destino not in vertice_origen["adyacentes"]:
            vertice_origen["adyacentes"].append(destino)

        if origen not in vertice_destino["adyacentes"]:
            vertice_destino["adyacentes"].append(origen)

    def buscar_vertice(self, nombre):
        for vertice in self.vertices:
            if vertice["nombre"] == nombre:
                return vertice

        return None

    def mostrar_conexiones(self, nombre):
        vertice = self.buscar_vertice(nombre)

        if vertice is None:
            print("El vértice no existe.")
            return

        print(f"Conexiones de {nombre}:")

        if len(vertice["adyacentes"]) == 0:
            print("No tiene conexiones.")
            return

        for conexion in vertice["adyacentes"]:
            print(f"- {conexion}")

    def existe_conexion(self, origen, destino):
        vertice = self.buscar_vertice(origen)

        if vertice is None:
            return False

        return destino in vertice["adyacentes"]