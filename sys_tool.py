# Simple System Info Tool

import platform
import psutil
import os
import socket
from datetime import datetime

# Pick a disk path that works per-OS
if platform.system() == "Windows":
    disk_path = "C:\\"
else:
    disk_path = "/"

def gather_system_info():
    """Return a nicely formatted string of system info."""
    os_name = f"{platform.system()} {platform.release()}"
    cpu = platform.processor() or "Unknown CPU"
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage(disk_path)
    net = psutil.net_if_addrs()
    lines = [
        f"Operating System: {os_name}",
        f"Processor: {cpu}",
        f"RAM: {round(mem.total / (1024 ** 3), 2)} GB",
        f"Storage: {round(disk.total / (1024 ** 3), 2)} GB total",
        f"Network Interfaces: {list(net.keys())}",
    ]
    return "\n".join(lines)

while True:
    print("\n--- System Tool ---")
    print("1) Show system info")
    print("2) Exit")
    print("3) Save system info to file (with timestamp)")
    print("4) Show detailed network info")
    choice = input("Select an option: ").strip()

    if choice == "1":
        print()
        print(gather_system_info())

    elif choice == "3":
        data = gather_system_info()

        # Create timestamped filename
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"system_info_{timestamp}.txt"

        # Save to same folder as script
        filepath = os.path.join(os.getcwd(), filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(data + "\n")

        print(f"\n✅ System info saved as '{filename}'")
        print(f"📂 Full path: {filepath}")
        

    elif choice == "4":
        print("\n--- Network Adapter Details ---")
        try:
            net_info = psutil.net_if_addrs()
            for adapter, details in net_info.items():
                print(f"\nAdapter: {adapter}")
                for item in details:
                    # Use numeric constants from the socket module
                    if item.family == socket.AF_INET:
                        print(f"  IPv4 Address: {item.address}")
                    elif item.family == socket.AF_INET6:
                        print(f"  IPv6 Address: {item.address}")
                    elif hasattr(socket, "AF_PACKET") and item.family == socket.AF_PACKET:
                        print(f"  MAC Address: {item.address}")
                    elif hasattr(socket, "AF_LINK") and item.family == socket.AF_LINK:
                        # macOS uses AF_LINK instead of AF_PACKET
                        print(f"  MAC Address: {item.address}")
        except Exception as e:
            print("Error fetching network details:", e)





    elif choice == "2":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice. Please try again.")
