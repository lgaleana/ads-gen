from fastapi import FastAPI
from .url_text_extractor import extract

app = FastAPI()

app.add_api_route('/extract', extract, methods=['POST'])