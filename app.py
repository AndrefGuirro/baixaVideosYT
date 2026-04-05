from flask import Flask, request, send_file, render_template
from main import baixar_video
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/download", methods=["POST"])
def download():
    url = request.form.get("url")

    if not url:
        return "URL não enviada", 400

    arquivo = baixar_video(url)

    nome_arquivo = os.path.basename(arquivo)

    return send_file(
        arquivo,
        as_attachment=True,
        download_name=nome_arquivo
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)