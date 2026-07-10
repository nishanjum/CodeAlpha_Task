def get_chatbot_response(user_input):
    """
    Evaluates user input and returns a predefined reply.
    Converts string to lowercase to handle variations like 'Hello' or 'HELLO'.
    """
    cleaned_input = user_input.strip().lower()

    if cleaned_input == "hello":
        return "Hi!"
    elif cleaned_input == "how are you":
        return "I'm fine, thanks!"
    elif cleaned_input == "bye":
        return "Goodbye!"
    else:
        return "I am a simple rule-based bot. Try saying 'hello', 'how are you', or 'bye'."

def start_chatbot():
    print("==============================================")
    print("🤖 Chatbot: System Initialized. Say something!")
    print("(Type 'bye' to exit the conversation)")
    print("==============================================\n")
    
    # Infinite loop to keep the chat running continuously
    while True:
        # Capture input from user
        user_message = input("You: ")
        
        # Generate response using our function
        bot_response = get_chatbot_response(user_message)
        
        # Output the response
        print(f"Bot: {bot_response}\n")
        
        # Break the loop conditions to safely close the script if user says 'bye'
        if user_message.strip().lower() == "bye":
            break

# --- Execution ---
if __name__ == "__main__":
    start_chatbot()