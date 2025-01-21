import random
import sys

rules = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm good, thanks!", "I'm doing well, how about you?", "All good!"],
    "bye": ["Goodbye!", "Bye bye!", "See you later!"],
    "default": ["I'm sorry, I don't understand.", "Could you please repeat that?", "I'm not sure I follow."],
}

def generate_response(user_input):
    user_input = user_input.lower()
    for key in rules:
        if key in user_input:
            return random.choice(rules[key])
    return random.choice(rules["default"])

def chat():
    print("Chatbot: Hi! How can I help you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            sys.exit()

        response = generate_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    chat()