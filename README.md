# Stamp Estimation Script

A script for estimating stamps cost and setup a socket sever to communicate with [Lamden Block Service](https://github.com/Lamden/lamden_block_service).

**These are install steps for UBUNTU 18.04**

### Install

Clone this repo

```
cd ~
git clone https://github.com/Lamden/stamp_estimation_script.git 

```

Install docker

```
curl -fsSL https://get.docker.com | bash -s docker
```

Then install docker-compose, you can get the latest release at [here](https://github.com/docker/compose/releases)

```
sudo curl -L "https://github.com/docker/compose/releases/download/v2.2.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

### Config

Create a config file at the root of project

```
cd stamp_estimation_script
touch config.ini
```

Copy the following configuration info to the config file ```config.ini``` and modify it according to your own situation.

```
# mongo config
[mongo]
conn=mongodb://user:pwd@localhost:27017 # Same as the mongo server that the blockservice use.
database=testnet-blockservice  # Same as the database name that the blockservice use
collection=currentState  # Collection name.

# socket config
[socket]
host=localhost # host address
port=3232    # port number
```

### Run

Build project

```
cd stamp_estimation_script/
docker-compose build # build docker image
```

Run the server

```
docker-compose up -d # 
```