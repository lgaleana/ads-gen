FROM --platform=linux/amd64 tiangolo/uvicorn-gunicorn-fastapi:python3.7

WORKDIR /app

COPY ./app /app

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]