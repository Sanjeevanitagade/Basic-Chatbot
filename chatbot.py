import random
import time
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True) # Automatically reset color after each print

def bot_print(message, color=Fore.CYAN, delay=0.03):
    """Prints the bot's message character by character with color."""
    print(color + "Bot: ", end="")
    for char in message:
        print(char, end="", flush=True)
        time.sleep(delay)
    print(Style.RESET_ALL) # Reset color at the end

def user_print(message, color=Fore.GREEN):
    """Prints the user's message with color."""
    print(color + "You: " + message + Style.RESET_ALL)

def get_bot_response(user_input):
    """Generates a response based on user input."""
    user_input = user_input.lower() # Case-insensitive matching

    # Predefined responses
    greetings = ["hello", "hi", "hey", "greetings"]
    farewells = ["bye", "goodbye", "exit", "quit"]
    how_are_you_responses = ["i'm doing great, thanks for asking!", "i'm just a bunch of code, but i'm feeling fine!", "feeling chatty! how about you?"]
    name_responses = ["you can call me ChatterBot 3000.", "i'm your friendly neighborhood chatbot!", "i don't really have a name, but i'm here to help!"]
    creator_responses = ["i was created by a clever programmer using Python!", "my origins are a mystery, even to me sometimes!"]
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "What do you call fake spaghetti? An impasta!"
    ]

    if any(greet in user_input for greet in greetings):
        return random.choice([
            "Hello there! How can I help you today? 😊",
            "Hi! What's on your mind?",
            "Hey! Great to chat with you."
        ])
    elif any(farewell in user_input for farewell in farewells):
        return random.choice([
            "Goodbye! Have a great day! 👋",
            "See you later! Come back soon.",
            "Bye for now!"
        ])
    elif "how are you" in user_input:
        return random.choice(how_are_you_responses)
    elif "what is your name" in user_input or "who are you" in user_input:
        return random.choice(name_responses)
    elif "who created you" in user_input or "who made you" in user_input:
        return random.choice(creator_responses)
    elif "tell me a joke" in user_input or "joke" in user_input:
        return random.choice(jokes)
    elif "help" in user_input:
        return "You can ask me things like 'how are you', 'what is your name', 'tell me a joke', or just chat! Type 'bye' to exit."
    elif "thanks" in user_input or "thank you" in user_input:
        return "You're welcome! 😊"
    elif "what can you do" in user_input:
        return "I can chat with you, tell jokes, and answer some basic questions. Try asking!"
    else:
        return random.choice([
            "Hmm, I'm not sure how to respond to that. Can you try asking something else?",
            "That's an interesting point! Tell me more.",
            "I'm still learning. Could you rephrase that?",
            "Let me think about that... 🤔 Actually, I'm not programmed for that yet."
        ])

def chat():
    """Main chat loop."""
    bot_print("Hello! I'm your friendly ChatBot. Type 'bye' to exit.", color=Fore.MAGENTA, delay=0.05)
    time.sleep(0.5) # Small pause after greeting

    while True:
        try:
            user_input = input(Fore.YELLOW + "You: " + Style.RESET_ALL) # Get user input
            if not user_input.strip(): # Handle empty input
                continue

            # user_print(user_input) # Optional: print user input again if you like the format

            if user_input.lower() in ["bye", "goodbye", "exit", "quit"]:
                bot_print(random.choice(["Goodbye! Take care! 👋", "Sad to see you go. Bye!"]), color=Fore.MAGENTA)
                break

            response = get_bot_response(user_input)
            time.sleep(random.uniform(0.5, 1.2)) # Simulate thinking
            bot_print(response)

        except KeyboardInterrupt: # Handle Ctrl+C
            bot_print("\nExiting chat. Goodbye!", color=Fore.MAGENTA)
            break
        except Exception as e:
            bot_print(f"Oops! Something went wrong: {e}", color=Fore.RED)
            bot_print("Let's try to continue...")

if __name__ == "__main__":
    chat()