# 🛍️ Data App de Controle de Estoque, Precificação e PDV — XZ Variedades

Este repositório contém uma aplicação interativa em Python e Streamlit desenvolvida para automatizar a gestão de estoque, controle de custos com rateio proporcional de frete, precificação dinâmica e baixas de vendas (PDV) para a loja **XZ Variedades**.

🔗 **Acesse o aplicativo rodando online:** [XZ Variedades - Streamlit Cloud](https://app-controle-de-sell-in-out.streamlit.app/)

---

# 🚀 Funcionalidades Principais

- 📥 **Importação Inteligente de Pedidos (CSV):** Leitura de notas e listas de fornecedores com normalização automática de nomes de produtos (limpeza de acentos, caracteres especiais e numerais no início do texto para evitar duplicidades).
- 🚚 **Rateio Proporcional de Frete:** Cálculo e distribuição automática do valor do frete por unidade com base na representatividade do valor total do item na nota.
- 🏷️ **Geração Dinâmica de SKUs:** Atribuição de identificadores únicos sequenciais (`XZ-001`, `XZ-002`, etc.) e recálculo automático pelo **Custo Médio Ponderado** em compras recorrentes.
- 📊 **Tabela Reativa de Margens e Preços:** Edição de preços de venda diretamente na interface gráfica via `st.data_editor` e `st.session_state`, com recálculo instantâneo da **% de Margem de Lucro**.
- 🛒 **Módulo PDV (Baixa Rápida):** Interface para registro manual de vendas com consulta dinâmica de estoque e persistência em histórico detalhado (data/hora, quantidade e lucro obtido).
- 📈 **Dashboard de KPIs:** Acompanhamento em tempo real do faturamento/lucro realizado versus as projeções financeiras caso o estoque atual seja totalmente vendido.

---

# 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python
- **Manipulação & Análise de Dados:** Pandas
- **Interface & Dashboard Interativo:** Streamlit & Streamlit Cloud
- **Interface/Suporte a Expressões Regulares:** `re` & `unicodedata`
- **Ambiente de Prototipagem:** Google Colab

---

# 📂 Estrutura do Repositório

```text
├── APP.py              # Código-fonte principal da aplicação Streamlit
├── Requirements.txt    # Dependências do projeto (streamlit, pandas)
├── estoque.csv         # Arquivo local de persistência do estoque (gerado automaticamente)
├── vendas.csv          # Arquivo local de histórico de vendas (gerado automaticamente)
└── README.md           # Documentação do projeto

# 🔧 Como Executar o Projeto Localmente

Clone este repositório: git clone [https://github.com/HugoFigueira-Dados/Controle-de-Sell-In-Out.git](https://github.com/HugoFigueira-Dados/Controle-de-Sell-In-Out.git)
cd Controle-de-Sell-In-Out
Instale as dependências:pip install -r Requirements.txt
Execute a aplicação Streamlit:Execute a aplicação Streamlit:
