FROM python:3.6.9-alpine3.9
RUN python -m pip install --upgrade pip
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["./app/run.py"]