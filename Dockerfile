FROM python:3

RUN apt update && apt install -y postgresql

RUN mkdir /app
COPY . /app/

WORKDIR /app

RUN pip install -r requirements.txt
ENV PYTHONPATH="/app:${PYTHONPATH}"

CMD [ "python", "geralda.py"]