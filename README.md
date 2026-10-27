# JA Studio 3D: conteúdo

Conteúdo que o app **JA Studio 3D** (iOS) busca ao abrir: os destaques da aba
Sobre, os dois banners da calculadora e os links de lojas e redes. Muda sem
publicar uma versão nova do app.

Publicado em: https://romulomotta.github.io/proj_input_calculadora3d/conteudo.json

## Como mudar (pelo formulário)

1. Abra https://app.pagescms.org e clique em **Sign in with GitHub**.
2. Escolha o repositório `proj_input_calculadora3d` → **Conteúdo do app**.
3. Mude o que quiser: em **Destaques**, cada produto tem **Nome**, **Link** e
   **Foto** (botão para enviar a imagem). **+ Add** cria um produto novo.
4. Clique em **Save**. Isso vira um commit e dispara a action **Publicar
   conteúdo**, que confere tudo e publica. Se ela falhar (❌ na aba
   **Actions** do GitHub), o app continua com a versão anterior; abra a
   execução para ver o que está errado.
5. A mudança chega ao app em alguns minutos (cache do GitHub Pages) e aparece
   ao reabrir o app.

Fotos: JPG, PNG ou WebP, de qualquer tamanho, de preferência quadradas. Ao
publicar, a action reduz para no máximo 600 px em JPG (até 200 KB) e troca o
caminho no `conteudo.json` se o nome mudar (`argola.png` → `argola.jpg`). Isso
vira um commit "reduz as fotos (automatico)": se o formulário estiver aberto,
recarregue a página antes de salvar de novo.

## Como mudar (direto no JSON)

Edite o `conteudo.json` pelo GitHub (lápis ✏️ → **Commit changes**). Fotos novas
vão em `fotos/`, e no JSON o `imagem` fica `/fotos/<arquivo>`. Para rodar a redução
localmente: `python3 scripts/otimizar_fotos.py` (precisa do Pillow). Para conferir
antes do commit: `python3 scripts/validar.py`.

## Formato

| Campo | O que é |
|---|---|
| `destaques` | Lista de produtos: `nome`, `link` (página da loja), `imagem` (`/fotos/<arquivo>` deste repositório ou link https externo) e, opcional, `preco` (texto, como `"R$ 89,90"`). Sem `preco`, o card mostra "Ver preço →" |
| `banner_materiais_1` | Banner acima de "Custos & Tempo": `texto` e `link` |
| `banner_materiais_2` | Banner acima de "Preço de Venda & Margem": `texto` e `link` |
| `links_redes` | Endereços dos botões `Shopee`, `ML`, `Amazon`, `TikTok`, `Instagram`; o que faltar fica com o endereço que está no app |


Tudo aqui é público: não coloque nada secreto.
