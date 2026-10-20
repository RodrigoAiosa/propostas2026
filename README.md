# Propostas 2026: Lula x Flávio (Python + Vercel)

Site Flask que compara as propostas econômicas, mostra o Top 5 e os setores,
e destaca sempre quem propõe menos Estado (intenção e nota ajustada pelo detalhamento).

## Rodar local
    pip install -r requirements.txt
    python app.py

## Deploy na Vercel
    npm i -g vercel
    vercel        # preview
    vercel --prod

## Editar conteúdo
Tudo está em `data.py` (notas 0-10, detalhamento, resumos, links dos planos e fontes).
O site e a API `/api/comparacao` recalculam sozinhos.

## Aviso
As notas são uma régua editorial aberta, não uma verdade científica. Os PDFs dos planos
não são hospedados: os links apontam para a fonte original (confira o registro no TSE).

## index.html estático
`python gerar_index.py` gera `index.html` e `public/index.html` com os mesmos dados.
Rode de novo sempre que editar `data.py`.

## Erro de deploy "unused_function ... app.py"
Causa: `vercel.json` com bloco `functions` apontando para `app.py`. Foi removido;
o Flask é detectado automaticamente pelo `app.py`.
