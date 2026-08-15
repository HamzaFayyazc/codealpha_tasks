def get_chatbot_response(user_input):
    # Input ko lowercase aur trim karna taake matching asaan ho
    user_input = user_input.lower().strip()

    # Predefined Rules & Responses
    if user_input in ["hello", "hi", "hey", "aoa", "assalam o alaikum"]:
        return "Hi there! How can I help you today?"
        
    elif "how are you" in user_input:
        return "I'm doing great, thank you for asking! How are you?"
        
    elif "your name" in user_input or "who are you" in user_input:
        return "I am CodeAlpha's Python Chatbot!"
        
    elif "python" in user_input:
        return "Python is an amazing programming language! Are you enjoying coding in Python?"
        
    elif user_input in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye! Have a great day ahead!"
        
    else:
        return "I'm sorry, I didn't quite understand that. Can you rephrase?"

def run_chatbot():
    print("Welcome to Basic Rule-Based Chatbot")
    print("Type 'bye' or 'exit' anytime to end the conversation.\n")

    while True:
        user_text = input("You: ")
        
        # Checking exit condition
        if user_text.lower().strip() in ["bye", "exit", "quit"]:
            print("Chatbot:", get_chatbot_response(user_text))
            break
            
        # Ignore empty inputs
        if not user_text.strip():
            continue

        response = get_chatbot_response(user_text)
        print(f"Chatbot: {response}\n")

if __name__ == "__main__":
    run_chatbot()