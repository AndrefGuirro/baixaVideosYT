import os

from flask import Flask, flash, redirect, render_template, request, send_file, url_for

from main import baixar_midia

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "change-this-secret")
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
        flash("Cole um link válido do YouTube.", "error")
        return redirect(url_for("home"))

    try:
        arquivo = baixar_midia(url, tipo)
        nome_arquivo = os.path.basename(arquivo)
        return send_file(arquivo, as_attachment=True, download_name=nome_arquivo)
    except Exception as exc:
        flash(f"Não foi possível concluir o download: {exc}", "error")
        return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)