import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Monitor SUS PE", layout="wide")

st.title("Monitor de Indicadores Epidemiológicos - SUS / PE")
st.caption("Análise de dados abertos de saúde pública (SES-PE / DATASUS)")

@st.cache_data
def carregar_dados():
    url = "https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv"
    df = pd.read_csv(url)
    df['date'] = pd.to_datetime(df['date'])
    return df

df_raw = carregar_dados()

df_pe = df_raw[df_raw['state'] == 'PE'].copy().sort_values('date')
df_pe['mm_casos'] = df_pe['newCases'].rolling(window=7).mean()
df_pe['mm_obitos'] = df_pe['newDeaths'].rolling(window=7).mean()
df_pe['letalidade'] = (df_pe['deaths'] / df_pe['totalCases']) * 100

st.sidebar.header("Filtros")
min_date = df_pe['date'].min().to_pydatetime()
max_date = df_pe['date'].max().to_pydatetime()

date_range = st.sidebar.date_input(
    "Período",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

if len(date_range) == 2:
    start_d, end_d = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])
    df_filtrado = df_pe[(df_pe['date'] >= start_d) & (df_pe['date'] <= end_d)]
else:
    df_filtrado = df_pe

ultima_linha = df_filtrado.iloc[-1] if not df_filtrado.empty else df_pe.iloc[-1]

k1, k2, k3, k4 = st.columns(4)
k1.metric("Casos Confirmados", f"{int(ultima_linha['totalCases']):,}".replace(",", "."))
k2.metric("Óbitos Acumulados", f"{int(ultima_linha['deaths']):,}".replace(",", "."))
k3.metric("Taxa de Letalidade", f"{ultima_linha['letalidade']:.2f}%")
k4.metric("Média Móvel (7d)", f"{int(ultima_linha['mm_casos'] if pd.notna(ultima_linha['mm_casos']) else 0)}")

st.divider()

tab1, tab2, tab3 = st.tabs(["Série Temporal", "Comparativo Nordeste", "Dados (CSV)"])

with tab1:
    fig = go.Figure()
    fig.add_trace(go.Bar(x=df_filtrado['date'], y=df_filtrado['newCases'], name="Casos Diários", marker_color='#cbd5e1'))
    fig.add_trace(go.Scatter(x=df_filtrado['date'], y=df_filtrado['mm_casos'], name="Média Móvel (7d)", line=dict(color='#e74c3c', width=3)))
    fig.update_layout(template="plotly_white", xaxis_title="Data", yaxis_title="Casos", hovermode="x unified")
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    estados_ne = ['PE', 'BA', 'CE', 'MA', 'PB', 'PI', 'RN', 'SE', 'AL']
    df_ne = df_raw[df_raw['state'].isin(estados_ne)].groupby('state').last().reset_index().sort_values('totalCases', ascending=False)
    
    fig_ne = px.bar(df_ne, x='state', y='totalCases', color='totalCases', 
                   labels={'state': 'Estado', 'totalCases': 'Total de Casos'},
                   color_continuous_scale='Reds', text_auto='.2s')
    fig_ne.update_layout(template="plotly_white")
    st.plotly_chart(fig_ne, use_container_width=True)

with tab3:
    colunas_exibir = ['date', 'state', 'totalCases', 'newCases', 'deaths', 'newDeaths', 'mm_casos', 'letalidade']
    st.dataframe(df_filtrado[colunas_exibir], use_container_width=True)
    
    csv = df_filtrado[colunas_exibir].to_csv(index=False).encode('utf-8')
    st.download_button("Baixar Dados (CSV)", data=csv, file_name="dados_saude_pe.csv", mime="text/csv")
