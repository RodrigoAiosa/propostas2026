from flask import Flask, jsonify, render_template

from conteudo import GLOSSARIO, QUIZ, SIMULADOR
from data import CANDIDATOS, DOCUMENTOS, FATOR_DETALHAMENTO, FONTES, calcular

app = Flask(__name__)


def _dados_js():
    """Dados entregues ao JavaScript (simulador, quiz e glossário)."""
    return {
        "nomes": {k: v["nome"] for k, v in CANDIDATOS.items()},
        "simulador": SIMULADOR,
        "quiz": QUIZ,
        "glossario": GLOSSARIO,
    }


@app.route("/")
def index():
    return render_template(
        "index.html",
        d=calcular(),
        candidatos=CANDIDATOS,
        documentos=DOCUMENTOS,
        fontes=FONTES,
        fatores=FATOR_DETALHAMENTO,
        sim=SIMULADOR,
        glossario=GLOSSARIO,
        dados=_dados_js(),
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
