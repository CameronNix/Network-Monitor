from ping3 import ping
import time

# Devices to check (update IPs to match your network)
devices = {
    "Router": "192.168.1.1",
    "Phone": "224.0.0.22",
    "Laptop": "224.0.0.251"
}

# Ping every 10 seconds
while True:
    print("Checking devices...\n")

    for name, ip in devices.items():
        result = ping(ip, timeout=1)
        
        if result is None:
            print(f"❌ {name} ({ip}) is OFFLINE.")
        else:
            ms = round(result * 1000, 2)
            print(f"✅ {name} ({ip}) is ONLINE. Ping: {ms} ms")

    print("\nWaiting 10 seconds...\n")
    time.sleep(10)