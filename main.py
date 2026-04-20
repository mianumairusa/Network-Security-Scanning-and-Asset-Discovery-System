from scanner.network_scan import scan_network
from scanner.port_scan import scan_ports
from analysis.risk_analysis import analyze_risk
from analysis.ai_analysis import ai_explain
from utils.report import generate_report

def main():
    print("=== NinjaScanner Advanced ===")
    target = input("Enter network (e.g., 192.168.1.1): ")

    devices = scan_network(target)
    results = []

    for device in devices:
        ports = scan_ports(device)
        risk = analyze_risk(ports)
        explanation = ai_explain(ports, risk)

        results.append({
            "ip": device,
            "ports": ports,
            "risk": risk,
            "analysis": explanation
        })

    generate_report(results)

if __name__ == "__main__":
    main()
