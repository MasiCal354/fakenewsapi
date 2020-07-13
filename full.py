from fastapi import FastAPI
from tensorflow.keras.models import load_model
import pickle
import os
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
import string, re
from keras.preprocessing import sequence
import numpy as np

stop = set(stopwords.words('english'))
punctuation = list(string.punctuation)
stop.update(punctuation)

def strip_html(text):
    soup = BeautifulSoup(text, 'html.parser')
    return soup.get_text()

def remove_between_square_brackets(text):
    return re.sub('\[[^]]*\]', '', text)

def remove_url(text):
    return re.sub(r'http\S+', '', text)

def remove_stopwords(text):
    final_text = []
    for i in text.split():
        if i.strip().lower() not in stop:
            final_text.append(i.strip())
    return " ".join(final_text)

def denoise_text(text):
    text = strip_html(text)
    text = remove_between_square_brackets(text)
    text = remove_url(text)
    text = remove_stopwords(text)
    return text

maxlen = 300

def fake_news_preprocess(title, content):
    text = content + ' ' + title
    text = denoise_text(text)
    tokenized_text = tokenizer.texts_to_sequences(np.array([text]))
    vector = sequence.pad_sequences(tokenized_text, maxlen=maxlen)
    return vector

model_path = os.path.abspath('models/model.keras')
model = load_model(model_path)
tokenizer_path = os.path.abspath('models/tokenizer.pkl')
with open(tokenizer_path, 'rb') as f:
    tokenizer = pickle.load(f)

description = """
A REST API to load predict if the news is fake or not using LSTM with GloVe Embeeded Text Data
"""

app_config = {
    'title': 'FakeNewsAPI',
    'description': description,
    'version': '0.0.1'
}

app = FastAPI(**app_config)

@app.get('/predict')
async def predict(title: str, content: str):
    vector = fake_news_preprocess(title, content)
    prediction = model.predict(vector)
    real_probability = float(prediction[0][0])
    fake_probability = 1 - real_probability
    response = {
        'fake_probability': fake_probability
    }
    return response
