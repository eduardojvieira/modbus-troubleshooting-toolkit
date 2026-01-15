# Modbus Troubleshooting Toolkit 🛠️

A collection of professional-grade tools and scripts for commissioning, debugging, and simulating Modbus RTU (Serial) and TCP (Ethernet) networks.

## Contents

- **`scripts/`**: Functional Python scripts based on `pymodbus`.
  - `async_tcp_server.py`: Simulates a robust PLC/Gateway.
  - `async_tcp_client.py`: High-performance client with byte-swapping (Endianness) support.
  - `rtu_serial_scanner.py`: Brute-force scanner for Modbus RTU Slave IDs.
- **`docs/`**: Deep technical references.
  - `wiring_rs485.md`: The physics of RS485 (Termination, Biasing).
  - `endianness_guide.md`: Mastering the "Byte-Swap" nightmare.

## Installation

```bash
pip install pymodbus pyserial
```

## Quick Start (Simulator)

Run the async server to simulate a device:
```bash
python scripts/async_tcp_server.py
```
