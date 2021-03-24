FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN python --version
RUN pip install --upgrade pip
RUN pip install hdbcli==2.3.119
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python ./index.py
