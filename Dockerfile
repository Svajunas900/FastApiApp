FROM python:alpine3.21

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

RUN pip install "fastapi[standard]"

CMD [ "fastapi", "run", "main.py", "--port", "3000" ]

EXPOSE 3000