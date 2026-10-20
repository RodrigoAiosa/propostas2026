"""Gera o index.html estático a partir do template Flask (mesmos dados de data.py).

Uso:  python gerar_index.py
Saída: index.html (raiz) e public/index.html
"""
from pathlib import Path

from app import app, index

with app.test_request_context("/"):
    html = index()

raiz = Path(__file__).parent
for destino in (raiz / "index.html", raiz / "public" / "index.html"):
    destino.parent.mkdir(exist_ok=True)
    destino.write_text(html, encoding="utf-8")
    print("gerado:", destino)
