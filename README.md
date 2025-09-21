# Multi-Agent Business Intelligence

Um sistema de Business Intelligence conversacional impulsionado por agentes autônomos com LangGraph.
O projeto simula um time virtual de analistas de dados capazes de extrair, consultar, contextualizar e comunicar insights de forma integrada.

🚀 Visão Geral

O MABI foi desenvolvido como projeto de portfólio para demonstrar como arquiteturas multiagente podem transformar o processo de análise de dados.
Ele combina ETL, banco de dados, RAG (Retrieval-Augmented Generation) e agentes especializados para oferecer uma experiência de BI de próxima geração.

Com o MABI, o usuário pode simplesmente perguntar:

"O clima impactou as vendas de eletrônicos no último trimestre? Mostre os dados e traga recomendações."

E os agentes se organizam para:

Extrair e transformar os dados.

Consultar o banco via SQL.

Buscar contexto em relatórios/documentos.

Criar gráficos e storytelling executivos.

Entregar um insight acionável, orquestrado pelo supervisor.

🧩 Arquitetura de Agentes

ETL Agent → coleta, limpa e carrega dados em um banco central (Postgres/SQLite).

SQL Agent → traduz perguntas em queries SQL e retorna resultados estruturados.

RAG Agent → busca contexto em documentos corporativos (PDFs, relatórios, manuais).

Storytelling/Visualization Agent → transforma dados em gráficos e insights executivos.

Supervisor Agent → orquestra os demais, decide quais agentes ativar e costura as respostas.

🛠️ Tecnologias Utilizadas

LangGraph
 → orquestração de múltiplos agentes.

Python 3.11+

PostgreSQL ou SQLite (para persistência dos dados tratados pelo ETL).

Pandas / SQLAlchemy (ETL e manipulação de dados).

Streamlit ou FastAPI (interface interativa — opcional).

OpenAI / LLM API (para agentes SQL e RAG).

📈 Caso de Uso Exemplo

Pergunta:

"Qual foi o impacto da inflação nos custos de logística nos últimos 12 meses? E traga recomendações do relatório de operações."

Fluxo de Resposta:

Supervisor encaminha a questão para o SQL Agent.

SQL Agent gera query e retorna tabela com custos x inflação.

RAG Agent consulta relatórios e traz recomendações.

Storytelling Agent gera gráfico + sumário executivo.

Supervisor compila e entrega a resposta final.

🎯 Objetivo do Projeto

Demonstrar habilidades práticas em IA multiagente com LangGraph.

Mostrar integração de ETL, bancos de dados e RAG.

Exibir capacidade de transformar dados em insights acionáveis.

Servir como projeto de portfólio com aplicabilidade direta em cenários de Business Intelligence real.

📌 Próximos Passos (Roadmap)

 Criar MVP com ETL + SQL Agent + Supervisor.

 Integrar RAG Agent para contexto adicional.

 Adicionar Storytelling Agent com visualizações automáticas.

 Construir interface em Streamlit para interação conversacional.

 Publicar versão demo hospedada.