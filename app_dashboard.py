import streamlit as st
import duckdb
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="Northwind Sales Dashboard", layout="wide")

st.title("📊 Northwind Sales Intelligence Dashboard")
st.markdown("### Análise de Receita Líquida - Top 10 Produtos")

# Caminho para o banco DuckDB
DB_PATH = "dbt_northwind/northwind.duckdb"

@st.cache_data
def load_data():
    if not os.path.exists(DB_PATH):
        st.error(f"Arquivo de banco de dados não encontrado em {DB_PATH}. Certifique-se de que o dbt run foi executado.")
        return None
    
    conn = duckdb.connect(DB_PATH, read_only=True)
    query = "SELECT * FROM top_10_products_revenue"
    df = conn.execute(query).df()
    conn.close()
    return df

df = load_data()

if df is not None:
    # Sidebar para filtros
    st.sidebar.header("Filtros")
    products = st.sidebar.multiselect("Selecione os Produtos (IDs):", options=df['product_id'].unique(), default=df['product_id'].unique())
    
    filtered_df = df[df['product_id'].isin(products)]

    # Layout de colunas
    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("Ranking: Top 10 Produtos por Receita Total")
        # Agregando para o gráfico de barras (Ranking Total)
        ranking_df = filtered_df.groupby('product_id')['total_net_revenue'].first().reset_index()
        ranking_df = ranking_df.sort_values('total_net_revenue', ascending=False)
        
        fig_bar = px.bar(
            ranking_df, 
            x='product_id', 
            y='total_net_revenue',
            labels={'product_id': 'ID do Produto', 'total_net_revenue': 'Receita Líquida Total'},
            color='total_net_revenue',
            color_continuous_scale='Viridis'
        )
        st.plotly_chart(fig_bar, use_container_width=True)

    with col2:
        st.subheader("Evolução Mensal da Receita")
        # Ordenando por mês para o gráfico de linha
        evolution_df = filtered_df.sort_values('month_year')
        
        fig_line = px.line(
            evolution_df, 
            x='month_year', 
            y='monthly_net_revenue', 
            color='product_id',
            labels={'month_year': 'Mês-Ano', 'monthly_net_revenue': 'Receita Mensal', 'product_id': 'Produto'},
            markers=True
        )
        st.plotly_chart(fig_line, use_container_width=True)

    # Tabela de Dados
    st.subheader("Dados Detalhados")
    st.dataframe(filtered_df.sort_values(['total_net_revenue', 'month_year'], ascending=[False, True]), use_container_width=True)

    st.info("💡 Nota: Os nomes dos produtos não estão disponíveis no dataset atual. Para incluí-los, adicione 'northwind_products.csv' ao pipeline.")
else:
    st.warning("Aguardando processamento de dados...")
