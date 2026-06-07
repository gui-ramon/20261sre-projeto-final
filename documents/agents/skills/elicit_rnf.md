# Skill: Elicitar Requisitos Não Funcionais (RNF)

## Quando usar
Quando o usuário pedir RNFs e já existir `spec/00_problem.md` e/ou `documents/01_functional_requirements.md`.

## Entrada
- `spec/00_problem.md` (obrigatório)
- `documents/01_functional_requirements.md` (opcional)

## Passos
1. Ler stakeholders e fluxos críticos do problema.
2. Mapear cada fluxo aos 8 atributos da ISO 25010.
3. Para cada atributo, propor 1 a 3 RNFs com SLI mensurável.
4. Marcar prioridade MoSCoW.
5. Listar premissas e fontes de medição.

## Saída
Arquivo `documents/02_non_functional_requirements.md` com:
- Seção por atributo ISO 25010.
- IDs RNF-NN únicos.
- Tabela final com (ID, atributo, SLI, SLO, fonte, prioridade).

## Critérios de aceitação
- 8 atributos cobertos.
- Todo RNF tem unidade e janela.
- Nenhum RNF aspiracional ("ser confiável" é proibido).
- Segue estritamente as restrições em `documents/agents/AGENTS.md`.
