import os
import configparser
from script.server import run_server
from script.driver import BlockserviceDriver
from script.contracts.install import install_contracts
from contracting.db.driver import ContractDriver
from contracting.client import ContractingClient

config = configparser.ConfigParser()
env = os.environ.get("PYTHON_ENV")
if(env == "production"):
    config.read('config.ini', encoding='UTF-8')
else:
    config.read('config.dev.ini', encoding='UTF-8')


CONN = config.get('mongo', 'conn') 
DATABASE = config.get('mongo', 'database') 
COLLECTION = config.get('mongo', 'collection') 
blockService_driver = BlockserviceDriver(CONN, DATABASE, COLLECTION)

HOST = config.get('socket', 'host') 
PORT = config.get('socket', 'port') 

def start():
    c_driver =  ContractDriver(driver = blockService_driver)
    # initital
    install_contracts(client=ContractingClient(submission_filename=os.path.dirname(__file__) + '/contracts/submission.s.py', driver = c_driver))
    # Start socket server
    run_server(driver=blockService_driver, host=HOST, port=PORT)
