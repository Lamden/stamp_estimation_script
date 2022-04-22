import os
import sys
import socketio
sys.path.append(os.getcwd())
from script.logger import createLogger
from script.executor import TxExecutor
from script.driver import BlockserviceDriver
from contracting.execution.executor import Executor
from contracting.db.driver import ContractDriver
from contracting.db.encoder import decode, encode
from aiohttp import web

logger = createLogger('estimation_script')

def run_server(host="localhost", port=3232, driver = BlockserviceDriver()):

    sio = socketio.AsyncServer()
    app = web.Application()
    sio.attach(app)

    # Executor
    executor = Executor(metering=False, driver=ContractDriver(driver=driver))
    transaction_executor = TxExecutor(executor)

    @sio.event
    async def connect(sid, environ):
        logger.info("connect %s", sid)


    @sio.event
    async def stamps_estimation(sid, data):
        logger.info("client %s, data: %s", sid, data)
        tx = decode(encode(data))
        output = transaction_executor.execute(tx)
        return encode(output)


    @sio.event
    def disconnect(sid):
        logger.info('disconnect %s', sid)

    web.run_app(app, host=host, port=port)
