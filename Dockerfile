FROM python:3-alpine

ENV DISCORD_TOKEN ""

WORKDIR /app

COPY app/requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY app/bot.py bot.py

ENTRYPOINT [ "python" ]

CMD [ "bot.py" ]
