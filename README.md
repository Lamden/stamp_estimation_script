# Stamp Estimation Script

A script for estimating stamps cost and setup a socket sever to communicate with [Lamden Block Service](https://github.com/Lamden/lamden_block_service).

### Prepare
**These are install steps for UBUNTU 18.04**

1. python 3.6.x (should come with UBUNTU 18.04)
2. docker && docker-compose (Optional)

### Install
```
cd ~
git clone https://github.com/Lamden/stamp_estimation_script.git 
cd stamp_estimation_script/
pip install -r requirements.txt

```

### Config
```
# mongo config
[mongo]
conn=mongodb://user:pwd@localhost:27017 # mongo connection string.
database=testnet-blockservice  # block service mongo database name.
collection=currentState  # Collection name.

# socket config
[socket]
host=localhost # host address
port=3232    # port number
```

### Run
```
python3 run.py # Default use config.dev.ini

ENVIRONMENT="production" python3 run.py # Will use config.ini
```


### Docker (Recommended)
```
docker-compose build
docker-compose up -d
```