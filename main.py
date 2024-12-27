# Importing required libraries

from textblob import TextBlob  # Library for Natural Language Processing (NLP) tasks like sentiment analysis

import colorama  # Library to add colored text to the terminal for better user experience

from colorama import Fore, Style  # Fore and Style are used to customize text color and style

import sys
import time
# Initialize colorama to ensure the terminal resets colors automatically after each output
colorama.init(autoreset=True)

# Global variables to store user information and sentiment counts
user_name = ""  # Stores the user's name (Agent)
conversation_history = []  # Keeps track of all sentences entered by the user
positive_count = 0  # Counter for positive messages
negative_count = 0  # Counter for negative messages
neutral_count = 0  # Counter for neutral messages

def show_processing_animation():
    print(f"{Fore.CYAN}🕵️ Detecting sentiment clues", end="")  # Starting animation text
    for _ in range(3):  # Loop to print three dots for the animation
        time.sleep(0.5)  # Pause for half a second (simulate processing delay)
        print(".", end="")  # Print a dot without moving to a new line
        sys.stdout.flush()  # Force the terminal to display the output immediately


def analyze_sentiment(text):
    """
    Analyzes the sentiment of the input text using TextBlob.
    Categories:
    - Positive: Polarity > 0.25
    - Neutral: Polarity between -0.25 and 0.25
    - Negative: Polarity < -0.25
    """
    global positive_count, negative_count, neutral_count  # Access global counters

    try:
        blob = TextBlob(text)  # Create a TextBlob object with the input text
        sentiment = blob.sentiment.polarity  # Get the polarity score (range: -1.0 to 1.0)
        conversation_history.append(text)  # Save the input to the conversation history

        # Categorize the sentiment based on thresholds
        if sentiment > 0.75:
            positive_count += 1  # Increment positive counter
            return f"\n{Fore.GREEN}🌟 Very Positive sentiment detected, Agent! (Score: {sentiment:.2f})"
        elif 0.25 < sentiment <= 0.75:
            positive_count += 1  # Increment positive counter
            return f"\n{Fore.GREEN}😊 Positive sentiment detected, Agent! (Score: {sentiment:.2f})"
        elif -0.25 <= sentiment <= 0.25:
            neutral_count += 1  # Increment neutral counter
            return f"\n{Fore.YELLOW}😐 Neutral sentiment detected."
        elif -0.75 <= sentiment < -0.25:
            negative_count += 1  # Increment negative counter
            return f"\n{Fore.RED}💔 Negative sentiment detected, Agent. (Score: {sentiment:.2f})"
        else:
            negative_count += 1  # Increment negative counter
            return f"\n{Fore.RED}💔 Very Negative sentiment detected, Agent. (Score: {sentiment:.2f})"

    except Exception as e:
        # Handles any errors that might occur during sentiment analysis
        return f"{Fore.RED}An error occurred during sentiment analysis: {str(e)}"


def start_sentiment_chat():
  
  print(f"{Fore.CYAN}{Style.DIM} 🕵️ Welcome to Sentiment Spy! Your personal emotion detective is here. 🎉")
  name=input("enter your name:").strip()
  if name and name.isalpha():
    print((f"\n{Fore.GREEN}Nice to meet you, Agent {name}! Type your sentences to analyze emotions. Type 'help' for options."))
    # Get user input
    user_input = input(f"\n{Fore.MAGENTA}{Style.BRIGHT}Agent {name}: {Style.RESET_ALL}").strip()
    if not user_input:  # Handle empty input
        print(f"{Fore.RED}Please enter a non-empty message or type 'help' for available commands.")
    elif user_input.lower() == 'exit':  # Exit the program
        print(f"\n{Fore.BLUE}🔚 Mission complete! Exiting Sentiment Spy. Farewell, Agent {name}!")
        #print(execute_command("summary"))  # Display final summary
    elif user_input.lower() in ["summary", "reset", "history", "help"]:  # Handle special commands
        print("checking")
    else:
            # Simulate processing animation and analyze sentiment
        show_processing_animation()
        result = analyze_sentiment(user_input)
        print(result)
  else:
    print(f"{Fore.RED}Please enter a valid name with only alphabetic characters.")






if __name__ == "__main__":
    start_sentiment_chat()
 