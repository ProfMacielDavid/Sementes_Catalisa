# Projeto Sementes Catalisa 🌱

Este repositório contém os códigos, exemplos e documentação relacionados à reconstrução 3D de sementes nativas da Amazônia usando sensores LiDAR e técnicas de inteligência artificial.

## Estrutura do Projeto

```
Projeto_Sementes_Catalisa/
├── src/
│   └── reconstrucao_3d.py           # Script principal para reconstrução da malha 3D
├── data/
│   └── nuvem_semente_dummy.ply      # Exemplo de nuvem de pontos (.ply)
├── notebooks/
│   └── reconstrucao_3d_demo.ipynb   # Notebook de demonstração
├── docs/
│   └── Anexo_I_Codigos_Reconstrucao3D.txt
├── requirements.txt                 # Lista de bibliotecas necessárias
└── README.md                        # Este arquivo
```

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/ProfMacielDavid/Sementes_Catalisa.git
cd Sementes_Catalisa
```

2. Crie um ambiente virtual e ative:

```bash
python -m venv venv
venv\Scripts\activate    # Windows
source venv/bin/activate   # Linux/Mac
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Uso

### Executar via script

No terminal:

```bash
python src/reconstrucao_3d.py
```

> Altere o caminho para sua própria nuvem de pontos se desejar.

### Executar via notebook

Abra o Jupyter Notebook:

```bash
jupyter notebook notebooks/reconstrucao_3d_demo.ipynb
```

Siga as instruções dentro do notebook para gerar a malha 3D.

## Créditos

Instituto GEITEC / Projeto Catalisa ICT – Etapa 2  
Autor: David Lopes Maciel  
Contato: maciel.1000@hotmail.com

---

Desenvolvido para promover a inovação tecnológica na seleção de sementes nativas com base em inteligência artificial, LiDAR e espectroscopia hiperespectral.