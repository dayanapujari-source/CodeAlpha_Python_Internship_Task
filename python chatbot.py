print("🤖 Welcome to Simple Chatbot!")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hello! Nice to meet you.")
    elif user == "how are you":
        print("Bot: I am fine. Thank you!")
    elif user == "what is your name":
        print("Bot: I am a Simple Chatbot.")
    elif user == "who created you":
        print("Bot: I was created using Python.")
    elif user == "bye":
        print("Bot: Goodbye! Have a great day.")
        break
    else:
        print("Bot: Sorry, I don't understand. Please try another question.")