from tensorflow.keras.models import load_model
import pickle
import os

model_path = os.path.abspath('models/model.keras')
model = load_model(model_path)

tokenizer_path = os.path.abspath('models/tokenizer.pkl')
with open(tokenizer_path, 'rb') as f:
    tokenizer = pickle.load(f)