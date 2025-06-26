import nltk
import random
import string
import spacy
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download NLTK data
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Sample responses
responses = {
    "hello": ["Hello!", "Hi there!", "Hey! How can I help you?"],
    "bye": ["Goodbye!", "See you later!", "Bye! Take care!"],
    "name": ["I'm a chatbot created by CODTECH.", "My name is CodBot."],
    "help": ["I can answer your questions. Try asking me something!"],
    "default": ["I'm sorry, I didn't understand that.", "Can you please rephrase your question?"]
}

# Preprocessing function
lemmatizer = WordNetLemmatizer()
def preprocess(text):
    text = text.lower()
    tokens = nltk.word_tokenize(text)
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in string.punctuation and word not in stopwords.words('english')]
    return tokens

# Intent matcher
def get_response(user_input):
    tokens = preprocess(user_input)
    if not tokens:
        return random.choice(responses["default"])

    for word in tokens:
        if word in responses:
            return random.choice(responses[word])
    
    return random.choice(responses["default"])

# Chat loop
print("CODTECH Chatbot (type 'exit' to stop)")
while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        print("Bot: Goodbye!")
        break
    response = get_response(user_input)
    print("Bot:", response)

