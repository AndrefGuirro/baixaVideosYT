from pytubefix import YouTube
import os
import re

def limpar_nome(nome):
    return re.sub(r'[\\/*?:"<>|]', "", nome)

def baixar_video(url, pasta="downloads"):
    if not os.path.exists(pasta):
        os.makedirs(pasta)

    yt = YouTube(url)

    titulo = limpar_nome(yt.title)

    stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

    caminho = stream.download(output_path=pasta, filename=titulo)

    return caminho