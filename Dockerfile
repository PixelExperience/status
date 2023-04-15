FROM python:3.8.6-buster

RUN mkdir /app
WORKDIR /app
RUN pip install pyyaml requests python-telegram-bot asyncio

CMD ["bash", "entrypoint.sh"]