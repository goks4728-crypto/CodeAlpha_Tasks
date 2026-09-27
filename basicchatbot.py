def get_bot_response(user_input):
    """Function to process user input using rule-based if-elif statements."""
    # Convert input to lowercase to handle different cases (e.g., "Hello", "HELLO")
    clean_input = user_input.lower().strip()

    if clean_input in ["hello", "hi", "hey"]:
        return "Hi!"
    elif clean_input == "how are you":
        return "I'm fine, thanks!"
    elif clean_input in ["bye", "goodbye"]:
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that. Try saying 'hello', 'how are you', or 'bye'."

def run_chatbot():
    """Main loop for running the interactive chat session."""
    print("=== Simple Rule-Based Chatbot ===")
    print("Chatbot is ready! Type 'bye' to end the conversation.\n")

    while True:
        # Get input from user
        user_input = input("You: ")
        
        # Get response from the function
        response = get_bot_response(user_input)
        print(f"Chatbot: {response}")

        # Exit loop if user says bye
        if user_input.lower().strip() in ["bye", "goodbye"]:
            break

if __name__ == "__main__":
    run_chatbot()