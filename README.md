# Monitor de Indicadores Epidemiológicos (SUS - PE)

Aplicação desenvolvida em Python para processamento e visualização de dados abertos de saúde pública do estado de Pernambuco.

## Sobre o Projeto

O projeto realiza a extração de dados públicos (DATASUS / SES-PE) e apresenta gráficos e métricas epidemiológicas, tais como:
- Média móvel de 7 dias de casos e óbitos
- Taxa de letalidade acumulada
- Comparativo entre estados do Nordeste
- Exportação dos dados filtrados em CSV

## Tecnologias Utilizadas

- Python
- Streamlit
- Pandas
- Plotly

## Como Executar

1. Instalar as dependências:
```bash
pip install streamlit pandas plotly

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
