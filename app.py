from flask import Flask

#Crear instancia
app = Flask(__name__)

#Ruta raiz
@app.route('/') 
def hola_mundo():
    return 'Hola mundo'

#Ruta alumnos
@app.route('/alumnos') 
def alumnos():
    return 'Aqui van los alumnos'


if __name__ == '__main__':
    app.run(debug=True)