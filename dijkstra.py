import heapq

def ruta_mas_corta(grafo, inicio, destino):
    distancias = {nodo: float('infinity') for nodo in grafo}
    distancias[inicio] = 0
    cola_prioridad = [(0, inicio)]
    camino_previo = {}

    while cola_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)

        if distancia_actual > distancias[nodo_actual]:
            continue

        if nodo_actual == destino:
            ruta = []
            while nodo_actual in camino_previo:
                ruta.insert(0, nodo_actual)
                nodo_actual = camino_previo[nodo_actual]
            ruta.insert(0, inicio)
            return ruta, distancias[destino]

        for vecino, peso in grafo[nodo_actual].items():
            distancia = distancia_actual + peso
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                camino_previo[vecino] = nodo_actual
                heapq.heappush(cola_prioridad, (distancia, vecino))
                
    return None, float('infinity')