# FakeNewsAPI
A REST API to determine if the News is fake or not using GloVe Embeddings and LSTM from this [kaggle notebook](https://www.kaggle.com/madz2000/nlp-using-glove-embeddings-99-8-accuracy). Implemented on Python [FastAPI](https://github.com/tiangolo/fastapi).

## Installation
```bash
git clone https://github.com/MasiCal354/fakenewsapi.git
conda env create --name fakenewsapi --file=environments.yml
conda activate fakenewsapi
cd fakenewsapi
```

## Run the API

### Run on localhost
```bash
uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```

### Run on Server
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### Run on Port 80 (HTTP) or 443 (HTTPS)
```bash
sudo apt-get update
sudo apt-get install authbind
sudo touch /etc/authbind/byport/80
sudo chmod 500 /etc/authbind/byport/80
sudo chown <username> /etc/authbind/byport/80
sudo touch /etc/authbind/byport/443
sudo chmod 500 /etc/authbind/byport/443
sudo chown <username> /etc/authbind/byport/443
authbind --deep uvicorn main:app --host 0.0.0.0 --port 80 --reload
authbind --deep uvicorn main:app --host 0.0.0.0 --port 443 --reload
```