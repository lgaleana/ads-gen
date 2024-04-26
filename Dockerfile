FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY ./scripts /app/scripts

CMD ["uvicorn", "scripts.url_text_extractor:app", "--host", "0.0.0.0", "--port", "8080"]