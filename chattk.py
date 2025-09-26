# -*- coding: utf-8 -*-
# pip install flask nltk scikit-learn
import tkinter as tk
from tkinter import scrolledtext
import nltk
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Inicialización NLTK
nltk.download('punkt')
nltk.download('wordnet')

# Corpus
with open('chatbot.txt', 'r', errors='ignore') as f:
    raw = f.read().lower()
sent_tokens = nltk.sent_tokenize(raw)

# Preprocesamiento
lemmer = nltk.stem.WordNetLemmatizer()
def LemTokens(tokens): return [lemmer.lemmatize(t) for t in tokens]
remove_punct_dict = dict((ord(p), None) for p in string.punctuation)
def LemNormalize(text): return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

# Saludos
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey")
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]
def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

# Respuesta
def response(user_response):
    robo_response = ''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if req_tfidf == 0:
        robo_response += "I am sorry! I don't understand you."
    else:
        robo_response += sent_tokens[idx]
    sent_tokens.remove(user_response)
    return robo_response

# Interfaz Tkinter
def send():
    user_input = entry.get()
    chat_window.insert(tk.END, "You: " + user_input + "\n")
    entry.delete(0, tk.END)
    if user_input.lower() == 'bye':
        chat_window.insert(tk.END, "ROBO🤖: Bye! Take care.\n")
        return
    elif user_input.lower() in ['thanks', 'thank you']:
        chat_window.insert(tk.END, "ROBO🤖: You are welcome!\n")
    elif greeting(user_input) is not None:
        chat_window.insert(tk.END, "ROBO🤖: " + greeting(user_input) + "\n")
    else:
        chat_window.insert(tk.END, "ROBO🤖: " + response(user_input) + "\n")

root = tk.Tk()
root.title("ROBO Chatbot")

chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20, font=("Arial", 12))
chat_window.pack(padx=10, pady=10)

entry = tk.Entry(root, width=60, font=("Arial", 12))
entry.pack(padx=10, pady=5)

send_button = tk.Button(root, text="Send", command=send, font=("Arial", 12))
send_button.pack(pady=5)

chat_window.insert(tk.END, "ROBO🤖: Hello! I am ROBO. Ask me anything about chatbots. Type 'bye' to exit.\n")

root.mainloop()
