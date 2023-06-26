FROM python:3.8-slim-buster
WORKDIR /app    
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app
ENV ACCESS_TOKEN=<token>
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "src/server.py" ]