FROM python:2.7

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 1111
ENTRYPOINT [ "python", "server.py" ]