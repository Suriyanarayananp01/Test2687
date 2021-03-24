FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip download hdbcli==2.3.119 -d vendor --find-links ./sap_dependencies --platform linux_x86_64 --only-binary=:all:
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python ./index.py
