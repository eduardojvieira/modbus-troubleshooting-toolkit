# RS485 Physical Layer: The "Black Magic" Explained

Most Modbus RTU failures aren't protocol errors—they are physics errors.

## 1. Termination (120Ω)
RS485 is a transmission line. Signal reflections occur if the line isn't terminated.
- **Rule**: Place a 120Ω resistor at the *absolute ends* of the daisy chain.
- **Symptom of missing termination**: "CRC Error" or "Intermittent Timeout" at high baud rates (115200+).

## 2. Fail-Safe Biasing
When no device is transmitting, the bus is "idle." In this state, the differential voltage can float near 0V, causing the receiver to see random bits (noise).
- **Solution**: Pull-up on Data+ (A) and Pull-down on Data- (B).
- **Modern Hardware**: Most industrial gateways (Moxa, Advantech) have internal DIP switches for biasing.

## 3. Grounding (The 3rd Wire)
RS485 is differential, but it has a **Common Mode Voltage** limit (usually -7V to +12V).
- **Mistake**: Using only two wires.
- **Correct**: Use a shielded twisted pair. Connect the shield/ground to the `G` or `SG` terminal of all devices to equalize potential.
