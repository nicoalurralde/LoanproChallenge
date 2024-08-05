FROM python:3.12-alpine

WORKDIR /app
COPY . /app

RUN pip3 install -r requirements.txt

RUN export PYTHONPATH="${PYTHONPATH}:/app"

CMD ["python", "-m", "pytest", "-r", "A", "-n", "auto"]