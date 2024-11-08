import re
import random

# Define a list of mental health-related topics and responses
responses = {
    "anxiety": [
        "I'm really sorry you're feeling anxious. It's okay to feel this way. Would you like to talk more about it?",
        "Anxiety can be overwhelming. Would you like some resources or tips to manage it?",
        "Take a deep breath. It's okay to feel anxious sometimes. Do you want to share more about what's on your mind?"
    ],
    "depression": [
        "I'm really sorry you're feeling down. It can be really tough, but you're not alone.",
        "It's okay to feel low sometimes, but it’s important to talk to someone. Would you like some resources or suggestions?",
        "Sometimes it helps to talk. Would you like to share more about what's going on?"
    ],
    "stress": [
        "Stress can be really exhausting. Would you like some tips on managing stress or do you want to talk more about it?",
        "I understand that stress can be hard. Would you like me to suggest some relaxation techniques?",
        "Take it easy. Would you like me to recommend some resources or just chat about how you're feeling?"
    ],
    "self_harm": [
        "I'm really sorry you're feeling this way, but I’m here to help. Please consider talking to a professional.",
        "Self-harm is a serious matter. It might help to speak with someone close to you or a professional."
    ],
    "general": [
        "I'm here to listen. What's on your mind?",
        "It's okay to talk about how you're feeling. Would you like to share more with me?"
    ]
}

# Define the function to check if a keyword is present in the user input
def check_keywords(user_input):
    # Convert the input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Simple keyword matching for mental health topics
    if re.search(r"\banxious\b|\banxiety\b|\bnervous\b|\bworry\b", user_input):
        return "anxiety"
    elif re.search(r"\bdepressed\b|\bsad\b|\bdown\b|\bunhappy\b", user_input):
        return "depression"
    elif re.search(r"\bstress\b|\bstressed\b|\boverwhelmed\b|\bpressure\b", user_input):
        return "stress"
    elif re.search(r"\bhurt\b|\bself-harm\b|\bcuts\b|\bpain\b", user_input):
        return "self_harm"
    else:
        return "general"

# Generate a response based on the identified topic
def generate_response(user_input):
    # Identify the mental health topic
    topic = check_keywords(user_input)
    
    # Select a random response from the corresponding list
    response = random.choice(responses.get(topic, responses["general"]))
    return response

# Sample conversation starter
def start_chat():
    print("Hello! I'm here to help. How are you feeling today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Bot: Take care! I'm here if you need to talk again.")
            break
        response = generate_response(user_input)
        print(f"Bot: {response}")

# Start the chatbot conversation
if __name__ == "__main__":
    start_chat()
