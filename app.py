from flask import Flask, render_template, request
from mapa import grafo_ucb
from dijkstra import ruta_mas_corta

app = Flask(__name__)

# Coordenadas GPS aproximadas de la UCB La Paz para dibujar en el mapa
coordenadas_gps = {
    'Atrio': [-16.5228, -68.1118],
    'J': [-16.5226, -68.1119],
    'K': [-16.5225, -68.1118],
    'D': [-16.5223, -68.1121],
    'G1': [-16.5224, -68.1115],
    'G2': [-16.5222, -68.1114],
    'Agora': [-16.5220, -68.1116],
    'Cafeteria': [-16.5222, -68.1110],
    'Capilla': [-16.5225, -68.1110],
    'Biblioteca_I': [-16.5223, -68.1105],
    'F': [-16.5218, -68.1106],
    'A': [-16.5219, -68.1120],
    'B': [-16.5217, -68.1118],
    'C': [-16.5215, -68.1115]
}

# Lista de eventos que exige el reto
lista_eventos = [
    {"nombre": "TECH MECH Hackathon", "fecha": "Hoy", "lugar": "F"}, 
    {"nombre": "Meca Gala", "fecha": "Mañana, 19:00", "lugar": "D"},
    {"nombre": "Defensa de Grado", "fecha": "Lunes, 10:00", "lugar": "Agora"}
]

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    
    # Si el usuario presiona un botón (POST)
    if request.method == 'POST':
        origen = request.form.get('origen')
        destino = request.form.get('destino')
        
        # Ejecutar Dijkstra
        ruta, distancia = ruta_mas_corta(grafo_ucb, origen, destino)
        
        if ruta:
            # Obtener las coordenadas GPS exactas de la ruta calculada
            coords_ruta = [coordenadas_gps[nodo] for nodo in ruta]
            
            resultado = {
                'camino': " ➔ ".join(ruta),
                'distancia': distancia,
                'tiempo': round(distancia / 80, 1), # 80 m/min caminando
                'coords': coords_ruta
            }

    # Renderizar el HTML y pasarle todas las variables que tu compañero configuró
    return render_template('index.html', 
                           puntos=list(grafo_ucb.keys()), 
                           eventos=lista_eventos, 
                           coordenadas=coordenadas_gps, 
                           resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)