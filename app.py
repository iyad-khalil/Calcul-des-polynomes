from flask import Flask, render_template, request, jsonify
from polynome_utils import calculer_racines, factoriser_polynome, tracer_polynome, methode_newton
import os
from flask import send_file

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/racines", methods=["POST"])
def racines():
    data = request.json
    coefficients = data.get("coefficients", [])
    complexes = data.get("complexes", False)
    try:
        racines = calculer_racines(coefficients, complexes=complexes)
        return jsonify({"racines": [str(r) for r in racines]})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/factorisation", methods=["POST"])
def factorisation():
    data = request.json
    coefficients = data.get("coefficients", [])
    try:
        factorise = factoriser_polynome(coefficients)
        return jsonify({"factorisation": str(factorise)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/graphe_image", methods=["POST"])
def graphe_image():
    data = request.json
    coefficients = data.get("coefficients", [])
    xmin = data.get("xmin", -10)
    xmax = data.get("xmax", 10)
    points = data.get("points", 500)
    try:
        image_path = "static/graphe.png"
        tracer_polynome(coefficients, xmin=xmin, xmax=xmax, points=points, save_as=image_path)
        return jsonify({"image_url": image_path})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/newton", methods=["POST"])
def newton():
    data = request.json
    coefficients = data.get("coefficients", [])
    x0 = data.get("x0", 0)
    tol = data.get("tol", 1e-6)
    max_iter = data.get("max_iter", 100)
    try:
        racine = methode_newton(coefficients, x0=x0, tol=tol, max_iter=max_iter)
        return jsonify({"racine": racine})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
