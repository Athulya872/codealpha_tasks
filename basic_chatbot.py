# Basic Chatbot

print("===== BASIC CHATBOT =====")
print("Type 'bye' to end the chat.\n")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hi! Nice to meet you.")

    elif user == "how are you":
        print("Bot: I'm fine, thanks! How are you?")

    elif user == "what is your name":
        print("Bot: I'm a simple Python chatbot.")

    elif user == "thank you":
        print("Bot: You're welcome!")

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")