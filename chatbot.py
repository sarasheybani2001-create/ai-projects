def chatbot():
    print("AI Assistant Ready.\n")

    name = input("What's your name? ")
    print(f"Nice to meet you, {name}.\n")

    mood = None

    while True:
        user = input("You: ").lower()

        if user == "bye":
            print("Bot: Goodbye. Take care.")
            break

        elif "name" in user:
            print(f"Bot: Your name is {name}.")

        elif "how are you" in user:
            print("Bot: I'm here and working. What about you?")

        elif "i am" in user or "i'm" in user:
            if "tired" in user:
                mood = "tired"
                print("Bot: Then don’t push too hard. Do light work today.")
            elif "sad" in user:
                mood = "sad"
                print("Bot: It’s okay. Take a pause. You don’t need to solve everything today.")
            elif "good" in user or "happy" in user:
                mood = "good"
                print("Bot: Good. Use that energy wisely.")
            else:
                print("Bot: I see.")

        elif "study" in user:
            if mood == "tired":
                print("Bot: Study in short sessions. 30–40 minutes is enough.")
            elif mood == "sad":
                print("Bot: Start with something easy. Build momentum slowly.")
            else:
                print("Bot: Focus on one subject at a time. Avoid multitasking.")

        elif "ai" in user:
            print("Bot: AI is about building systems that can learn and make decisions.")

        elif "help" in user:
            print("Bot: You can ask me about study, mood, or general questions.")

        else:
            print("Bot: I’m still learning. Try asking in a different way.")


chatbot()