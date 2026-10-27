"""Reduz as fotos de fotos/ antes de publicar: no máximo 600 px no maior lado, em JPG.

Aceita JPG, PNG e WebP. Foto que muda de nome (argola.png → argola.jpg) tem o caminho
trocado no conteudo.json. Foto já leve (JPG até 600 px e até 200 KB) não é mexida, então
rodar de novo não muda nada. Transparência vira fundo branco, que é o fundo do card no app.
"""
import os
import sys

from PIL import Image, ImageOps

PASTA = "fotos"
LADO_MAXIMO = 600
TAMANHO_MAXIMO = 200 * 1024
EXTENSOES = {".jpg", ".jpeg", ".png", ".webp"}


def ja_leve(caminho):
    if os.path.splitext(caminho)[1].lower() != ".jpg":
        return False
    if os.path.getsize(caminho) > TAMANHO_MAXIMO:
        return False
    with Image.open(caminho) as imagem:
        return max(imagem.size) <= LADO_MAXIMO


def destino_livre(origem):
    base = os.path.splitext(origem)[0]
    destino = base + ".jpg"
    numero = 2
    # Não sobrescreve outra foto que já tenha o nome .jpg
    while destino != origem and os.path.exists(destino):
        destino = f"{base}-{numero}.jpg"
        numero += 1
    return destino


def otimizar(origem):
    with Image.open(origem) as aberta:
        imagem = ImageOps.exif_transpose(aberta)
        imagem.thumbnail((LADO_MAXIMO, LADO_MAXIMO))
        if imagem.mode in ("RGBA", "LA", "P"):
            imagem = imagem.convert("RGBA")
            fundo = Image.new("RGB", imagem.size, "white")
            fundo.paste(imagem, mask=imagem.split()[-1])
            imagem = fundo
        else:
            imagem = imagem.convert("RGB")
        destino = destino_livre(origem)
        for qualidade in (85, 75, 65):
            imagem.save(destino, "JPEG", quality=qualidade, optimize=True, progressive=True)
            if os.path.getsize(destino) <= TAMANHO_MAXIMO:
                break
    if destino != origem:
        os.remove(origem)
    return destino


def main():
    with open("conteudo.json", encoding="utf-8") as arquivo:
        texto = arquivo.read()
    mudou = False
    for nome in sorted(os.listdir(PASTA)):
        origem = os.path.join(PASTA, nome)
        if os.path.splitext(nome)[1].lower() not in EXTENSOES or ja_leve(origem):
            continue
        antes = os.path.getsize(origem)
        destino = otimizar(origem)
        print(f"{origem} ({antes // 1024} KB) → {destino} ({os.path.getsize(destino) // 1024} KB)")
        if destino != origem:
            texto = texto.replace(f'"/{origem}"', f'"/{destino}"')
        mudou = True
    if mudou:
        with open("conteudo.json", "w", encoding="utf-8") as arquivo:
            arquivo.write(texto)
    else:
        print("Fotos já otimizadas.")


if __name__ == "__main__":
    sys.exit(main())
