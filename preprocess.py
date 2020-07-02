from models import tokenizer
from utils import denoise_text
from keras.preprocessing import sequence
import numpy as np

maxlen = 300

def fake_news_preprocess(payload):
    text = payload.text + ' ' + payload.title
    text = denoise_text(text)
    tokenized_text = tokenizer.texts_to_sequences(np.array([text]))
    vector = sequence.pad_sequences(tokenized_text, maxlen=maxlen)
    
    return vector