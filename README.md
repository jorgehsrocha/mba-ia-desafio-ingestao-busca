# Desafio MBA Engenharia de Software com IA - Full Cycle

Para executar o projeto, siga os passos abaixo:

Atenção: O projeto utiliza a OpenAI API, certifique-se de ter uma chave válida e configurada na variável de ambiente `OPENAI_API_KEY`.

1. Configure as variáveis de ambiente necessárias no arquivo `.env`:
    ```env
        OPENAI_API_KEY=
        OPENAI_EMBEDDING_MODEL='text-embedding-3-small'
        DATABASE_URL=postgresql+psycopg://postgres:postgres@localhost:5432/rag
        PG_VECTOR_COLLECTION_NAME=
    ```

2. Clone o repositório:
    ```bash
    git clone <repository_url>
3. Execute os serviços necessários presentes no `docker-compose.yml`:
    ```bash
    docker-compose up -d
    ```
5. Navegue até o diretório do projeto:
    ```bash
    cd mba-ia-desafio-ingestao-busca
    ```
6. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
7. Ingestão de documentos PDF:
    ```bash
    python -m src.ingest
    ```
8. Inicie o chat para fazer perguntas sobre os documentos ingeridos:
    ```bash
    python -m src.chat
    ```
