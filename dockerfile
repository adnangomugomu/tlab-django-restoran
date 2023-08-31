FROM python:3.11.5

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y netcat-traditional

RUN chmod +x /app/entrypoint.sh

RUN pip install Django==4.2.2 mysqlclient djangorestframework

CMD ["/app/entrypoint.sh"]

EXPOSE 8000