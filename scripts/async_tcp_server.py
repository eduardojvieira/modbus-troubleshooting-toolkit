import asyncio
import logging
from pymodbus.server import StartAsyncTcpServer
from pymodbus.datastore import (
    ModbusSequentialDataBlock,
    ModbusDeviceContext,
    ModbusServerContext,
)

# Configure logging for industrial diagnostics
logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)

class MonitoringDataBlock(ModbusSequentialDataBlock):
    """
    A custom datablock that logs every read and write operation.
    Essential for debugging SCADA polling behavior.
    """
    def setValues(self, address, values):
        super().setValues(address, values)
        _logger.info(f"MODBUS WRITE - Address: {address}, Values: {values}")

    def getValues(self, address, count=1):
        values = super().getValues(address, count)
        _logger.info(f"MODBUS READ - Address: {address}, Count: {count}")
        return values

async def run_server():
    # Initialize 100 registers with zeros
    store = ModbusDeviceContext(
        di=ModbusSequentialDataBlock(0, [0]*100),
        co=ModbusSequentialDataBlock(0, [0]*100),
        hr=MonitoringDataBlock(0, [0]*100),
        ir=ModbusSequentialDataBlock(0, [0]*100),
    )
    context = ModbusServerContext(devices=store, single=True)

    _logger.info("Starting Modbus TCP Server on 0.0.0.0:5020...")
    await StartAsyncTcpServer(
        context=context,
        address=("0.0.0.0", 5020)
    )

if __name__ == "__main__":
    try:
        asyncio.run(run_server())
    except KeyboardInterrupt:
        _logger.info("Server stopped.")
