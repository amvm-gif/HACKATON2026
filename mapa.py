# Distancias estimadas en metros según el plano visual
grafo_ucb = {
    'Atrio': {'J': 20, 'G1': 40, 'Capilla': 50},
    'J': {'Atrio': 20, 'K': 10, 'D': 30},
    'K': {'J': 10, 'G1': 20},
    'D': {'J': 30, 'A': 40, 'G1': 30}, # El Bloque D conecta hacia el A y el G1
    'G1': {'Atrio': 40, 'K': 20, 'D': 30, 'G2': 10, 'Agora': 20},
    'G2': {'G1': 10, 'Cafeteria': 20},
    'Agora': {'G1': 20, 'B': 30, 'F': 50},
    'Cafeteria': {'G2': 20, 'Capilla': 30, 'Biblioteca_I': 40},
    'Capilla': {'Atrio': 50, 'Cafeteria': 30, 'Biblioteca_I': 30},
    'Biblioteca_I': {'Cafeteria': 40, 'Capilla': 30, 'F': 30},
    'F': {'Agora': 50, 'Biblioteca_I': 30, 'C': 20},
    'A': {'D': 40, 'B': 30},
    'B': {'A': 30, 'Agora': 30, 'C': 20},
    'C': {'B': 20, 'F': 20}
}