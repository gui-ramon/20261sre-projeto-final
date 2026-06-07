# Plano de Teste de Modelagem (ATAM) · Olist SRE Pipeline

Este documento aplica uma versão enxuta do método **ATAM (Architecture Analysis Method)** sobre a arquitetura do projeto.

## 1. Utility Tree
Priorização baseada nos cenários de RNF.

| Atributo | Cenário | Prioridade |
|---|---|---|
| Desempenho | Processar 100k registros em < 30min (RNF-01) | Alta |
| Segurança | 100% dos segredos via SSM (RNF-03) | Alta |
| Confiabilidade | Recuperação de carga após falha (RTO < 2h) | Média |

## 2. Análise de Cenários ATAM

### Cenário: Carga de Pico no ETL (RNF-01)
- **Risco:** A instância t3.micro pode não ter memória suficiente (RAM) para o Pandas processar o volume.
- **Sensibilidade:** O desempenho é altamente sensível ao tamanho dos "chunks" de leitura do arquivo.
- **Trade-off:** Aumento da complexidade do código (processamento em partes) para ganhar eficiência de memória.

### Cenário: Gestão de Segredos via SSM (RNF-03)
- **Risco:** Latência adicional no startup do script ao buscar múltiplos parâmetros no SSM.
- **Sensibilidade:** A segurança depende integralmente da política IAM aplicada à EC2.
- **Trade-off:** Segurança (cumprimento do RNF) em troca de uma dependência externa obrigatória da AWS.

### Cenário: Observabilidade via CloudWatch (RNF-04)
- **Risco:** Throttling na API do CloudWatch se o script gerar logs em excesso.
- **Sensibilidade:** A capacidade de diagnóstico depende da verbosidade correta do log.
- **Trade-off:** Custo de armazenamento/ingestão de logs vs. facilidade de diagnóstico.

---
## 3. Conclusões de Modelagem
A arquitetura é resiliente para o escopo do Learner Lab, mas possui pontos de estrangulamento claros em relação aos limites de recursos da AWS Academy (instâncias micro e IOPS).
