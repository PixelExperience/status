FROM python:alpine

RUN mkdir /app
RUN apk update && apk add bash
COPY  . /app
WORKDIR /app
RUN pip install pyyaml requests pygithub

CMD ["bash", "entrypoint.sh"]
