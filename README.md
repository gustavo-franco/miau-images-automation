# 🐾 MIAU IMAGENS - Automação de Assets com IA

Este repositório faz parte do ecossistema do aplicativo **MIAU**, focado em produtividade e bem-estar. Aqui documentamos o pipeline de criação e processamento dos ícones do sistema.

## 🔴 O Problema
Durante a criação da interface do aplicativo, enfrentamos dois desafios principais:
1. **Consistência Visual:** Gerar 50 ícones distintos que mantivessem o mesmo estilo de traço, cores e personagem (Gatinha Tabby).
2. **O "Falso Transparente":** Modelos de geração de imagem por IA frequentemente entregam o padrão quadriculado (xadrez) como parte da imagem, em vez de um canal alfa (transparência real), o que impossibilita a sobreposição direta na UI do app.

## 🟢 A Solução (Pipeline Técnico)
Desenvolvemos um fluxo de trabalho em duas etapas:

1. **Geração (Prompt Engineering):** Utilização do Google Gemini/Imagen 3 com prompts técnicos estruturados para garantir o estilo "Sticker 2D" e isolamento do objeto.
2. **Processamento (Python + IA de Segmentação):** Criação de um script Python utilizando a biblioteca `rembg` (baseada na arquitetura U2-Net) para remover automaticamente o fundo xadrez e gerar arquivos `.png` com transparência real via processamento de CPU/GPU.

## 🛠️ Tecnologias Utilizadas
- **Python 3.13**
- **Pillow** (Processamento de imagem)
- **rembg[cpu]** (Remoção de fundo baseada em Deep Learning)
- **Google Gemini API** (Geração de assets)

## Scripts
/
- **├── scripts/
- **│   └── removedor-de-fundo-img.py    # O código que você rodou
- **├── requirements.txt                # Lista das bibliotecas (rembg, pillow)
- **├── .gitignore                      # Para NÃO subir a pasta 'icon' com 1GB de imagens
- **└── README.md                       # A documentação que te mandei
