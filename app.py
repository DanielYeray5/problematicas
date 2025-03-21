from flask import Flask, request, jsonify, render_template
from Optilamity import buscar_solucion_BFS as bfs_optimality
from Puzzle import buscar_solucion_DFS as dfs_puzzle
from DFS_rec import buscar_solucion_DSF_rec as dfs_rec
from Arbol import Nodo
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve_puzzle', methods=['POST'])
def solve_puzzle():
    data = request.get_json()
    estado_inicial = data['estado_inicial']
    solucion = data['solucion']
    
    nodo_solucion = dfs_puzzle(estado_inicial, solucion)

    resultado = []
    nodo = nodo_solucion
    while nodo.get_padre() is not None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()

    return jsonify({'resultado': resultado})

@app.route('/solve_dfs', methods=['POST'])
def solve_dfs():
    data = request.get_json()
    estado_inicial = data['estado_inicial']
    solucion = data['solucion']
    
    nodo_inicial = Nodo(estado_inicial)
    nodo_solucion = dfs_rec(nodo_inicial, solucion, [])

    resultado = []
    nodo = nodo_solucion
    while nodo.get_padre() is not None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()

    return jsonify({'resultado': resultado})

@app.route('/solve_optimality', methods=['POST'])
def solve_optimality():
    data = request.get_json()
    conexiones = data['conexiones']
    estado_inicial = data['estado_inicial']
    solucion = data['solucion']

    nodo_solucion = bfs_optimality(conexiones, estado_inicial, solucion)

    resultado = []
    nodo = nodo_solucion
    while nodo.get_padre() is not None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()

    return jsonify({'resultado': resultado})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8000)))