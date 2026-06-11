# Guia de Acesso aos Resultados - Olist SRE Pipeline

Este documento resume como acessar todos os artefatos e resultados gerados no projeto.

## 1. Localização dos Artefatos
*   **Código Fonte:** Todo o código de ingestão (`ingest.py`), transformação (`dbt_northwind/`) e visualização (`app_dashboard.py`) está comitado no branch `main`.
*   **Documentação SRE:** A pasta `documents/` contém todo o ciclo de vida do projeto (Requisitos, Arquitetura, RTM e Planos de Teste).
*   **Banco de Dados Analítico:** O arquivo `dbt_northwind/northwind.duckdb` contém os dados processados e prontos para consulta.

## 2. Como Executar o Ambiente (Quick Start)
Para subir todos os serviços e visualizar os resultados, execute:
```bash
docker-compose up -d
```

## 3. URLs de Acesso Local
Após subir os containers, acesse as ferramentas via:
*   **Dashboard de BI (Streamlit):** `http://localhost:8501` (Exibe o Ranking Top 10 e Evolução Mensal).
*   **Orquestrador (Dagster):** `http://localhost:3000` (Monitoramento do pipeline).
*   **Storage (MinIO Console):** `http://localhost:9001` (Visualização dos arquivos brutos no S3 local).
*   **Grafana:** `http://localhost:3001` (Monitoramento de métricas).

## 4. Consulta Manual de Resultados (SQL)
Caso queira consultar os resultados diretamente no banco via Python/DuckDB:
```python
import duckdb
conn = duckdb.connect('dbt_northwind/northwind.duckdb')
print(conn.execute('SELECT * FROM top_10_products_revenue').df())
```

## 5. Status do Repositório Git
*   **Sincronização:** O código local está 100% sincronizado com o repositório remoto (`origin/main`).
*   **Última Versão:** `feat: implement Streamlit dashboard and complete BI stack (Step 06)`.

---
*Documento gerado em 11/06/2026 para garantir a persistência dos resultados.*
