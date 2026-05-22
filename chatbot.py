def chatbot():
    print("Chatbot is ready! Type 'bye' to exit")

    while True:
        user_input = input("You: ").lower()

        if user_input == "bye":
            print("Bot: Goodbye!")
            break
        elif "hello" in user_input:
            print("Bot: Hi there!")
        elif "name" in user_input:
            print("Bot: I am a simple AI chatbot.")
        elif "ai" in user_input:
            print("Bot: AI stands for Artificial Intelligence.")
        else:
            print("Bot: I don't understand that yet.")

chatbot()