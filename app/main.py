from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from app.url_text_extractor import extract, Url

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

app.add_api_route('/extract', extract, methods=['POST'], dependencies=[Depends(Url)])
