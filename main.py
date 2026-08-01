from __future__ import annotations

import os
import random
import re
import string
import time
from pathlib import Path

import yt_dlp

BASE_DIR = Path(__file__).resolve().parent
DOWNLOADS_DIR = BASE_DIR / "downloads"


def limpar_nome(nome: str) -> str:
    nome = re.sub(r'[\\/*?:"<>|]', "", nome or "download").strip()
    nome = re.sub(r"\s+", " ", nome)
    return nome[:100] or "download"


def get_downloads_dir() -> Path:
    DOWNLOADS_DIR.mkdir(parents=True, exist_ok=True)
    return DOWNLOADS_DIR


def gerar_caminho_download(titulo: str, tipo: str = "video") -> str:
    nome = limpar_nome(titulo)
    ext = "mp4" if tipo == "video" else "webm"
    pasta = get_downloads_dir()
    caminho = pasta / f"{nome}.{ext}"

    if caminho.exists():
        sufixo = "".join(random.choices(string.ascii_lowercase + string.digits, k=4))
        caminho = pasta / f"{nome}-{sufixo}.{ext}"

    return str(caminho)


def baixar_midia(url: str, tipo: str = "video") -> str:
    if tipo not in {"video", "audio"}:
        raise ValueError("Tipo inválido. Use 'video' ou 'audio'.")

    if not url.startswith("http"):
        raise ValueError("Informe um link válido do YouTube.")

    ydl_opts = {
        "quiet": True,
        "no_warnings": True,
        "noplaylist": True,
        "restrictfilenames": True,
        "socket_timeout": 30,
        "http_headers": {"User-Agent": "Mozilla/5.0"},
    }

    with yt_dlp.YoutubeDL({**ydl_opts, "skip_download": True}) as ydl:
        info = ydl.extract_info(url, download=False)
        titulo = limpar_nome(info.get("title", "download"))

    pasta_destino = get_downloads_dir() / f"{titulo}-{int(time.time())}"
    pasta_destino.mkdir(parents=True, exist_ok=True)

    format_option = "best[ext=mp4]/best" if tipo == "video" else "bestaudio/best"
    download_opts = {
        **ydl_opts,
        "format": format_option,
        "outtmpl": str(pasta_destino / "%(title)s.%(ext)s"),
    }

    with yt_dlp.YoutubeDL(download_opts) as ydl:
        ydl.download([url])

    arquivos = [p for p in pasta_destino.iterdir() if p.is_file()]
    if not arquivos:
        raise FileNotFoundError("O arquivo não foi gerado corretamente.")

    preferidos = [".mp4", ".m4a", ".webm", ".mp3", ".ogg", ".opus"]
    arquivo = next((p for p in arquivos if p.suffix.lower() in preferidos), arquivos[0])

    return str(arquivo)