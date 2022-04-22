# Stamp Estimation Script

A script for estimating stamps cost and setup a socket sever to communicate with [Lamden Block Service](https://github.com/Lamden/lamden_block_service).

### Prepare

- python 3.6+
- poetry installed. `poetry` is a package manager tool. More detail click [here](https://python-poetry.org/docs)

### Install
```
git clone https://github.com/Lamden/stamp_estimation_script.git 

cd stamp_estimation_script/

poetry install # Installing dependences.

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
poetry run python ./setup.py # Default use config.dev.ini

poetry run PYTHON_ENV="production" python ./setup.py # Will use config.ini
```