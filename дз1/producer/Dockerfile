FROM python:3
WORKDIR /app/producer
ADD . /app/producer
RUN pip install -r requirements.txt
CMD ["python3", "/app/producer/send.py"]
