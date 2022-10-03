from contracting.execution.executor import Executor
from contracting.db.encoder import safe_repr
from contracting.stdlib.bridge.time import Datetime
from datetime import datetime

from script.utils import format_dictionary


class TxExecutor:
    def __init__(self, executor: Executor):
        self.executor = executor

    def generate_environment(self, input_hash='0'*64, bhash='0' * 64, num=1):
        now = Datetime._from_datetime(
            datetime.now()
        )

        return {
            'block_hash': bhash,
            'block_num': num,
            '__input_hash': input_hash,  # Used for deterministic entropy for random games
            'now': now,
        }

    def execute_tx(self, transaction, stamp_cost, environment: dict = {}):

        balance = self.executor.driver.get_var(
            contract='currency',
            variable='balances',
            arguments=[transaction['payload']['sender']],
        )

        if balance is None:
            balance = 0

        output = self.executor.execute(
            sender=transaction['payload']['sender'],
            contract_name=transaction['payload']['contract'],
            function_name=transaction['payload']['function'],
            stamps=balance * stamp_cost,
            stamp_cost=stamp_cost,
            kwargs=transaction['payload']['kwargs'],
            environment=environment,
            auto_commit=False,
            metering=True
        )

        self.executor.driver.clear_pending_state()

        writes = [{'key': k, 'value': v}
                    for k, v in output['writes'].items()]

        tx_output = {
            'transaction': transaction,
            'status': output['status_code'],
            'state': writes,
            'stamps_used': output['stamps_used'],
            'result': safe_repr(output['result'])
        }

        tx_output = format_dictionary(tx_output)

        return tx_output

    def execute(self, transaction):
        environment = self.generate_environment()
        stamp_cost = int(self.executor.driver.get_var(contract='stamp_cost', variable='S', arguments=['value']))
        return self.execute_tx(
            transaction = transaction,
            environment = environment,
            stamp_cost = stamp_cost
        )