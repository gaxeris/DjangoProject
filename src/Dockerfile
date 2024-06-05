FROM python:3.11.4-slim-buster

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

#postgres dependencies to remove errors when installing requirements
RUN apt-get update && apt-get install -y libpq-dev gcc
#netcat provides simple client which can try to connect to postgres and check if its ready
RUN apt-get install -y netcat 
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# COPY ./entrypoint.sh /
RUN chmod +x ./entrypoint.sh

#this image is used for two containers: nginx and django. Only django needs a custom entrypoint
# ENTRYPOINT ["sh", "entrypoint.sh"]

# EXPOSE 8000
