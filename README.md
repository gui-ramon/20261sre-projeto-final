# 🚀 Northwind SRE Pipeline - Projeto Final

Este repositório contém o projeto final da disciplina de SRE/Cloud Computing. O objetivo foi construir um pipeline de dados resiliente, escalável e monitorado para analisar a **Receita Líquida** do dataset Northwind.

## 📋 Visão Geral
O projeto implementa um stack moderno de dados (Modern Data Stack) focado em princípios SRE:
- **Ingestão:** Python (boto3) simulando ambiente S3 com **MinIO**.
- **Orquestração:** **Dagster** para gerenciamento de assets e linhagem.
- **Transformação:** **dbt** (Data Build Tool) rodando sobre **DuckDB**.
- **Visualização:** **Streamlit** (Dashboard de BI) e **Grafana** (Métricas).
- **Arquitetura:** Baseada no framework RM-ODP e táticas de Len Bass.

## 🏁 Como Ver os Resultados
Para que o professor possa avaliar o projeto rapidamente:
1.  **Guia Completo:** Acesse o [**FINAL_RESULTS_GUIDE.md**](./FINAL_RESULTS_GUIDE.md) para instruções de execução e links das ferramentas.
2.  **Documentação:** Toda a fundamentação teórica, requisitos (RF/RNF) e planos de teste estão na pasta [**documents/**](./documents/).
3.  **Análise de Dados:** O resultado do ranking "Top 10 Produtos" e a evolução mensal da receita podem ser vistos diretamente no código do modelo dbt ou rodando o dashboard Streamlit.

## 🛠️ Stack Tecnológico
- **Containers:** Docker & Docker Compose
- **Database:** DuckDB (OLAP de alta performance)
- **Dashboard:** Streamlit & Plotly
- **Orquestrador:** Dagster

## 👤 Autor
- **Gui Ramon**

---
*Este projeto foi desenvolvido seguindo as restrições do AWS Learner Lab, garantindo portabilidade e eficiência.*
