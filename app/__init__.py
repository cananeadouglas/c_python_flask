from flask import Flask

app = Flask(__name__)

# chamando o arquivo defatul dentro de controllers, nosso Hello World
from app.controllers import default

