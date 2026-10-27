# JA Studio 3D: conteúdo

Conteúdo que o app **JA Studio 3D** (iOS) busca ao abrir: os destaques da aba
Sobre, os dois banners da calculadora e os links de lojas e redes. Muda sem
publicar uma versão nova do app.

Publicado em: https://romulomotta.github.io/proj_input_calculadora3d/conteudo.json

## Como mudar

1. Edite o `conteudo.json` (pelo site do GitHub serve: lápis ✏️ → **Commit changes**).
2. Fotos novas vão em `fotos/` (quadradas, cerca de 600 px, JPG, menos de 200 KB),
   e no JSON o `imagem` fica `https://romulomotta.github.io/proj_input_calculadora3d/fotos/<arquivo>`.
3. O commit dispara a action **Publicar conteúdo**: ela confere o JSON e publica.
   Se ela falhar (❌ na aba **Actions**), o app continua com a versão anterior;
   abra a execução para ver o que está errado.
4. A mudança chega ao app em alguns minutos (cache do GitHub Pages) e aparece ao reabrir o app.

## Formato

| Campo | O que é |
|---|---|
| `destaques` | Lista de produtos: `nome`, `link` (página da loja), `imagem` (link https da foto) e, opcional, `preco` (texto, como `"R$ 89,90"`). Sem `preco`, o card mostra "Ver preço →" |
| `banner_materiais_1` | Banner acima de "Custos & Tempo": `texto` e `link` |
| `banner_materiais_2` | Banner acima de "Preço de Venda & Margem": `texto` e `link` |
| `links_redes` | Endereços dos botões `Shopee`, `ML`, `Amazon`, `TikTok`, `Instagram`; o que faltar fica com o endereço que está no app |

Para conferir antes do commit: `python3 scripts/validar.py`.

Tudo aqui é público: não coloque nada secreto.
