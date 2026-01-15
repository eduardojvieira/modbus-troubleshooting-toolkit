import asyncio
import struct
from pymodbus.client import AsyncModbusTcpClient
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.constants import Endian

async def decode_float_example(client, address):
    """
    Reads two registers and decodes them as a 32-bit Float.
    Demonstrates handling of Endianness (Byte/Word swapping).
    """
    result = await client.read_holding_registers(address, 2, slave=1)
    if result.isError():
        print(f"Error reading address {address}")
        return

    # Big Endian (Standard)
    decoder = BinaryPayloadDecoder.fromRegisters(
        result.registers,
        byteorder=Endian.BIG,
        wordorder=Endian.BIG
    )
    val = decoder.decode_32bit_float()
    print(f"Decoded Float (Big Endian): {val:.2f}")

async def main():
    # Set timeout for flaky industrial links
    client = AsyncModbusTcpClient('localhost', port=5020, timeout=10)
    
    print("Connecting to Modbus Server...")
    if not await client.connect():
        print("Failed to connect!")
        return

    # 1. Basic Write/Read
    await client.write_register(1, 1234, slave=1)
    res = await client.read_holding_registers(1, 1, slave=1)
    print(f"Register 1: {res.registers[0]}")

    # 2. Float handling
    await decode_float_example(client, 10)

    client.close()

if __name__ == "__main__":
    asyncio.run(main())
