from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from .url_text_extractor import extract

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

app.add_api_route('/extract', extract, methods=['POST'])