FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN python --version
RUN pip install --upgrade pip
RUN pip3 install hdbcli
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python ./index.py
