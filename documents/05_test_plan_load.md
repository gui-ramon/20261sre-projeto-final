# Plano de Teste de Carga · Olist SRE Pipeline

Este plano detalha os cenários de teste para validar os requisitos de eficiência de desempenho (RNF-01) utilizando a ferramenta **k6**.

## Cenários de Teste

### TC-LOAD-01: Load Test (Carga Normal)
- **Hipótese:** O sistema processa um volume padrão de vendas sem degradação de latência.
- **Volume:** 10.000 registros.
- **Duração:** 10 minutos.
- **Métrica de Sucesso:** Tempo total de execução < 5 minutos (proporcional ao SLO do RNF-01).
- **RNF Coberto:** RNF-01.

### TC-LOAD-02: Soak Test (Carga de Longa Duração)
- **Hipótese:** Não há vazamentos de memória ou exaustão de créditos de CPU (t3.micro) durante operação contínua.
- **Volume:** Fluxo constante de 1.000 registros/hora.
- **Duração:** 4 horas (limite da sessão do Learner Lab).
- **Métrica de Sucesso:** Estabilidade no consumo de RAM da EC2 e 0 falhas por OOM.
- **RNF Coberto:** RNF-01, RNF-04.

### TC-LOAD-03: Spike Test (Pico Repentino)
- **Hipótese:** O sistema lida com um aumento súbito de arquivos na Landing Zone.
- **Volume:** 50.000 registros simultâneos.
- **Duração:** 2 minutos de pico.
- **Métrica de Sucesso:** O pipeline conclui o processamento sem corrupção de dados (RNF-02).
- **RNF Coberto:** RNF-01, RNF-02.

### TC-LOAD-04: Stress Test (Limite do Sistema)
- **Hipótese:** Identificar o ponto de ruptura da instância EC2 e do banco Postgres.
- **Volume:** Incremental até falha.
- **Duração:** 15 minutos.
- **Métrica de Sucesso:** Logs de erro capturados (RNF-04) antes da falha total do serviço.
- **RNF Coberto:** RNF-04.

---
## Ferramental
- **k6:** Scripts em JS para simulação de carga via API ou inserção direta (se aplicável).
- **CloudWatch:** Monitoramento de CPU/RAM/IOPS durante os testes.
