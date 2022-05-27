# Stamp Estimation Script

A script for estimating stamps cost and setup a socket sever to communicate with [Lamden Block Service](https://github.com/Lamden/lamden_block_service).

### Prepare
**These are install steps for UBUNTU 18.04**

1. python 3.6.x (should come with UBUNTU 18.04)
2. poetry installed. `poetry` is a package manager tool. More detail click [here](https://python-poetry.org/docs)
```
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
    source $HOME/.poetry/env
```

### Install Dependancies
1. pip3
```
    sudo apt-get update
    sudo apt-get -y install python3-pip
```

2. python setuptools
```
    pip3 install setuptools
```

2. lamden contracting
```
    cd ~
    git clone https://github.com/Lamden/contracting.git
    cd contracting
    git checkout blockservice-driver
    python3 ./setup.py develop
```

3. 

### Install
```
cd ~
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

PYTHON_ENV="production" poetry run python ./setup.py # Will use config.ini
```