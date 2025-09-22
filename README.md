# Multi-Agent Compliance

Um sistema de Compliance conversacional impulsionado por agentes autônomos com LangGraph.
O projeto simula um time virtual de analistas de dados capazes de extrair, consultar, contextualizar e comunicar insights de forma integrada.

## Agentes:
- Supervisor: gerencia os demais agentes
- RAG: agente especializado em RAG dos arquivos de compliance e jurídicos da empresa
- SQL: agente consultivo, que extrai informações direto do banco de dados
- GMAIL: agente gerenciador de email, capaz de enviar relatórios direto para a caixa de entrada do usuario
---
## Stacks

- LangGraph → orquestração de múltiplos agentes
- Python 3.11+
- PostgreSQL
- Pandas
- Flask
- LLM API (adaptável)

---
### Caso de Uso Exemplo

Pergunta:

"Qual foi o impacto da inflação nos custos de logística nos últimos 12 meses? 
E traga recomendações do relatório de acordo com a política da empresa. Envie essas recomendações para
empresa@empresa.com.br com o assunto: 'Relatório de recomendações' "

Fluxo de Resposta:

- Supervisor encaminha a questão para o SQL Agent.
- SQL Agent gera query e retorna tabela com custos x inflação.
- RAG Agent consulta relatórios e traz recomendações.
- Supervisor compila e entrega a resposta final.

## Próximos Passos
- Implementar dashboard visual com Streamlit
- Adicionar agent de business intelligence
- publicar mvp hospedado
- Implementar tests
