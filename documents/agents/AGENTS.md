# AGENTS.md · olist-sre-pipeline

## Contexto
Pipeline de dados Olist em AWS Academy Learner Lab (us-east-1).
ETL Python -> Postgres -> Grafana. SRE-first.

## Restrições duras
- **Serviços Proibidos:** Sem Glue, Redshift, SageMaker (Learner Lab não habilita).
- **Segurança:** Sem secrets em código. Tudo via SSM Parameter Store.
- **Modo de Operação:** Sem provisionar nada nesta aula. Apenas Markdown e Mermaid.

## Saída esperada
- **Formatação:** Markdown válido com cabeçalhos hierárquicos.
- **Rastreabilidade:** IDs estáveis: RF-NN, RNF-NN, TC-NN, ADR-NN.
- **Métricas:** RNF mensurável (valor, unidade, janela, fonte).
- **Fechamento:** Premissas e questões em aberto ao final de cada documento.

## Comportamento
- **Auto-crítica:** Critique sua saída antes de entregar.
- **Análise de Risco:** Liste 3 riscos e 2 ambiguidades por arquivo.
- **Especialização:** Use as skills em `documents/agents/skills/`.
- **Fidelidade AWS:** Não invente nomes de serviço AWS. Use apenas serviços reais e disponíveis no Learner Lab.
