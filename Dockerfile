FROM python:3.11
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD gunicorn --bind 0.0.0:$PORT app:app
# Use the environment variable PORT to specify the port number
# Use gunicorn to serve the app
# Use the app module to run the app