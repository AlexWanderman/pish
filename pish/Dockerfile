FROM python
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
ENTRYPOINT gunicorn --bind 0.0.0.0:5000 wsgi:app
