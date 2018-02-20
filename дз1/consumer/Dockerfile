FROM python:3
MAINTAINER elena
WORKDIR /app
ADD . /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python", "recieve.py" ]


