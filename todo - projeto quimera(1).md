---
title: Projeto Quimera — Plano de Execução
projeto: Quimera
status: Em andamento
prioridade: Alta
tags:
  - projeto/quimera
  - plano
  - engenharia
criado_em: 2025-10-22
owner: "@responsavel-principal"
dv_objetivo:
  - Subir os serviços localmente sem erros
  - Postgres acessível para os serviços
  - Esquema do banco alinhado aos modelos
  - Estrutura idêntica em todos os serviços
  - Eliminar duplicações e alinhar modelos/clients
  - Ponto único para ler/validar variáveis
  - Garantir operações básicas de banco
  - Isolar a lógica de análise (texto/imagem)
  - Trocar modelos por configuração, sem alterar código
  - Evitar quedas de qualidade
  - Encapsular a escolha de estratégia
  - Alterar lógica de decisão sem novo deploy
  - Comparar versões de regras na prática
  - Editar textos de prompt sem tocar no código
  - Cache, retentativas e tratamento de erro nas chamadas
  - Medir a qualidade das respostas geradas
  - Registrar episódios e calcular “recompensa” por conversa concluída
  - Avaliações semanais e consolidação dos resultados
  - Atualizar modelos/prompts com dados suficientes e ganho comprovado
  - Garantir qualidade a cada mudança
dv_entregas:
  - "`docker-compose up` funcional; `.env.example` atualizado; `Makefile` com `make up/down/logs`"
  - "`healthcheck_db.sh`; usuário/base criados via init"
  - "`alembic.ini` e `env.py` corretos; `revision --autogenerate`; `upgrade head`"
  - "`app/core`, `app/domain`, `app/infrastructure`, `app/api`; guia rápido (1 página)"
  - "Modelos (ex.: Perfil), esquemas, clientes Postgres/Redis, utilitários"
  - Módulo `settings` com validação; docs das variáveis
  - Testes de criação/leitura/atualização/remoção; pipeline local
  - Serviço com funções de entrada/saída bem definidas
  - "`ModelCache` (carregamento por versão; fallback)"
  - "`evals/analyst/` com dados rotulados; script de precisão/recall/F1"
  - "Interface simples (entrada: perfil/contexto; saída: estratégia)"
  - Arquivos em `rules/` (YAML/JSON); validador de esquema
  - Chaveamento por porcentagem; coleta de resultados por versão
  - "`app/prompts/` com templates nomeados e variáveis claras"
  - "`LLMService` com timeout configurável; logs úteis em falha"
  - "`evals/scribe/` com conjunto de ouro e métricas (clareza, aderência)"
  - Serviço ouvindo `ConversaFinalizada`; persiste `episodios_treinamento`
  - Agendamento (cron/worker) para `evals/analyst`, `evals/persuasion`, `evals/scribe`
  - "Scripts de retreino; política de gatilho (ex.: N exemplos de alta qualidade)"
  - GitHub Actions com testes, avaliações, build de imagens e deploy
  - "`ruff/black/isort` (ou equivalentes) e hook `pre-commit`"
  - Logs estruturados; métricas de latência/erro; traços simples entre serviços
  - Segredos fora do repo; rotação simples; princípio do menor acesso
dv_passos:
  - Revisar versões, redes e volumes; padronizar nomes de serviços; checar portas; revisar variáveis de ambiente
  - Configurar `init.sql`; validar credenciais no `.env`
  - Apontar `SQLALCHEMY_DATABASE_URI`; gerar e aplicar revisão
dv_aceitação:
  - Contêineres “healthy” em `docker ps`; logs sem erros críticos
  - "`psql` conecta; `SELECT 1` responde; serviço dependente inicia"
  - Tabela(s) criadas/alteradas; `downgrade` reversível em dev
  - Todos os serviços seguem o layout; builds sem regressões
  - Serviços importam do `common/`; código duplicado removido
  - Troca de ambiente sem editar código; erros de config claros
  - Testes passam (>80% dos casos críticos); roda em `make test`
  - Chamadas previsíveis; testes dos caminhos principais
  - Versão na config seleciona o modelo correto; logs claros
  - Relatório em arquivo; falha se escore < limite definido
  - Testes cobrindo cenários comuns e extremos
  - Mudança de arquivo altera comportamento; validação bloqueia regras inválidas
  - Relatório por grupo; opção “vencedor leva tudo”
  - Mudança de prompt reflete no resultado; histórico versionado
  - Simulações mostram recuperação; interrupções não quebram o fluxo
  - Relatório com escore global; limite mínimo evita regressões
  - Eventos com campos obrigatórios; painel simples de taxa/hora
  - Relatórios por data; alerta se cair abaixo do limite
  - Comparativo antes/depois com ganho mensurável; rollback disponível
  - Falha quando escore cai; sucesso gera imagem e deploy automatizados
  - "`make lint` e `make format` sem pendências"
  - Dashboards mínimos; alerta em falhas frequentes
  - Scanner não encontra segredos; variáveis carregadas em runtime seguro
dv_dependências:
  - —
  - T0.1
  - T0.2
  - T0.x
  - T1.1
  - T1.2
  - T0.3, T1.2
  - T1.1
  - T1.3
  - T1.4
  - T1.1
  - T2B.1
  - T2B.2, T3.1 (dados)
  - T1.1
  - T1.3
  - T2C.2
  - T1.2, T0.3
  - T3.1, T2A.3, T2B.3, T2C.3
  - T3.2
  - T1.4, T2*.3
dv_esforço:
  - M
  - S
  - S
  - M
  - M
  - S
  - S
  - M
  - S
  - M
  - S
  - S
  - M
  - S
  - M
  - M
  - M
  - S
  - M
  - M
  - S
  - M
  - S
---

# Projeto Quimera — Plano (tarefas acionáveis)

> [!summary] Visão geral
> Cada tarefa lista **objetivo**, **entregas**, **critérios de aceitação**, **dependências** e **esforço (S/M/L)**. Use as _checkboxes_ para acompanhar o progresso. Os campos `chave:: valor` funcionam com **Dataview**.

---


```


```

> ```
```
## Trilha 0 — Desbloqueio do Ambiente (prioridade máxima)

- [ ] **T0.1 | Ajustar execução local com Docker**  
  objetivo:: Subir os serviços localmente sem erros  
  entregas:: `docker-compose up` funcional; `.env.example` atualizado; `Makefile` com `make up/down/logs`  
  passos:: Revisar versões, redes e volumes; padronizar nomes de serviços; checar portas; revisar variáveis de ambiente  
  aceitação:: Contêineres “healthy” em `docker ps`; logs sem erros críticos  
  dependências:: —  
  esforço:: M

- [ ] **T0.2 | Banco de dados operacional**  
  objetivo:: Postgres acessível para os serviços  
  entregas:: `healthcheck_db.sh`; usuário/base criados via init  
  passos:: Configurar `init.sql`; validar credenciais no `.env`  
  aceitação:: `psql` conecta; `SELECT 1` responde; serviço dependente inicia  
  dependências:: T0.1  
  esforço:: S

- [ ] **T0.3 | Migrações automáticas com Alembic**  
  objetivo:: Esquema do banco alinhado aos modelos  
  entregas:: `alembic.ini` e `env.py` corretos; `revision --autogenerate`; `upgrade head`  
  passos:: Apontar `SQLALCHEMY_DATABASE_URI`; gerar e aplicar revisão  
  aceitação:: Tabela(s) criadas/alteradas; `downgrade` reversível em dev  
  dependências:: T0.2  
  esforço:: S

---

## Trilha 1 — Arquitetura Padronizada & Dados

- [x] **T1.1 | Padronizar layout de serviços**  
  objetivo:: Estrutura idêntica em todos os serviços  
  entregas:: `app/core`, `app/domain`, `app/infrastructure`, `app/api`; guia rápido (1 página)  
  aceitação:: Todos os serviços seguem o layout; builds sem regressões  
  dependências:: T0.x  
  esforço:: M

- [x] **T1.2 | Biblioteca comum (`common/`)**  
  objetivo:: Eliminar duplicações e alinhar modelos/clients  
  entregas:: Modelos (ex.: Perfil), esquemas, clientes Postgres/Redis, utilitários  
  aceitação:: Serviços importam do `common/`; código duplicado removido  
  dependências:: T1.1  
  esforço:: M

- [x] **T1.3 | Configuração central**  
  objetivo:: Ponto único para ler/validar variáveis  
  entregas:: Módulo `settings` com validação; docs das variáveis  
  aceitação:: Troca de ambiente sem editar código; erros de config claros  
  dependências:: T1.2  
  esforço:: S

- [x] **T1.4 | Testes do nível de dados**  
  objetivo:: Garantir operações básicas de banco  
  entregas:: Testes de criação/leitura/atualização/remoção; pipeline local  
  aceitação:: Testes passam (>80% dos casos críticos); roda em `make test`  
  dependências:: T0.3, T1.2  
  esforço:: S

---

## Trilha 2 — Agentes com Avaliação Contínua

### 2A) Agente Analista

- [x] **T2A.1 | Extrair `AnalystService` (domínio)**  
  objetivo:: Isolar a lógica de análise (texto/imagem)  
  entregas:: Serviço com funções de entrada/saída bem definidas  
  aceitação:: Chamadas previsíveis; testes dos caminhos principais  
  dependências:: T1.1  
  esforço:: M

- [x] **T2A.2 | Cache de modelos por versão**  
  objetivo:: Trocar modelos por configuração, sem alterar código  
  entregas:: `ModelCache` (carregamento por versão; fallback)  
  aceitação:: Versão na config seleciona o modelo correto; logs claros  
  dependências:: T1.3  
  esforço:: S

- [ ] **T2A.3 | Conjunto de ouro + avaliação**  
  objetivo:: Evitar quedas de qualidade  
  entregas:: `evals/analyst/` com dados rotulados; script de precisão/recall/F1  
  aceitação:: Relatório em arquivo; falha se escore < limite definido  
  dependências:: T1.4  
  esforço:: M

### 2B) Motor de Persuasão

- [ ] **T2B.1 | `PersuasionService`**  
  objetivo:: Encapsular a escolha de estratégia  
  entregas:: Interface simples (entrada: perfil/contexto; saída: estratégia)  
  aceitação:: Testes cobrindo cenários comuns e extremos  
  dependências:: T1.1  
  esforço:: S

- [ ] **T2B.2 | Regras externas versionadas**  
  objetivo:: Alterar lógica de decisão sem novo deploy  
  entregas:: Arquivos em `rules/` (YAML/JSON); validador de esquema  
  aceitação:: Mudança de arquivo altera comportamento; validação bloqueia regras inválidas  
  dependências:: T2B.1  
  esforço:: S

- [ ] **T2B.3 | A/B simples de estratégias**  
  objetivo:: Comparar versões de regras na prática  
  entregas:: Chaveamento por porcentagem; coleta de resultados por versão  
  aceitação:: Relatório por grupo; opção “vencedor leva tudo”  
  dependências:: T2B.2, T3.1 (dados)  
  esforço:: M

### 2C) Agente Escriba

- [ ] **T2C.1 | Diretório de prompts**  
  objetivo:: Editar textos de prompt sem tocar no código  
  entregas:: `app/prompts/` com templates nomeados e variáveis claras  
  aceitação:: Mudança de prompt reflete no resultado; histórico versionado  
  dependências:: T1.1  
  esforço:: S

- [ ] **T2C.2 | Serviço de LLM resiliente**  
  objetivo:: Cache, retentativas e tratamento de erro nas chamadas  
  entregas:: `LLMService` com timeout configurável; logs úteis em falha  
  aceitação:: Simulações mostram recuperação; interrupções não quebram o fluxo  
  dependências:: T1.3  
  esforço:: M

- [ ] **T2C.3 | Avaliação do Escriba**  
  objetivo:: Medir a qualidade das respostas geradas  
  entregas:: `evals/scribe/` com conjunto de ouro e métricas (clareza, aderência)  
  aceitação:: Relatório com escore global; limite mínimo evita regressões  
  dependências:: T2C.2  
  esforço:: M

---

## Trilha 3 — MLOps & Automação (melhoria contínua)

- [ ] **T3.1 | Agente de Aprendizagem (loop de feedback)**  
  objetivo:: Registrar episódios e calcular “recompensa” por conversa concluída  
  entregas:: Serviço ouvindo `ConversaFinalizada`; persiste `episodios_treinamento`  
  aceitação:: Eventos com campos obrigatórios; painel simples de taxa/hora  
  dependências:: T1.2, T0.3  
  esforço:: M

- [ ] **T3.2 | Reavaliação periódica**  
  objetivo:: Avaliações semanais e consolidação dos resultados  
  entregas:: Agendamento (cron/worker) para `evals/analyst`, `evals/persuasion`, `evals/scribe`  
  aceitação:: Relatórios por data; alerta se cair abaixo do limite  
  dependências:: T3.1, T2A.3, T2B.3, T2C.3  
  esforço:: S

- [ ] **T3.3 | Retreinamento automatizado**  
  objetivo:: Atualizar modelos/prompts com dados suficientes e ganho comprovado  
  entregas:: Scripts de retreino; política de gatilho (ex.: N exemplos de alta qualidade)  
  aceitação:: Comparativo antes/depois com ganho mensurável; rollback disponível  
  dependências:: T3.2  
  esforço:: M

- [ ] **T3.4 | Integração/Entrega Contínuas (CI/CD)**  
  objetivo:: Garantir qualidade a cada mudança  
  entregas:: GitHub Actions com testes, avaliações, build de imagens e deploy  
  aceitação:: Falha quando escore cai; sucesso gera imagem e deploy automatizados  
  dependências:: T1.4, T2*.3  
  esforço:: M

---

## Governança Técnica (transversal)

- [ ] **G1 | Linters + formatação + pre-commit**  
  entregas:: `ruff/black/isort` (ou equivalentes) e hook `pre-commit`  
  aceitação:: `make lint` e `make format` sem pendências  
  esforço:: S

- [ ] **G2 | Observabilidade básica**  
  entregas:: Logs estruturados; métricas de latência/erro; traços simples entre serviços  
  aceitação:: Dashboards mínimos; alerta em falhas frequentes  
  esforço:: M

- [ ] **G3 | Segurança e segredos**  
  entregas:: Segredos fora do repo; rotação simples; princípio do menor acesso  
  aceitação:: Scanner não encontra segredos; variáveis carregadas em runtime seguro  
  esforço:: S

---

## Ordem recomendada (marcos)

1. **T0.1 → T0.3** (ambiente e migrações)  
2. **T1.1 → T1.4** (arquitetura + base de dados + testes)  
3. **T2A.x → T2B.x → T2C.x** (agentes com avaliação)  
4. **T3.1 → T3.4** (loop de aprendizagem + automação)  
5. **G1–G3** distribuídas ao longo das trilhas

---

> [!warning] Riscos principais e mitigação
> - **Bloqueio de migração:** usar `--autogenerate`, testar `downgrade` e base de dev isolada  
> - **Queda de qualidade em modelo/prompt:** limites mínimos nos `evals` + rollback rápido  
> - **Complexidade de config:** `settings` central + docs curtas por serviço  
> - **Custos de inferência:** cache no `LLMService` + amostragem nos A/B

---

## Definição de Pronto (DoD) por serviço

- Sobe via `docker-compose` sem erro  
- Testes passando (dados e domínio)  
- Métricas básicas expostas  
- Config validada em runtime  
- Participa dos `evals` e respeita limites mínimos

---

## Métricas de sucesso (mínimas)

- **Confiabilidade:** >99% de sucesso em chamadas internas (dev)  
- **Qualidade Analista:** F1 ≥ alvo do conjunto de ouro  
- **Qualidade Escriba:** escore ≥ limite em clareza/aderência  
- **Persuasão:** grupo vencedor > controle, com significância simples  
- **Ciclo:** retreino apenas quando o `eval` indicar ganho ≥ limiar

---

## Próximo passo prático (hoje)

- [ ] Executar **T0.1–T0.3**  
- [ ] Registrar `README_DEV.md` com comandos de subir/derrubar o ambiente e como rodar migrações e testes
