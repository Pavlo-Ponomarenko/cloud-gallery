FROM python:3.9

WORKDIR /app

COPY . .

RUN chmod +x run.sh

RUN pip install --no-cache-dir flask

EXPOSE 5000

ENTRYPOINT ["bash", "run.sh"]