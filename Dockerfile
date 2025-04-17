FROM python:3.12-slim
COPY . /hab
WORKDIR /hab
RUN pip install -r requirements.txt
CMD gunicorn --bind 0.0.0.0:8888 app:app