FROM python:3.6.9-slim
RUN python -m pip install --upgrade pip
RUN apt-get update
RUN apt-get install -y git llvm tk-dev libhdf5-dev clang
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN pip install lmdb motor
RUN pip install git+https://github.com/Lamden/contracting.git
ENTRYPOINT ["python","./run.py"]