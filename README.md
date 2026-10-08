```markdown
# 🏥 Monitor de Indicadores Epidemiológicos - SUS / PE

Aplicação interativa desenvolvida em Python para ingestão, tratamento, processamento de métricas epidemiológicas e visualização de dados abertos de saúde pública do estado de Pernambuco.

O projeto conecta-se a bases públicas alinhadas ao **OpenDataSUS** e às diretrizes de **Saúde Digital**, automatizando a análise temporal de agravos à saúde pública e oferecendo suporte à visualização de dados para gestão e pesquisa.

---

## 🎯 Funcionalidades Principais

- **Ingestão Automatizada de Dados:** Consumo e estruturação de dados públicos de saúde via pipeline HTTP/REST.
- **Engenharia de Métricas Epidemiológicas:**
  - Cálculo de **Média Móvel de 7 dias** para suavização estatística de variações diárias.
  - Cálculo contínuo da **Taxa de Letalidade (%)**.
  - Consolidação de casos e óbitos acumulados.
- **Visualização Interativa:**
  - Gráficos dinâmicos de barras e séries temporais com suporte a zoom e *hover*.
  - Análise comparativa da distribuição acumulada entre estados do **Nordeste**.
  - Filtro temporal configurável via menu lateral.
- **Exportação de Dados:** Módulo integrado para geração e download do dataset tratado em formato `.csv`.

---

## 🛠️ Stack Tecnológica

| Componente | Tecnologia | Uso |
| :--- | :--- | :--- |
| **Linguagem** | Python 3.10+ | Lógica de processamento e manipulação de dados |
| **Interface Web** | Streamlit | Construção do dashboard e componentes interativos |
| **Manipulação de Dados** | Pandas | Limpeza, transformação e geração de séries temporais |
| **Visualização** | Plotly (Express / Graph Objects) | Rendimento dos gráficos dinâmicos e interativos |

---

## 🚀 Como Executar o Projeto Localmente

### Pré-requisitos
- Python 3.10 ou superior instalado.

### Passo a Passo

1. **Clonar o repositório:**
   ```bash
   git clone [https://github.com/SEU_USUARIO/monitor-sus-pe.git](https://github.com/SEU_USUARIO/monitor-sus-pe.git)
   cd monitor-sus-pe

```

2. **Instalar as dependências:**
```bash
pip install streamlit pandas plotly

```


3. **Executar a aplicação:**
```bash
streamlit run app.py

```


4. Acesse no navegador o endereço indicado no terminal (geralmente `http://localhost:8501`).

---

## 📂 Estrutura do Repositório

```text
monitor-sus-pe/
├── app.py           # Código fonte principal da aplicação Streamlit
├── README.md        # Documentação do projeto

```

---

## 📄 Fonte dos Dados

Os dados utilizados nesta aplicação são extraídos de repositórios públicos e unificados que compilam boletins oficiais do **DATASUS** e da **Secretaria Estadual de Saúde de Pernambuco (SES-PE)**.

---

## 👤 Autor

Desenvolvido por **Anderson Cabral Silva Júnior**

Estudante de Sistemas de Informação — **Centro de Informática (CIn / UFPE)**

```

```
