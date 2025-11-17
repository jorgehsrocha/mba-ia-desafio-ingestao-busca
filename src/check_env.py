import os
from dotenv import load_dotenv
load_dotenv()

def check_env():
    required_env_vars = [
        "OPENAI_API_KEY",
        "OPENAI_EMBEDDING_MODEL",
        "DATABASE_URL",
        "PG_VECTOR_COLLECTION_NAME"
    ]

    env_errors = [f"Environment variable {var} is not set." for var in required_env_vars if not os.getenv(var)]
    if env_errors:
        raise EnvironmentError(" ".join(env_errors))
