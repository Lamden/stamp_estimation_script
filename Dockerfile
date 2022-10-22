FROM python:3.6.9-alpine3.9
RUN python -m pip install --upgrade pip
RUN apk update
RUN apk add musl-dev gcc git
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN pip install lmdb motor
RUN pip install git+https://github.com/Lamden/contracting.git
ENTRYPOINT ["python","./run.py"]