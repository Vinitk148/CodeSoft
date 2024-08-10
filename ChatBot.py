rules = {
    "hello": "Hi there! How can I assist you today?",
    "how are you": "I'm just a bot, but I'm doing great! How about you?",
    "what is your name": "I'm a chatbot created to help you with simple tasks.",
    "bye": "Goodbye! Have a nice day!",
    "default": "Sorry, I don't understand that. Can you please rephrase?"
}

def chatbot_response(user_input):
    user_input = user_input.lower()
    for key in rules:
        if key in user_input:
            return rules[key]    
    return rules["default"]

def chat():
    print("Welcome to the rule-based chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")        
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a nice day!")
            break        
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

chat()
