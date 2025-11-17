# Desafio MBA Engenharia de Software com IA - Full Cycle

Para executar o projeto, siga os passos abaixo:

1. Clone o repositório:
    ```bash
    git clone <repository_url>
2. Execute os serviços necessários presentes no `docker-compose.yml`:
    ```bash
    docker-compose up -d
    ```
3. Navegue até o diretório do projeto:
    ```bash
    cd mba-ia-desafio-ingestao-busca
    ```
4. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
5. Ingestão de documentos PDF:
    ```bash
    python src/ingest.py
    ```
6. Inicie o chat para fazer perguntas sobre os documentos ingeridos:
    ```bash
    python -m src.chat
    ```
