from flask import Flask, jsonify, render_template

from data import CANDIDATOS, DOCUMENTOS, FATOR_DETALHAMENTO, FONTES, calcular

app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
        "index.html",
        d=calcular(),
        candidatos=CANDIDATOS,
        documentos=DOCUMENTOS,
        fontes=FONTES,
        fatores=FATOR_DETALHAMENTO,
    )


@app.route("/api/comparacao")
def api_comparacao():
    """Mesmos dados do site em JSON (útil para reuso/embed)."""
    return jsonify(calcular())


@app.route("/healthz")
def healthz():
    return {"ok": True}


if __name__ == "__main__":
    app.run(debug=True)
