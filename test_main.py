from pathlib import Path

from main import gerar_caminho_download


def test_gerar_caminho_download_cria_arquivo_em_downloads():
    caminho = gerar_caminho_download("Vídeo Teste: 01/02", "video")

    assert caminho.endswith(".mp4")
    assert Path(caminho).parent.name == "downloads"
    assert Path(caminho).exists() is False
