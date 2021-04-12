FROM python:3.9.4-slim-buster
COPY . /app
WORKDIR /app
RUN python --version  >"log.txt"
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python ./index.py
