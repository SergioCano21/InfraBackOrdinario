from flask import Flask, jsonify

app = Flask(__name__)

# Ruta para el endpoint GET
@app.route('/saludo', methods=['GET'])
def saludo():
    return jsonify({'mensaje': 'Hola Profe pongame 10 porfa'}), 200

# Ejecución de la app
if __name__ == '__main__':
    app.run(debug=True) 
