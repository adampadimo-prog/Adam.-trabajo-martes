
## Importamos flask
from flask import Flask
from flask_cors import CORS
app=Flask(__name__)
CORS(app)

## Definimos la ruta principal
@app.route("/")
def HolaFlask():
    return "<h1>¡Hola Flask!</h1> <hr>"

## Ahora tomamos la segunda ruta y la reemplazamos por el siguiente ejemplo
## 1.) Haga un programa que calcule el promedio de notas sabiendo que tienen un valor de
## 30%, 30% y 40% respectivamente.
@app.route("/notas")
@app.route("/notas/<float:nota1>/<float:nota2>/<float:nota3>")
def notas(nota1=0, nota2=0, nota3=0):
    resultado = (nota1*30)/100+(nota2*30)/100+(nota3*40)/100
    return f"<h1>El resultado es: {resultado}</h1> <hr>"

## Tomamos la tercera ruta y la reemplazamos por el siguiente ejemplo
## 2.) Un programa que al capturar la edad de una persona diga si es:
## Menor de edad (Menor a 18 años)
## Adulto (Mayor o igual a 18 años y menor a 60 años)
## Adulto mayor (Mayor o igual a 60 años)
@app.route("/edades")
@app.route("/edades/<int:edad>")
def edades(edad=0):
    if edad < 18:
        R = "Menor de edad"
    elif edad < 60:
        R = "Adulto"
    else:
        R = "Adulto mayor"
    return f"<h1>La persona es: {R}</h1> <hr>"

## Creamos otra ruta realizamos el siguiente ejemplo
## 3.) Programa que crea arreglos con valores aleatorios
## Importamos la libreria numpy si no existe la instalamos con: pip install numpy
import numpy as np

@app.route("/arreglos")
@app.route("/arreglos/<int:valores>/<int:columnas>")
@app.route("/arreglos/<int:valores>/<int:columnas>/<int:filas>")
def arreglos(valores=0, columnas=0, filas=0):
    if filas==0:
        arreglo=np.random.randint(valores, size=columnas)
    else:
        arreglo=np.random.randint(valores, size=(filas,columnas))

    return f"<h1>El arreglo aleatorio es: {arreglo}</h1> <hr>"

## 4.) Programa que calcule la siguiente ecuación: Y = X * Z + Z + X

@app.route("/ecuacion")
@app.route("/ecuacion/<float:x>/<float:z>")
def ecuacion(x=0, z=0):
    Y = x * z + z + x
    return f"<h1>El resultado de la ecuación es: {Y}</h1> <hr>"

## 5.) Programa que realice la tabla de multiplicar de un número hasta el 10.

@app.route("/tabla")
@app.route("/tabla/<int:numero>")
def tabla(numero=0):
    resultado = "<h1>Tabla de multiplicar</h1>"
    for i in range(1, 11):
        resultado += f"<h2>{numero} x {i} = {numero*i}</h2>"
    return resultado + "<hr>"

if __name__ == '__main__':
    ## El valor True indica que la app se deja en modo debug
    app.run(debug=True)