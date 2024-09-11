from flask import Flask, render_template

app = Flask(__name__)

"""
@app.route('/')
def principal():
    # return "Bienvenido o bienvenida a mi sitio web con python!"
    return "UskoKruM2010 - Suscríbete!"

@app.route('/contacto')
def contacto():
    return "Esta es la página de contacto"
"""


@app.route('/')
def principal():
    return render_template('index.html')


@app.route('/ventas')
def mostrarVentas():
    misVentas = ("parlantes", "computadoras", "celulares", "audigenos",
                    "cargadores", "impresoras", "tintas", "toner")
    return render_template('ventas.html', ventas=misVentas)


@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5017)
