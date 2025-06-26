# AI-CHATBOT-WITH-NLP
COMPANY: CODTECH IT SOLUTIONS 
NAME: C Kishore
INTERN ID: CT06DN863
DOMAIN: Python Programming 
DURATION: 6 weeks 
MENTOR: NEELA SANTOSH

Project Title: AI Chatbot using NLP
Internship Task - 3 | CODTECH

Overview:
This project is about creating a text-based AI chatbot using Natural Language Processing (NLP) libraries such as NLTK and spaCy in Python. The chatbot can understand simple user inputs and respond to basic queries using predefined responses.

Tools and Technologies Used:

Python: Main programming language used for development

NLTK: For tokenization, stopword removal, and lemmatization

spaCy: For NLP parsing and model usage

VS Code: Code editor used to write and run the script

Terminal/Command Prompt: To install packages and run the chatbot

Steps to Create the File:

Installed required libraries using the terminal:

pip install nltk spacy

python -m nltk.downloader punkt wordnet stopwords

python -m spacy download en_core_web_sm

Created a Python file named chatbot_codtech.py in VS Code.

Wrote code that:

Accepts user input from the terminal

Preprocesses input text using NLTK

Matches input keywords with predefined categories

Responds with appropriate answers

Ran the chatbot using the command:

python chatbot_codtech.py

How the Chatbot Works:

The user types a message.

The message is tokenized and lemmatized to simplify understanding.

The chatbot checks for keywords like "hello", "bye", "help", etc.

Based on keyword matching, it responds with a suitable reply.

If no keyword matches, it replies with a default response.

Typing "exit" or "quit" ends the chat session.

Deliverables:

chatbot_codtech.py: Python script for the chatbot

This project description file

