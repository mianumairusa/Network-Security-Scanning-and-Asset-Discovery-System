import json

def generate_report(data):
    with open("report.json","w") as f:
        json.dump(data,f,indent=4)
    print("Report saved: report.json")
