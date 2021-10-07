ARG PYTHON_IMAGE_VERSION=python:3

FROM $PYTHON_IMAGE_VERSION

RUN apt update && apt install -y postgresql

RUN mkdir /app
COPY . /app/

WORKDIR /app

RUN pip install -r requirements.txt
ENV PYTHONPATH="/app:${PYTHONPATH}"

RUN python --version

CMD [ "python", "geralda.py"]