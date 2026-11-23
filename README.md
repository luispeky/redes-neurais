# Comparação de Arquiteturas de MLP para Diagnóstico de Câncer de Mama

Projeto da disciplina de Redes Neurais Artificiais. Treina e compara redes MLP (Perceptron de Múltiplas Camadas) para classificar tumores de mama como **malignos** ou **benignos**, usando o dataset [Breast Cancer Wisconsin (Diagnostic)](https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic) do UCI Machine Learning Repository.

## Pergunta de pesquisa

Como a quantidade de camadas ocultas e de neurônios influencia o desempenho de uma MLP na classificação de tumores mamários? A rede mais complexa supera a mais simples, ou ocorre overfitting?

## Dataset

- 569 amostras (357 benignas e 212 malignas) e 30 atributos numéricos.
- Os atributos descrevem os núcleos celulares: raio, textura, perímetro, área, suavidade, compacidade, concavidade, pontos côncavos, simetria e dimensão fractal. Cada um aparece como média (sufixo `1`), erro padrão (`2`) e pior valor (`3`).
- Alvo: `Diagnosis`, com `M` (maligno, codificado como 1) e `B` (benigno, codificado como 0).
- Descrição original em `data/wdbc.names`.

## Estrutura do projeto

```
projeto-redes-neurais/
├── artigo/
│   └── template_artigo_IEEE.tex    # Template do artigo (IEEEtran, para Overleaf, máx. 3 páginas)
├── data/
│   ├── wdbc.data                   # Dados originais (CSV sem cabeçalho)
│   ├── wdbc.names                  # Documentação do dataset
│   └── wdbc.xlsx                   # Dados com cabeçalho, usados no notebook
├── notebooks/
│   └── experimento.ipynb           # Pré-processamento, treino e avaliação das MLPs
├── src/
│   ├── gerar_excel.py              # Converte wdbc.data em wdbc.xlsx com nomes de colunas
│   └── verificar_integridade.py    # Confere dimensões, nulos, duplicados e tipos
└── README.md
```

## Metodologia

**Pré-processamento**
1. Separação de atributos (X) e alvo (y).
2. Divisão em 80% treino e 20% teste, estratificada e com `random_state=42`.
3. Padronização com `StandardScaler`, ajustado apenas nos dados de treino para evitar data leakage.

**Modelos** (`MLPClassifier` do scikit-learn)

| Modelo | Camadas ocultas |
|---|---|
| `MLP_Simples` | (16,) |
| `MLP_Intermediaria` | (32, 16) |
| `MLP_Profunda` | (64, 32, 16) |

Os três usam os mesmos hiperparâmetros: ativação `relu`, otimizador `adam`, `alpha=0.0001`, `max_iter=1000` e `random_state=42`.

**Avaliação** no conjunto de teste: acurácia, precisão, recall, F1-score, ROC-AUC e matriz de confusão. A classe positiva é maligno.

## Como executar

Requisitos: Python 3 com `pandas`, `openpyxl`, `scikit-learn` e `jupyter`.

```bash
pip install pandas openpyxl scikit-learn jupyter
```

1. (Opcional) Gerar o Excel a partir dos dados originais: `python src/gerar_excel.py`. O arquivo `wdbc.xlsx` é salvo no diretório atual, então mova-o para `data/` se quiser substituir o existente.
2. (Opcional) Verificar a integridade dos dados: `python src/verificar_integridade.py`. O esperado é shape `(569, 32)`, sem nulos e sem IDs duplicados.
3. Abrir `notebooks/experimento.ipynb` e executar as células em ordem.

> Os scripts e o notebook usam o caminho absoluto `C:/Users/usuario/projeto-redes-neurais/data/...`. Ajuste-o se o projeto estiver em outro local.

## Artigo

O arquivo `artigo/template_artigo_IEEE.tex` é um template no formato IEEE para ser usado no Overleaf. Nele entram os resultados do experimento, incluindo as figuras de matriz de confusão e curva ROC.

## Fonte dos dados

Wolberg, W. H., Street, W. N., Mangasarian, O. L. *Breast Cancer Wisconsin (Diagnostic)*. UCI Machine Learning Repository.
