import socket

def scan_ports(ip):
    open_ports = []
    ports = range(20, 1025)

    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        if s.connect_ex((ip, port)) == 0:
            open_ports.append(port)
        s.close()

    return open_ports
