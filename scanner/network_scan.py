import socket

def scan_network(target):
    devices = []
    base = ".".join(target.split(".")[:-1])

    for i in range(1, 50):
        ip = f"{base}.{i}"
        try:
            socket.gethostbyaddr(ip)
            devices.append(ip)
        except:
            pass
    return devices
