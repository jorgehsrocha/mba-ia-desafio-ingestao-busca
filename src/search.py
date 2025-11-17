import os
from dotenv import load_dotenv
load_dotenv()
from src.check_env import check_env
check_env()

from langchain_core.prompts import PromptTemplate

from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_postgres import PGVector


PROMPT_TEMPLATE = """
CONTEXTO:
{contexto}

REGRAS:
- Responda somente com base no CONTEXTO.
- Se a informação não estiver explicitamente no CONTEXTO, responda:
  "Não tenho informações necessárias para responder sua pergunta."
- Nunca invente ou use conhecimento externo.
- Nunca produza opiniões ou interpretações além do que está escrito.

EXEMPLOS DE PERGUNTAS FORA DO CONTEXTO:
Pergunta: "Qual é a capital da França?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Quantos clientes temos em 2024?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Você acha isso bom ou ruim?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

PERGUNTA DO USUÁRIO:
{pergunta}

RESPONDA A "PERGUNTA DO USUÁRIO"
"""


def search_prompt(question=None):
  try:
    if not question:
        raise ValueError("A pergunta não pode estar vazia.")

    embeddings = OpenAIEmbeddings(model=os.environ.get("OPENAI_EMBEDDING_MODEL"))
    vector_store = PGVector(
        embeddings=embeddings,
        collection_name=os.environ.get("PG_VECTOR_COLLECTION_NAME"),
        connection=os.environ.get("DATABASE_URL"),
        use_jsonb=True
    )
    context = vector_store.similarity_search_with_score(
      k=10,
      query=question
    )

    prompt = PromptTemplate(
        input_variables=["contexto", "pergunta"],
        template=PROMPT_TEMPLATE
    )
    prompt_template = prompt.format(
      contexto="\n".join([f"Score: {score}\n Content: {doc.page_content} \n\n" for doc, score in context]),
      pergunta=question
    )
    chat = ChatOpenAI(model="gpt-5-nano")
    response = chat.invoke(prompt_template)
    return response.content
  except Exception as e:
    print(f"Erro ao buscar resposta: {e}")
    return None



