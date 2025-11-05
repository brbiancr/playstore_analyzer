# 📱📊 PlayStore Analyzer

> Status: Finalizadodesenvolvimento

> Um projeto desenvolvido com foco em **análise de dados e visualização**, que tem como objetivo explorar e gerar insights a partir do **dataset da Google Play Store**, aplicando técnicas de limpeza, processamento e visualização de informações.
> 

Este projeto tem como objetivo **analisar dados de aplicativos da Google Play Store**, desde o pré-processamento até a criação de gráficos e indicadores relevantes. É voltado para iniciantes em **ciência de dados e análise exploratória**, utilizando **Python e a biblioteca Matplotlib**.

---

## 📝 Descrição do Desafio

O desafio consiste em processar um **arquivo de estatísticas da Google Play Store** e gerar **análises gráficas e métricas descritivas**.

As principais etapas incluem:

1. **Limpeza de dados**
    - Remover **linhas duplicadas** do dataset.
    - Tratar inconsistências e valores ausentes.
2. **Análises e métricas**
    - Exibir os **Top 5 aplicativos** por número de instalações.
    - Mostrar o **app mais caro** existente no dataset.
    - Identificar quantos apps são classificados como **"Mature 17+"**.
    - Exibir o **Top 10 apps por número de reviews**, em ordem decrescente.
    - Incluir **duas novas análises adicionais**, apresentando uma em formato de **lista** e outra em **valor agregado**.
3. **Visualizações**
    - Criar um **gráfico de barras** para os Top 5 apps por instalações.
    - Criar um **gráfico de pizza** para as categorias mais frequentes.
    - Desenvolver **duas visualizações adicionais** dos indicadores com a biblioteca **Matplotlib**.
4. **Resultados e insights**
    - Fornecer uma visão clara sobre os aplicativos mais populares, suas categorias e padrões de mercado.

---

## 🔍 Análise prevista

- Distribuição das categorias de aplicativos.
- Correlação entre número de reviews e número de instalações.
- Comparativo entre apps gratuitos e pagos.
- Identificação de tendências de mercado por tipo de app.
- Ranking dos aplicativos mais relevantes.

---

## 📊 Tecnologias Utilizadas

| Tecnologia | Finalidade |
| --- | --- |
| Python | Scripts de ingestão, processamento e análise |
| Pandas | Manipulação de limpeza dos dados |
| Jupyter notebook | ambiente de análise |
| Matplotlib | Para criação de gráficos e vizualização |

---

## 🗂 Estrutura do Projeto

```bash
Playlytics/
├── data/
│   ├── googleplaystore.csv     #Dados brutos
│   └── processed/      # Dados limpos
├── notebooks/
│   └── playlytics_analysis.ipynb
├── outputs/ #Graficos
├── scripts/ #Script de limpeza dos dados
└── README.md
```

---