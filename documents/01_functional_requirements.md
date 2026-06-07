# Requisitos Funcionais (RF) - Olist SRE Pipeline

Este documento detalha as funcionalidades necessárias para o pipeline de dados da Olist, focado na resposta à pergunta de negócio sobre receita líquida, sob as restrições do AWS Learner Lab.

## RF-01: Ingestão de Dados (Extração)
*   **Descrição:** O sistema deve extrair dados de fontes externas em formatos CSV e JSON (Northwind dataset).
*   **Requisito SRE:** A extração deve ser **idempotente**; re-execuções não devem duplicar dados na zona de pouso.
*   **Saída:** Arquivos brutos armazenados localmente na EC2 ou em bucket S3 (se disponível).

## RF-02: Processamento e Transformação (ETL)
*   **Descrição:** O sistema deve processar os dados brutos utilizando scripts Python (Pandas/Polars) para limpeza e cálculo.
*   **Regra de Negócio (Receita Líquida):** Calcular `Receita Líquida = Σ (UnitPrice × Quantity × (1 − Discount))` através do join de `Orders` e `Order_Details`.
*   **Agregações Necessárias:**
    1.  Ranking de Top 10 produtos por receita acumulada.
    2.  Série temporal de receita mensal por produto.
*   **Qualidade:** Remoção de nulos em campos críticos (`ProductID`, `OrderID`, `UnitPrice`) e normalização de datas.

## RF-03: Persistência Analítica (Carga)
*   **Descrição:** O sistema deve carregar os dados transformados em um banco Postgres organizado em um esquema analítico (ex: Star Schema ou tabelas de agregação).
*   **Saída:** Tabelas `dim_products`, `dim_time`, `fact_sales` ou uma View materializada para o dashboard.

## RF-04: Observabilidade e Auditoria do Pipeline
*   **Descrição:** O sistema deve registrar métricas de execução para cada estágio.
*   **Métricas de Auditoria (Reconciliação):**
    *   Contagem de linhas na origem vs. contagem de linhas inseridas no Postgres.
    *   Logs de início, fim e duração de cada etapa.
*   **Rastreabilidade:** Cada registro no Postgres deve conter um campo `load_timestamp` e `source_file`.

## RF-05: Dashboard de Inteligência de Negócio
*   **Descrição:** Visualização no Grafana que responda especificamente:
    1.  **Ranking:** Gráfico de barras com os 10 produtos de maior receita.
    2.  **Evolução:** Gráfico de linhas mostrando a evolução mensal da receita ao longo do período do dataset.
*   **Saúde:** Painel adicional com o status do último job (Sucesso/Erro) e Frescor do Dado (Tempo desde a última carga).

---
## Análise de Risco (RF)
1.  **Risco de Integridade:** Cálculos de desconto incorretos no script ETL podem gerar métricas de receita falsas.
2.  **Risco de Escalabilidade:** O dataset Northwind é pequeno, mas o código deve prever processamento em chunks para evitar estouro de memória na EC2.
3.  **Risco de Concorrência:** Múltiplas execuções simultâneas sem controle de trava (locking) podem corromper o estado do banco.

## Ambiguidades (RF)
1.  O tratamento de moedas diferentes (se houver no dataset) não foi especificado.
2.  A definição de "Mês" (data do pedido ou data de entrega) deve ser confirmada.
