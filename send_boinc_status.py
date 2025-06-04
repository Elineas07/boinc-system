import requests
import socket
import time
import json
import subprocess
from datetime import datetime

# Sett IP til Windows-serveren
SERVER_URL = "http://172.31.1.34:5000/boinc-update"

# Simulert henting – her kan du bruke ekte BOINC GUI RPC-kall
def get_boinc_data():
    cmd = r"C:\Program Files\BOINC\boinccmd.exe"
    result = subprocess.run([cmd, "--get_simple_gui_info"], capture_output=True, text=True)
    return {
        "hostname": socket.gethostname(),
        "timestamp": datetime.now().isoformat(),
        "status": result.stdout,
        "error": "",  # Sett inn feilmeldinger her hvis noen
    }


def send_data():
    data = get_boinc_data()
    try:
        r = requests.post(SERVER_URL, json=data)
        print(f"Status: {r.status_code}, Response: {r.text}")
    except Exception as e:
        print(f"Feil under sending: {e}")

if __name__ == "__main__":
    send_data()
