from flask import Flask, render_template, request

app = Flask(__name__)

usuarios = {
    'juan': 'admin',
    'pepe': 'user'
}


@app.route('/')
def home():

    return render_template('menu_principal.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])
        precio_tarro = 9000
        total_sin_descuento = precio_tarro * cantidad
        descuento = 0

        # Aqui Aplicamos el descuento según la edad
        if 18 <= edad <= 30:
            descuento = total_sin_descuento * 0.15
        elif edad > 30:
            descuento = total_sin_descuento * 0.25

        total_con_descuento = total_sin_descuento - descuento

        return render_template('ejercicio1.html',
                               nombre=nombre,
                               total_sin_descuento=total_sin_descuento,
                               descuento=descuento,
                               total_con_descuento=total_con_descuento)
    else:

        return render_template('ejercicio1.html')


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = None
    usuario_ingresado = None
    if request.method == 'POST':
        usuario_ingresado = request.form['usuario']
        contraseña_ingresada = request.form['contraseña']

        # Aqui verificamos si el usuario y la contraseña son correctos
        if usuarios.get(usuario_ingresado) == contraseña_ingresada:

            if usuario_ingresado == 'juan':
                mensaje = 'Bienvenido Administrador juan'
            elif usuario_ingresado == 'pepe':
                mensaje = 'Bienvenido Usuario pepe'
        else:
            mensaje = 'Usuario o contraseña incorrectos'

    return render_template('ejercicio2.html', mensaje=mensaje)


if __name__ == '__main__':
    app.run(debug=True)
