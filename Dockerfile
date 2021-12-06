FROM python:3.8-slim

# Adiciona aplicação
ADD . /code
COPY . /code
WORKDIR /code
RUN pip install -r requirements.txt

CMD ["python", "-u", "/app/main.py"]