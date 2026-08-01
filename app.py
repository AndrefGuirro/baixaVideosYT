import os
import urllib.parse

from flask import Flask, redirect, render_template, request, send_file, url_for

from main import baixar_midia

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 200 * 1024 * 1024


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/download", methods=["GET", "POST"])
def download():
    if request.method == "GET":
        return redirect(url_for("home"))
    url = (request.form.get("url") or "").strip()
    tipo = (request.form.get("tipo") or "video").strip()

    if not url:
        mensagem = urllib.parse.quote("Cole um link válido do YouTube.")
        return redirect(url_for("home", error=mensagem))

    try:
        arquivo = baixar_midia(url, tipo)
        nome_arquivo = os.path.basename(arquivo)
        return send_file(arquivo, as_attachment=True, download_name=nome_arquivo)
    except Exception as exc:
        mensagem = urllib.parse.quote(f"Não foi possível concluir o download: {exc}")
        return redirect(url_for("home", error=mensagem))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)