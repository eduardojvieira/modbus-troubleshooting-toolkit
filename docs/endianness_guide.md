# The Endianness Nightmare: A Practical Guide

In Modbus, a "Holding Register" is 16 bits. But industrial data (Floats, 32-bit Integers) often spans multiple registers. Since there is no official standard for the order of these bytes/words, we get **Endianness Hell**.

## 1. The Combinations

Imagine a 32-bit hex value `0x12345678` (represented as 4 bytes: `12 34 56 78`).

| Format | Byte Order | Word Order | Resulting Sequence |
| :--- | :--- | :--- | :--- |
| **Big Endian** | Big | Big | `12 34 56 78` (Standard) |
| **Little Endian** | Little | Little | `78 56 34 12` |
| **Mid-Big Endian** | Big | Little | `56 78 12 34` (Word Swapped) |
| **Mid-Little Endian** | Little | Big | `34 12 78 56` (Byte Swapped) |

## 2. Python Solution (struct)

Using Python's built-in `struct` module is the cleanest way to handle this.

```python
import struct

# Raw registers from Modbus: [0x1234, 0x5678]
regs = [4660, 22136] 

# Convert to 4 bytes (Big Endian)
raw_bytes = struct.pack('>HH', *regs)

# Unpack as Float (Big Endian)
val_be = struct.unpack('>f', raw_bytes)[0]

# Unpack as Float (Little Endian / Word Swap)
val_le = struct.unpack('<f', raw_bytes)[0]
```

## 3. Pymodbus BinaryPayloadDecoder

Pymodbus provides a high-level wrapper:

```python
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.constants import Endian

decoder = BinaryPayloadDecoder.fromRegisters(
    regs, 
    byteorder=Endian.BIG, 
    wordorder=Endian.LITTLE
)
print(decoder.decode_32bit_float())
```
