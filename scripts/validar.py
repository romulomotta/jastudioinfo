"""Confere o conteudo.json antes de publicar. Sai com erro (e o Pages não publica) se algo estiver errado."""
import json
import os
import sys

BASE = "https://romulomotta.github.io/proj_input_calculadora3d/"
CHAVES_REDES = {"Shopee", "ML", "Amazon", "TikTok", "Instagram"}
erros = []


def https(valor, onde):
    if not isinstance(valor, str) or not valor.startswith("https://"):
        erros.append(f"{onde}: precisa ser um link https:// (veio {valor!r})")


def texto(valor, onde):
    if not isinstance(valor, str) or not valor.strip():
        erros.append(f"{onde}: precisa ser um texto não vazio")


try:
    with open("conteudo.json", encoding="utf-8") as arquivo:
        conteudo = json.load(arquivo)
except json.JSONDecodeError as erro:
    sys.exit(f"conteudo.json não é um JSON válido: linha {erro.lineno}, coluna {erro.colno}: {erro.msg}")

destaques = conteudo.get("destaques")
if not isinstance(destaques, list) or not destaques:
    erros.append("destaques: precisa ser uma lista com pelo menos um produto")
else:
    for i, destaque in enumerate(destaques, 1):
        onde = f"destaques[{i}]"
        if not isinstance(destaque, dict):
            erros.append(f"{onde}: precisa ser um objeto {{ }}")
            continue
        texto(destaque.get("nome"), f"{onde}.nome")
        https(destaque.get("link"), f"{onde}.link")
        imagem = destaque.get("imagem")
        https(imagem, f"{onde}.imagem")
        # Foto deste repositório: o arquivo tem de existir em fotos/
        if isinstance(imagem, str) and imagem.startswith(BASE):
            caminho = imagem[len(BASE):]
            if not os.path.isfile(caminho):
                erros.append(f"{onde}.imagem: o arquivo {caminho} não existe no repositório")
        if "preco" in destaque and not isinstance(destaque["preco"], str):
            erros.append(f"{onde}.preco: se existir, precisa ser texto, como \"R$ 89,90\"")

for chave in ("banner_materiais_1", "banner_materiais_2"):
    banner = conteudo.get(chave)
    if not isinstance(banner, dict):
        erros.append(f"{chave}: precisa ser um objeto com texto e link")
        continue
    texto(banner.get("texto"), f"{chave}.texto")
    https(banner.get("link"), f"{chave}.link")

redes = conteudo.get("links_redes")
if not isinstance(redes, dict):
    erros.append("links_redes: precisa ser um objeto { \"Nome\": \"link\" }")
else:
    for nome, link in redes.items():
        if nome not in CHAVES_REDES:
            erros.append(f"links_redes.{nome}: nome desconhecido; use {sorted(CHAVES_REDES)}")
        https(link, f"links_redes.{nome}")

if erros:
    print("conteudo.json tem problemas:")
    for erro in erros:
        print(f"  - {erro}")
    sys.exit(1)
print(f"conteudo.json ok: {len(destaques)} destaques, 2 banners, {len(redes)} links")
