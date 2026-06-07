# Matriz de Rastreabilidade de Requisitos (RTM) · Olist SRE Pipeline

| Req | Tipo | Origem | Componente | Caso de Teste | Status |
|---|---|---|---|---|---|
| RF-01 | Funcional | spec/00_problem.md | Extractor Module | TC-LOAD-01 | Coberto |
| RF-02 | Funcional | spec/00_problem.md | Transformer Engine | TC-LOAD-03 | Coberto |
| RF-03 | Funcional | spec/00_problem.md | Loader Service | TC-SEC-01 (Bandit) | Coberto |
| RF-04 | Funcional | spec/00_problem.md | Health Monitor | TC-LOAD-04 | Coberto |
| RF-05 | Funcional | spec/00_problem.md | Grafana | TC-SEC-03 (ZAP) | Coberto |
| RNF-01 | Não Funcional | ISO 25010 | EC2 ETL | TC-LOAD-01 | Coberto |
| RNF-02 | Não Funcional | ISO 25010 | RDS/Postgres | TC-LOAD-03 | Coberto |
| RNF-03 | Não Funcional | ISO 25010 | SSM | TC-SEC-04 (Gitleaks) | Coberto |
| RNF-04 | Não Funcional | ISO 25010 | CloudWatch | TC-LOAD-04 | Coberto |
| RNF-05 | Não Funcional | ISO 25010 | EC2 ETL | TC-SEC-02 (Trivy) | Coberto |

---

## Resumo de Cobertura
- **Requisitos Totais:** 10
- **Requisitos Cobertos (Componente + Teste definido):** 10
- **Requisitos Abertos:** 0

---

## Análise de Risco (RTM)
1. **Risco de Falsos Positivos:** Testes automatizados (SAST/SCA) podem ignorar vulnerabilidades lógicas.
2. **Risco de Custo de Teste:** Testes de estresse (TC-LOAD-04) podem consumir os 100 dólares do Learner Lab se não monitorados.
3. **Risco de Fidelidade:** Os cenários de ATAM são qualitativos e dependem da implementação correta do código.

## Ambiguidades (RTM)
1. A frequência de execução do Prowler (TC-SEC-05) no ambiente restrito.
2. Definição exata de "falha" para o teste de estresse.
