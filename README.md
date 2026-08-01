# BaixaVideosYT

Aplicação Flask simples para baixar vídeo ou áudio de links do YouTube.

## Como executar localmente

```bash
cd c:/baixaVideosYT
c:/baixaVideosYT/.venv/Scripts/python.exe app.py
```

Acesse em `http://127.0.0.1:5000`.

## Dependências

- Flask
- yt-dlp
- gunicorn

## Deploy no Render (gratuito)

1. Faça push deste repositório para o GitHub.
2. Crie conta gratuita em https://render.com.
3. Conecte o Render ao seu GitHub.
4. Crie um novo "Web Service".
5. Configure:
   - Ambiente: Python
   - Branch: `main` (ou a branch que usar)
   - Build command: `pip install -r requirements.txt`
   - Start command: `gunicorn --bind 0.0.0.0:$PORT wsgi:app`
6. Clique em Deploy.

## Observações

- O servidor gratuito do Render entra em modo ocioso após algum tempo sem acesso.
- Para testar localmente, use o endereço retornado pelo Render.
