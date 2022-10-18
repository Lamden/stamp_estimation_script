# Stamp Estimation Script

A script for estimating stamps cost and setup a socket sever to communicate with [Lamden Block Service](https://github.com/Lamden/lamden_block_service).

### Prepare
**These are install steps for UBUNTU 18.04**

1. python 3.6.x (should come with UBUNTU 18.04)
2. poetry installed. `poetry` is a package manager tool. More detail click [here](https://python-poetry.org/docs)
``` 
    # Install poetry
    curl -sSL https://install.python-poetry.org -o install-poetry.py
    python3 install-poetry.py --version 1.1.7

    # Add poetry to environment variable
    sudo vim /etc/profile # then add `export PATH="/root/.local/bin:$PATH"` to this file
    source /etc/profile # make it works

    poetry --version # test that everything is set up
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
poetry run start # Default use config.dev.ini

PYTHON_ENV="production" poetry run start # Will use config.ini
```