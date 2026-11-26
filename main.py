from flask import Flask, render_template, request

app = Flask(__name__)

PRECIO_TARRO = 9000

USUARIOS = {
    "juan": {"clave": "admin", "mensaje": "Bienvenido Administrador juan"},
    "pepe": {"clave": "user", "mensaje": "Bienvenido Usuario pepe"},
}


def calcular_porcentaje_descuento(edad):
    """Devuelve el porcentaje de descuento según la edad."""
    if edad < 18:
        return 0
    if edad <= 30:
        return 15
    return 25


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    resultado = None
    error = None

    if request.method == "POST":
        nombre = request.form.get("nombre", "").strip()
        try:
            edad = int(request.form.get("edad", ""))
            tarros = int(request.form.get("tarros", ""))
        except ValueError:
            edad = tarros = None
            error = "La edad y la cantidad de tarros deben ser números enteros."

        if error is None and (not nombre or edad < 0 or tarros < 0):
            error = "Ingresa un nombre y valores no negativos."

        if error is None:
            total_sin_descuento = tarros * PRECIO_TARRO
            porcentaje = calcular_porcentaje_descuento(edad)
            descuento = total_sin_descuento * porcentaje / 100
            resultado = {
                "nombre": nombre,
                "total_sin_descuento": total_sin_descuento,
                "descuento": descuento,
                "total_a_pagar": total_sin_descuento - descuento,
            }

    return render_template("ejercicio1.html", resultado=resultado, error=error)


@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    mensaje = None

    if request.method == "POST":
        usuario = request.form.get("usuario", "").strip()
        clave = request.form.get("clave", "")
        datos = USUARIOS.get(usuario)

        if datos and datos["clave"] == clave:
            mensaje = datos["mensaje"]
        else:
            mensaje = "Usuario o contraseña incorrectos"

    return render_template("ejercicio2.html", mensaje=mensaje)


if __name__ == "__main__":
    app.run(debug=True)
