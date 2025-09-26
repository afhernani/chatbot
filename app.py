# -*- coding: utf-8 -*-
# pip install flask nltk scikit-learn
from flask import Flask, render_template, request
import nltk, random, string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
nltk.download('punkt')
nltk.download('wordnet')

# Descargar stopwords en español
nltk.download('stopwords')
from nltk.corpus import stopwords
spanish_stopwords = stopwords.words('spanish')


with open('chatbot.txt', 'r', errors='ignore') as f:
    raw = f.read().lower()
# Tokenización en español
sent_tokens = nltk.sent_tokenize(raw, language='spanish')
word_tokens = nltk.word_tokenize(raw, language='spanish')

sent_tokens = nltk.sent_tokenize(raw)
lemmer = nltk.stem.WordNetLemmatizer()
def LemTokens(tokens): return [lemmer.lemmatize(t) for t in tokens]
remove_punct_dict = dict((ord(p), None) for p in string.punctuation)
def LemNormalize(text): return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))
# Saludos en español
GREETING_INPUTS = ("hola", "buenas", "saludos", "qué tal", "hey")
GREETING_RESPONSES = ["¡Hola!", "¡Hey!", "*asiente*", "Hola, ¿qué tal?", "¡Encantado de hablar contigo!"]
def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)
def response(user_response):
    robo_response = ''
    sent_tokens.append(user_response)
    # TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words=spanish_stopwords)
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if req_tfidf == 0:
        robo_response += "lo siento! No te entiendo."
    else:
        robo_response += sent_tokens[idx]
    sent_tokens.remove(user_response)
    return robo_response

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    if greeting(userText):
        return greeting(userText)
    else:
        return response(userText)

if __name__ == "__main__":
    app.run(debug=True)
