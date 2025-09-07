# Simple Door Sensor with 2 Classes for Pico 2W
# Easy to understand, perfect for school projects!

from machine import Pin
import time
import network

# Change this to your WiFi info
WIFI_NAME = "FIU_Public_Wifi"
WIFI_PASSWORD = "OrangePanther"

class LED:
    """Simple LED class for visual feedback"""
    
    def __init__(self):
        """Set up the built-in LED"""
        self.led = Pin(25, Pin.OUT)
    
    def blink_fast(self):
        """Fast blink for door open alert"""
        for _ in range(8):
            self.led.on()
            time.sleep(0.1)
            self.led.off()
            time.sleep(0.1)
    
    def blink_slow(self):
        """Slow blink for door closed confirmation"""
        for _ in range(3):
            self.led.on()
            time.sleep(0.4)
            self.led.off()
            time.sleep(0.3)

class DoorSensor:
    """Main door sensor class that controls everything"""
    
    def __init__(self):
        """Set up the door sensor system"""
        self.sensor = Pin(18, Pin.IN, Pin.PULL_UP)  # Reed switch on pin 18
        self.led = LED()                            # Create LED controller
        self.last_state = None                      # Track door state changes
        
        print("🚪 Door Sensor Ready!")
        print("Connect reed switch to pin 18 and ground")
    
    def connect_wifi(self):
        """Connect to WiFi network"""
        if WIFI_NAME != "YourWiFi":
            try:
                wifi = network.WLAN(network.STA_IF)
                wifi.active(True)
                print(f"Connecting to {WIFI_NAME}...")
                wifi.connect(WIFI_NAME, WIFI_PASSWORD)
                time.sleep(5)
                
                if wifi.isconnected():
                    ip = wifi.ifconfig()[0]
                    print(f"✅ WiFi connected: {ip}")
                else:
                    print("❌ WiFi connection failed")
            except Exception as e:
                print(f"❌ WiFi error: {e}")
        else:
            print("⚠️ Update WiFi settings in code")
    
    def is_door_open(self):
        """Check if door is currently open"""
        return self.sensor.value() == 1
    
    def run(self):
        """Main monitoring loop"""
        # Connect to WiFi first
        self.connect_wifi()
        
        print("\n🔍 Monitoring door...")
        print("🛑 Press Ctrl+C to stop")
        
        try:
            while True:
                # Check current door state
                door_open = self.is_door_open()
                
                # Only act if state changed
                if door_open != self.last_state:
                    if door_open:
                        print("🚨 DOOR OPENED!")
                        self.led.blink_fast()
                    else:
                        print("✅ Door closed")
                        self.led.blink_slow()
                    
                    # Remember new state
                    self.last_state = door_open
                
                # Small delay to prevent excessive CPU usage
                time.sleep(0.1)
                
        except KeyboardInterrupt:
            print("\n🛑 Sensor stopped by user")
            print("✅ Program ended")

# Create and run the door sensor
print("🎯 Pico 2W Door Sensor")
print("🎓 School Project Edition")
print("=" * 30)

sensor = DoorSensor()
sensor.run()
