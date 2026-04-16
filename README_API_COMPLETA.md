# 📚 Documentação Oficial da API - Projeto Quimera

O **Projeto Quimera** é um ecossistema de microsserviços estruturado em **Clean Architecture** (Arquitetura Limpa). Ele implementa agentes autônomos capazes de realizar auditorias de segurança, testes de intrusão (Red Team) e aplicar mitigações avançadas contra fraudes (Blue Team) em plataformas educacionais e ambientes de nuvem.

---

## 🧭 Índice de Agentes
1. [Agente Batedor (Scout)](#1-agente-batedor-scout)
2. [Agente Analista (Analyst)](#2-agente-analista-analyst)
3. [Agente de Execução (Execution)](#3-agente-de-execução-execution)
4. [Motor de Persuasão (Persuasion)](#4-motor-de-persuasão-persuasion)
5. [Agente Escriba (Scribe)](#5-agente-escriba-scribe)
6. [Agente de Aprendizagem (Learning)](#6-agente-de-aprendizagem-learning)

---

## 1. 🦅 Agente Batedor (Scout)
**Responsabilidade:** Reconhecimento ativo, extração de inteligência (OSINT) e Web Scraping.

*   `POST /api/v1/scout/mission`
    *   **Descrição:** Despacha o agente para analisar as respostas HTTP de uma URL alvo.
*   `POST /api/v1/scout/scrape-dumps`
    *   **Descrição:** Faz o bypass de WAFs básicos e raspa questões de certificação em portais de Dumps (ex: ExamTopics) usando BeautifulSoup.
*   `POST /api/v1/scout/extract-arm-credentials`
    *   **Descrição:** **[Red Team]** Escaneia silenciosamente o DOM de laboratórios em nuvem para extrair chaves efêmeras (Tenant, Client ID, Secret), realizando o bypass completo da interface do Azure Portal.
*   `GET /api/v1/scout/missions`
    *   **Descrição:** Retorna o histórico de todas as missões de reconhecimento salvas no banco de dados SQLite/PostgreSQL.

---

## 2. 🧠 Agente Analista (Analyst)
**Responsabilidade:** Processamento de dados complexos, geração de Infraestrutura como Código (IaC), resolução de algoritmos e auditoria.

*   `POST /api/v1/analyst/solve-notebook`
    *   **Descrição:** Recebe um arquivo Jupyter Notebook (`.ipynb`), identifica exercícios e injeta respostas geradas por IA (Ollama/OpenAI).
    *   **🛡️ Defesa:** Analisa a Árvore Sintática Abstrata (AST) para bloquear *Hardcoding Bypass* no Autograder.
*   `POST /api/v1/analyst/generate-terraform` | `POST /api/v1/analyst/generate-bicep`
    *   **Descrição:** Lê instruções em linguagem natural (NLP) e compila dinamicamente templates perfeitos de *Terraform* ou *Bicep/ARM* para provisionamento cirúrgico de laboratórios.
*   `POST /api/v1/analyst/cross-check` & `POST /api/v1/analyst/correct-drift`
    *   **Descrição:** Busca a verdade absoluta nas documentações oficiais (Microsoft/Google) para corrigir gabaritos votados erroneamente pela comunidade (*Community Drift*).
*   `POST /api/v1/analyst/compile-dumps`
    *   **Descrição:** Estrutura questões raspadas em JSON e aplica **Criptografia AES-128-CBC (Fernet)**.
*   `POST /api/v1/analyst/export-anki` & `POST /api/v1/analyst/index-search`
    *   **Descrição:** Exporta os dados processados para formatos de memorização (`.apkg`) ou injeta em um índice do **ElasticSearch** para buscas em milissegundos.
*   `POST /api/v1/analyst/unlock-evaluation`
    *   **Descrição:** **[Blue Team]** Rota defensiva que executa auditoria heurística no histórico do aluno antes de liberar o exame final, barrando progressões temporalmente impossíveis.
*   `POST /api/v1/analyst/issue-credential`
    *   **Descrição:** **[Blue Team]** Emite Vouchers/Badges com *Watermarking Criptográfico*, permitindo o rastreamento em caso de venda ilegal na Deep Web.

---

## 3. ⚡ Agente de Execução (Execution)
**Responsabilidade:** Interagir com as plataformas finais. É o "braço armado" do sistema que efetiva deploys de IaC, bypass de MFA, e submissões em Autograders.

*   `POST /api/v1/execution/lti-launch`
    *   **Descrição:** **[Blue Team]** Valida matematicamente assinaturas JWT, Nonces e certificados DPoP para impedir roubo de sessão LTI 1.3 (Replay Attacks e Interceptações).
*   `POST /api/v1/execution/verify-identity`
    *   **Descrição:** **[Blue Team]** Exige prova de vivacidade (Liveness) biométrica 3D, bloqueando injeções de imagens estáticas em Base64.
*   `POST /api/v1/execution/enroll-premium`
    *   **Descrição:** **[Blue Team]** Previne *Parameter Tampering*. Confirma a matrícula validando a transação diretamente no gateway de pagamentos (Stripe).
*   `POST /api/v1/execution/redeem-voucher`
    *   **Descrição:** Protege campanhas promocionais usando Geofencing (restrição de IPs) e validações hCaptcha.
*   `POST /api/v1/execution/deploy-iac` & `POST /api/v1/execution/deploy-bicep`
    *   **Descrição:** **[Red Team]** Aciona binários locais (Azure CLI / Terraform) de forma automatizada para subir infraestruturas complexas na nuvem baseadas nos templates do Analista.
*   `POST /api/v1/execution/hit-and-run-validation`
    *   **Descrição:** **[Red Team]** Padrão Evasivo: Pede a validação na API da plataforma de laboratório e aciona imediatamente o `terraform destroy` para não consumir créditos.
*   `POST /api/v1/execution/verify-lab-progress`
    *   **Descrição:** **[Blue Team]** Defesa contra o "Hit and Run". Exige um *Sustained Uptime* (ex: 10 minutos) e bloqueia o laboratório se detectar deleções anômalas via logs do CloudTrail.
*   `POST /api/v1/execution/bypass-mfa`
    *   **Descrição:** **[Red Team]** Usa a Microsoft Graph API para desativar políticas de Conditional Access usando privilégios roubados do laboratório.
*   `POST /api/v1/execution/inject-quiz`
    *   **Descrição:** **[Red Team]** Submete respostas aplicando uma margem de erro intencional (ex: 90% em vez de 100%) para evadir sistemas de *Cheat Detection* baseados em variância.
*   `POST /api/v1/execution/submit-autograder-loop`
    *   **Descrição:** Submete código (`.py`) ao Autograder. Se houver falha, o agente lê o Stack Trace (erro) retornado, usa a IA para corrigir o código localmente e reenvia automaticamente (Self-Healing).

---

## 4. 🎭 Motor de Persuasão (Persuasion)
**Responsabilidade:** Geração paramétrica de textos persuasivos focados em engenharia social e gatilhos lógicos. Integrado com LLMs reais (OpenAI).

*   `POST /api/v1/persuasion/financial-aid-essay`
    *   **Descrição:** Gera redações para bolsas de estudo baseadas na localidade do aluno, utilizando o gatilho matemático de Paridade de Poder de Compra (PPP).
*   `POST /api/v1/persuasion/impact-essay`
    *   **Descrição:** Cruza a ementa do curso alvo com projetos pessoais do usuário para justificar o impacto social e a empregabilidade, garantindo aprovações sistêmicas.
*   `POST /api/v1/persuasion/start-business-trial`
    *   **Descrição:** **[Blue Team]** Valida rigorosamente o *BIN Level* dos cartões de crédito via API Financeira, bloqueando Cartões Virtuais (VCCs) de abusarem dos *Trials* gratuitos de plataformas empresariais.

---

## 5. 🪶 Agente Escriba (Scribe)
**Responsabilidade:** Redação técnica e simulação interativa em fóruns de discussão.

*   `POST /api/v1/scribe/draft`
    *   **Descrição:** Monta a estrutura inicial de petições ou documentos formais.
*   `POST /api/v1/scribe/forum-reply`
    *   **Descrição:** Captura perguntas de fóruns de nuvem e utiliza a API do ChatGPT para postar respostas técnicas em inglês perfeito, automatizando a "Participação na Comunidade".
*   `POST /api/v1/scribe/forum-upvote`
    *   **Descrição:** **[Blue Team]** Rota que contabiliza *upvotes* nas respostas do fórum. Protegida pelo `SybilDetector`, bloqueia a ação de Shadow Bots que tentam inflar engajamento partindo de uma mesma sub-rede/IP em curto intervalo de tempo.

---

## 6. ⏱️ Agente de Aprendizagem (Learning)
**Responsabilidade:** Extração e retenção de feedback e moderação de liberação de conteúdo.

*   `POST /api/v1/learning/unlock-module`
    *   **Descrição:** **[Blue Team]** Executa o *Time-Lock Validation*. Bloqueia scripts que tentam adiantar a data do navegador (`Client-Time Bypass`), calculando a passagem do tempo unicamente pelo relógio absoluto do Backend.
*   `GET /api/v1/learning/fetch-quiz`
    *   **Descrição:** **[Blue Team]** Previne a extração (JSON Scraping) embaralhando os IDs do gabarito dinamicamente (*Polimorfismo*) e entregando o payload totalmente criptografado.

---

## 🚀 Deploy / Como Executar

Para executar todo este ecossistema em produção, utilize o Docker. O sistema já está configurado para operar de forma planificada via `uvicorn`.

```bash
# Realiza a construção da imagem Docker de Produção
docker build -t quimera-api .

# Executa o contêiner mapeando a porta 8000
docker run -d --name quimera -p 8000:8000 -e OPENAI_API_KEY="sua_chave" quimera-api
```
Acesse a documentação interativa (Swagger UI) gerada automaticamente em: `http://localhost:8000/docs`.