from openai import OpenAI
from dotenv import dotenv_values

def main():
    config = dotenv_values(".env")

    client = OpenAI(
        api_key=config["OPENAI_API_KEY"],
    )

    # Histórico do chat
    messages = [
        {"role": "system", "content": "You are an assistant."}
    ]

    print("Chatbot iniciado! (digite 'sair' para encerrar)\n")

    while True:
        user_input = input("Você: ")
        if user_input.lower() in ["sair", "exit", "quit"]:
            print("Encerrando o chat. Até mais!")
            break

        # Adiciona a mensagem do usuário no histórico
        messages.append({"role": "user", "content": user_input})

        # Faz a chamada para o OpenAI
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )

        # Pega a resposta
        chatbot_response = completion.choices[0].message.content
        print(f"Chatbot: {chatbot_response}\n")

        # Adiciona a resposta do bot no histórico
        messages.append({"role": "assistant", "content": chatbot_response})

if __name__ == "__main__":
    main()