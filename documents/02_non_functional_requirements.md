# Requisitos Não Funcionais (RNF) - Olist SRE Pipeline

Este documento estabelece os critérios de qualidade e metas de confiabilidade (SRE) baseados na ISO/IEC 25010 (Qualidade de Produto) e ISO/IEC 25012 (Qualidade de Dados).

## 1. Confiabilidade e Resiliência (SRE Principles)
*   **RNF-01 (Idempotência):** O pipeline deve permitir re-execuções sem causar duplicidade de dados ou estados inconsistentes.
    *   **SLI:** Taxa de duplicidade no banco após re-execução.
    *   **SLO:** 0% de registros duplicados.
*   **RNF-02 (Retentativa):** O script de carga deve possuir lógica de *retry* exponencial para falhas temporárias de conexão com o Postgres.

## 2. Eficiência de Desempenho e Frescor (Performance)
*   **RNF-03 (Data Freshness):** O intervalo entre a chegada do dado na origem e sua disponibilidade no dashboard deve ser minimizado.
    *   **SLI:** Tempo decorrido desde o `max(OrderDate)` na origem até o `max(OrderDate)` no dashboard.
    *   **SLO:** < 1 hora (considerando execução agendada).

## 3. Qualidade de Dados (ISO 25012)
*   **RNF-04 (Exatidão e Completude):** O total de receita calculado pelo pipeline deve bater com a soma dos arquivos brutos.
    *   **SLI:** Diferença percentual entre `SUM(Revenue)` no CSV vs `SUM(Revenue)` no Postgres.
    *   **SLO:** 0% de discrepância (Precisão total).
*   **RNF-05 (Consistência):** Todos os `ProductID` na tabela de vendas devem existir na tabela de produtos (Integridade Referencial).

## 4. Segurança e Governança
*   **RNF-06 (Segurança de Segredos):** Uso obrigatório do AWS SSM Parameter Store ou Variáveis de Ambiente protegidas.
    *   **SLO:** Zero senhas "hardcoded" no repositório GitHub.
*   **RNF-07 (Princípio do Menor Privilégio):** O usuário do banco de dados usado pelo ETL deve ter apenas permissões de `INSERT/SELECT/UPDATE`, sem privilégios de `DROP` ou `ADMIN`.

## 5. Observabilidade (Golden Signals)
*   **RNF-08 (Monitoramento de Saúde):** O pipeline deve expor métricas de sucesso e latência.
    *   **SLI:** Percentual de jobs bem sucedidos.
    *   **SLO:** > 95% de sucesso semanal.
    *   **SLI:** Tempo de execução do ETL.
    *   **SLO:** < 10 minutos para o dataset padrão.

## Tabela de SLIs/SLOs Consolidada

| Categoria | ID | SLI | SLO | Fonte de Dados |
|---|---|---|---|---|
| Confiabilidade | RNF-01 | Taxa de Duplicidade | 0% | Postgres (Unique Constraints) |
| Performance | RNF-03 | Data Freshness | < 1 hora | Dashboard Time Metrics |
| Qualidade | RNF-04 | Reconciliação Financeira | 0% de erro | Logs de Auditoria |
| Segurança | RNF-06 | Secrets no Código | 0 | Scan de Segurança (Gitleaks) |
| Observabilidade| RNF-08 | Job Success Rate | > 95% | CloudWatch Metrics |

---
## Análise de Risco (RNF)
1.  **Risco de Quota AWS:** O monitoramento detalhado pode gerar excesso de logs, esgotando o armazenamento da EC2.
2.  **Risco de Disponibilidade:** Como o RDS é caro para o Learner Lab, rodar o Postgres na EC2 aumenta o risco de perda de dados se a instância for terminada sem snapshot.
