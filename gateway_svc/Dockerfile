FROM python:3.9-slim

WORKDIR /app

COPY gateway.py /app/

RUN pip install flask requests

EXPOSE 5000

CMD ["python", "gateway.py"]
