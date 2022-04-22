import json
import os
from contracting.client import ContractingClient

root = os.path.dirname(__file__)
genesis_path = os.path.dirname(__file__) + '/genesis.json'
submission_path = os.path.dirname(__file__) + '/submission.s.py'

def install_contracts(client: ContractingClient):

    with open(genesis_path) as f:
        genesis = json.load(f)

    for contract in genesis['contracts']:
        c_filepath = root + '/genesis/' + contract['name'] + '.s.py'
        with open(c_filepath) as f:
            code = f.read()
        contract_name = contract['name']
        if contract.get('submit_as') is not None:
            contract_name = contract['submit_as']

        if client.get_contract(contract_name) is None:
            client.submit(code, name=contract_name, owner=contract['owner'],
                          constructor_args=contract['constructor_args'])
    
    client.raw_driver.commit()
    # clear cache
    client.raw_driver.clear_pending_state()

