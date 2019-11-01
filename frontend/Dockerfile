FROM python:3-alpine

WORKDIR /app

COPY app/requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY app/server.py server.py

ENTRYPOINT [ "python" ]

CMD [ "server.py" ]