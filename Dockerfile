FROM python:3.6.9-alpine3.9
RUN python -m pip install --upgrade pip
RUN apk update
RUN apk add musl-dev gcc git make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libhdf5-dev clang
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN pip install lmdb motor
RUN pip install git+https://github.com/Lamden/contracting.git@dev-staging
ENTRYPOINT ["python","./run.py"]