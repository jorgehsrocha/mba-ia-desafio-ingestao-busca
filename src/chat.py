from src.search import search_prompt
from src.check_env import check_env

check_env()

def main():
    question = input("PERGUNTA: ")

    if question.lower() == "sair":
        print("Até mais!")
        return

    if not question.strip():
        print("A pergunta não pode estar vazia.")
        return main()
    
    chain = search_prompt(question)
    if not chain:
        print("Não foi possível iniciar o chat. Verifique os erros de inicialização.")
        return
    print("RESPOSTA:", chain, "\n\n")
    return main()


if __name__ == "__main__":

    print("\nBem-vindo ao sistema de perguntas e respostas! Para sair digite 'sair'.\n")
    print("======="*10)
    main()