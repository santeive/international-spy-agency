FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y libpq-dev python3-dev git

# Install dependencies
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN mkdir /code
WORKDIR /code

ENTRYPOINT ["sh", "entrypoint.sh"]
