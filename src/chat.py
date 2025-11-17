from .search import search_prompt

def main():
    question = input("PERGUNTA: ")
    
    if not question.strip():
        print("A pergunta não pode estar vazia.")
        main()
        return
    
    chain = search_prompt(question)
    if not chain:
        print("Não foi possível iniciar o chat. Verifique os erros de inicialização.")
        return
    print("RESPOSTA:", chain, "\n\n")
    main()


if __name__ == "__main__":

    print("\nBem-vindo ao sistema de perguntas e respostas! \n")
    print("======="*10)
    main()