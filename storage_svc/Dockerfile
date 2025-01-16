FROM python:3.9-slim

WORKDIR /app

COPY storage.py /app/

RUN pip install flask

EXPOSE 5001

CMD ["sh", "-c", "python storage.py $PORT"]
