# 🛡️ Projeto Quimera: Arquitetura de Defesa E-Learning & Cloud

O **Projeto Quimera** é um ecossistema backend contruído sob a égide da **Clean Architecture** (Arquitetura Limpa), projetado primordialmente como uma fortaleza de *Blue Team*. O objetivo da aplicação é prover resiliência, validação de integridade e auditoria agressiva contra métodos avançados de fraude, *Scraping* acadêmico, e abuso de benefícios *Cloud* (Exploitation de Autograders e Vouchers).

A infraestrutura foi construída como resposta de mapeamento de Threat Intelligence às operações de um Agente Ofensivo Automatizado (apelidado de "Alex/Motor B92"), encarregado de dizimar barreiras de exames práticos, extrair laboratórios na nuvem e burlar esteiras de testes.

---

## 🏛️ Filosofia Arquitetural (Clean Architecture)
A fundação do Quimera é modular. Todas as regras de fraude residem na **Application/Domain Layer**, independentes de framework (FastAPI) e abstraídas através de Protocolos e Injeção de Dependência (`Depends`). O router HTTP **nunca toma decisões de bloqueio**, apenas recebe os dados e atira a exceção lançada pelas profundezas do domínio.

* **`/domain`:** Entidades base (Ex: `AnalystAgent`, `ExecutionAgent`) e abstrações contratuais de defesa (`ILtiValidator`, `IEncryptionService`).
* **`/application`:** Casos de uso diretos (`run_notebook_solver`, `run_autograder_loop`) que engatam os serviços e ditam o andamento do processo.
* **`/infrastructure/services`:** O maquinário pesado anti-bot. É aqui que os bytes são analisados (Scrapers, Cryptography, AST Parsing).
* **`/api`:** Endpoints limpos do FastAPI.

---

## ⚔️ Os 6 Agentes e suas Especialidades

1. **🕵️ Agente Scout (Batedor):**
   * *Ameaça:* Envenenamento de base e Scraping de Dumps.
   * *Módulo:* `scout.py` / `sql_scout_repository.py`
2. **✍️ Agente Scribe (Escriba):**
   * *Ameaça:* Shadow Bots e Fazendas de Upvotes (Sybil Attack).
   * *Módulo:* `scribe.py` / `forum_defense.py`
3. **💬 Agente Persuasion (Persuasão):**
   * *Ameaça:* Farm de VCCs Trials para benefício econômico.
   * *Módulo:* `persuasion.py` / `billing_service.py`
4. **🧠 Agente Learning (Aprendizagem):**
   * *Ameaça:* Speedrunning de Vídeos/Testes e Time Travel de Headers.
   * *Módulo:* `learning.py` / `time_service.py`
5. **⚙️ Agente Analyst (Analista):**
   * *Ameaça:* Bypass de Testes Automáticos (Autograder) e Exfiltração de Quiz JSON.
   * *Módulo:* `analyst.py` / `audit_service.py`
6. **🚀 Agente Execution (Execução):**
   * *Ameaça:* OOB Azure Deploy e Mineração Criptográfica em Laboratórios Sandbox.
   * *Módulo:* `execution.py` / `lab_platform_client.py`

---

## 🧱 As 10 Linhas de Defesa Ciber-Aplicadas (Matriz de Mitigação)

Em resposta à automação agressiva do Atacante, o backend executa 10 barreiras físicas:

| Vetor de Ataque | Ação Ofensiva | Defesa Ativa Quimera (Blue Team) |
| :--- | :--- | :--- |
| **1. Time-Travel Header** | Falsificação de marca de tempo (Client-Time) na DOM para destravar aulas. | **`time_service.py`**: Relógio Absoluto Server-Side (`TimeLockValidator`). |
| **2. Shadow Botting (Sybil)** | Disparo de 40 requisições simultâneas aprovando respostas em fóruns visibilidade. | **`forum_defense.py`**: Tracking de IP e *Behavioral Rate Limiting*. |
| **3. Virtual Credit Cards** | Uso massivo de cartões virtuais p/ quebrar assinaturas Trial Gratuitas. | **`payment_validator.py`**: Análise rígida de BIN (Bank ID) anti-prepagos via Stripe. |
| **4. Cloud Hit-and-Run** | Desligamento imediato do laboratório após atingir 100% via API. | **`infrastructure_auditor.py`**: Sustained Uptime Metrics (Bloqueio orgânico em infraestrutura jovem). |
| **5. Camera Spoofing OBS** | Projeção de WebRTC "Falso/Offline" contra validadores acadêmicos. | **`kyc_provider.py`**: Onfido Biometric liveness 3D em tempo real. |
| **6. Credential Scraping** | Roubo do Voucher bruto para venda no Mercado Negro. | **`voucher_defense.py`**: Geolocking, Humanity Checks e Watermarking de Token (Rastreabilidade). |
| **7. IAM Escalation Abuse** | Bot usa o cluster lab para minerar Criptomoedas ou criar Sub-Tenants. | **`lab_platform_client.py`**: Sandboxing e corte severo de privilégios VPC. |
| **8. Quiz JSON Exfiltration** | O Bot pula o Selenium, pega a API Base `/fetch-quiz` e joga no Github. | **`encryption_service.py`**: Payloads viajam em AES (`Fernet`) e Ids sofrem *Polymorphism*. |
| **9. Autograder Hardcoding** | Código cravado (`assert = 42`) sem nenhuma rede neural treinada no meio da prova. | **`audit_service.py`**: Inspeção estrutural de *Abstract Syntax Tree (AST)* e Blind Data. |
| **10. CLI Remote Deploy** | Roubo de Service Principal via DOM para dar `az login` local em Varginha. | **`lab_platform_client.py`**: IPs fixados (Conditional Access) e Iframe Bastion sem segredos client-side. |

---

## 🛠️ Stack Tecnológico e Inicialização
- **Linguagem:** Python 3.10+
- **Framework Web:** FastAPI
- **Core Dependencies:** `cryptography`, `PyJWT`, `pytest`, `uvicorn`.

Para executar baterias de teste locais em Produção Mockada (`Quimera_Production`), utilize o isolamento sem dependência de Docker.

```bash
cd Quimera_Production/
pip install -r requirements.txt
pytest app/tests/ -v
```

> **NOTA DO ARQUITETO:**
> As APIs contidas neste repositório não processam lógica nas bordas. Se um bypass de AST ocorrer, é o *Use Case* numéricas e injetivas que emite a explosão nativa (ValueError), protegendo o sistema contra o pior inimigo de sistemas estatais e acadêmicos na nuvem: Automação cega.
