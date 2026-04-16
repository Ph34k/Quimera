# PROJETO QUIMERA - TODO & ROADMAP
*Atualizado por: Jules (Chief Dev Engineer)*

## ✅ Fase 1: Infraestrutura Básica (Concluído)
- [x] Criação do esqueleto de diretórios (Clean Architecture): `app/domain`, `app/application`, `app/infrastructure`, `app/api`.
- [x] Configuração centralizada com `.env.example` e `app/core/config.py`.
- [x] Orquestração Docker: `docker-compose.yml` (Postgres, Redis, ElasticSearch).
- [x] Estrutura Inicial do Banco de Dados: `app/infrastructure/database.py` (SQLAlchemy).
- [x] Definição Abstrata dos 6 Agentes Base: `app/domain/agents.py`.

## ✅ Fase 2: Mínimo Produto Viável - MVP (Concluído)
- [x] Instanciação do app FastAPI (`app/main.py`).
- [x] Roteamento API Básico (`app/api/router.py`) com Health Check.
- [x] Endpoint da API do Agente Batedor (Scout) `/api/v1/scout/mission`.
- [x] Testes Unitários de MVP (`tests/test_api.py`) via `pytest` e `TestClient`.

---

## 🚧 Fase 3: Desenvolvimento de Agentes (Em Andamento)
- [ ] **🕵️ Agente Scout:** Implementar extração Selenium/BeautifulSoup para coleta de Hotspots.
- [ ] **🧠 Agente Analista:** Ligar ao pipeline NLP (OpenAI) para atribuição de escores "Big Five" a perfis.
- [ ] **🚀 Agente Execution:** Integrar lógica de furtividade (rotação de Proxy/User-Agent).
- [ ] **💬 Agente Persuasion:** Criar motor de templates para gatilhos de Cialdini.
- [ ] **🪶 Agente Escriba:** Mapear RAG para gerar abordagens "Push & Pull" seguras.
- [ ] **⏱️ Agente de Aprendizagem:** Integrar Redis para taxa de resposta e limite de *Shadow Bans*.

## 🛠️ Fase 4: DevOps e MLOps (Futuro)
- [ ] Concluir migrações completas do Alembic (quando os Modelos ORM estiverem prontos).
- [ ] Ligar ElasticSearch ao pipeline de vetorização para busca semântica de documentação / perfis.
- [ ] Hook de pre-commit para formatação (`black`, `isort`, `ruff`).
- [ ] Esteira CI/CD no GitHub Actions.
