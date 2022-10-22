FROM python:3.6.9-alpine3.9
RUN python -m pip install --upgrade pip
RUN apk update
RUN apk add musl-dev gcc
RUN git clone https://github.com/Lamden/stamp_estimation_script.git
RUN cd contracting
RUN python3 ./setup.py develop
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["python","./run.py"]