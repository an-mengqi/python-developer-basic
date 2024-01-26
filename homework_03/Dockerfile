FROM python:3.11.7-bookworm

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY my_application ./

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=8000"]

EXPOSE 8000
