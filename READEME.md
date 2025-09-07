# Pico Door Sensor

Simple door security sensor using Raspberry Pi Pico 2W with LED alerts.

## What it does
- Detects when door opens and closes
- Fast LED blink when door opens (alert)
- Slow LED blink when door closes (confirmation)
- Connects to WiFi for future features
- Shows messages in console

## Hardware needed
- Raspberry Pi Pico 2W ($6)
- Magnetic reed switch ($3)
- 2 jumper wires
- **Total cost: ~$9**

## Wiring
```
Reed switch wire 1 → GPIO 18 (pin 24)
Reed switch wire 2 → GND (pin 23)
Built-in LED → GPIO 25 (automatic)
```

## Software setup
1. Install Thonny IDE
2. Configure for Pico 2W: `Run → Configure interpreter → MicroPython (Raspberry Pi Pico)`
3. Copy `door_sensor.py` code into Thonny
4. Update WiFi settings in code (lines 7-8)
5. Save to Pico 2W
6. Run the program

## Code structure
The code uses 2 simple classes:
- **LED class**: Handles blinking patterns
- **DoorSensor class**: Main sensor logic and WiFi

Perfect for learning object-oriented programming!

## How to use
1. Connect hardware as shown above
2. Run the code in Thonny
3. Open and close door to test
4. Watch LED patterns and console messages

## Features
- ✅ Real-time door monitoring
- ✅ Visual LED feedback
- ✅ WiFi connectivity
- ✅ Simple 2-class structure
- ✅ Easy to understand code
- ✅ Perfect for school projects

## Future improvements
- Add webhook notifications
- Multiple sensor support
- Data logging
- Mobile app integration

## Troubleshooting
- **LED not working**: Check Pico 2W power connection
- **Sensor always "open"**: Check reed switch wiring
- **WiFi not connecting**: Verify credentials and use 2.4GHz network

---
**Perfect for IoT class projects and learning MicroPython!**