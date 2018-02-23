FROM python:3
WORKDIR /app/consumer
ADD . /app/consumer
RUN pip install -r requirements.txt
CMD ["python3", "/app/consumer/recieve.py"]
