# Plano de Teste de Segurança · Olist SRE Pipeline

Análise de segurança baseada na metodologia STRIDE e conformidade OWASP Top 10 para o pipeline Olist.

## 1. Análise STRIDE por Componente

| Componente | S (Spoofing) | T (Tampering) | R (Repudiation) | I (Info Disc.) | D (DoS) | E (Elev. Priv.) |
|---|---|---|---|---|---|---|
| EC2 ETL | IAM Roles p/ evitar spoofing | Scripts assinados | Logs CloudWatch | SSM p/ segredos | Limite de conexões | IAM restrito |
| RDS Postgres | Autenticação IAM | Permissões SQL | Audit logs | Criptografia repouso | Security Groups | Roles de banco |
| SSM | Políticas IAM | Versionamento | Logs CloudTrail | SecureString | Throttling AWS | Restrição de Path |

## 2. OWASP Top 10 Aplicáveis
- **A01:2021-Broken Access Control:** Falha nas políticas IAM do Learner Lab.
- **A03:2021-Injection:** SQL Injection na carga do Postgres (Loader Service).
- **A07:2021-Identification and Authentication Failures:** Uso de senhas fracas ou segredos expostos.

## 3. Casos de Teste de Segurança (TC-SEC)

| ID | Tipo | Ferramenta | Objetivo |
|---|---|---|---|
| TC-SEC-01 | SAST | Bandit | Scan estático do código Python em busca de vulnerabilidades. |
| TC-SEC-02 | SCA | Trivy | Scan de dependências (requirements.txt) para CVEs conhecidas. |
| TC-SEC-03 | DAST | OWASP ZAP | Scan de segurança básico no endpoint do Grafana. |
| TC-SEC-04 | Secret Scan | Gitleaks | Verificar se segredos foram commitados no repositório. |
| TC-SEC-05 | Posture | Prowler | Validar conformidade das configurações AWS (Learner Lab). |

---
## Restrições de Execução
- Testes DAST (TC-SEC-03) devem ser realizados com cautela para não violar as políticas de uso da AWS Academy.
