FROM python:3.12-alpine

ENV workers=4

WORKDIR /app
COPY . /app

RUN pip3 install -r requirements.txt

RUN export PYTHONPATH="${PYTHONPATH}:/app"

CMD python3 -m pytest -r A -n ${workers}