FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir fastapi uvicorn requests redis faiss-cpu sentence-transformers

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

#docker build -t sre-ai .
#docker run -p 8000:8000 sre-ai