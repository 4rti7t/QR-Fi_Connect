import qrcode
import pyfiglet
from flask import Flask, jsonify, send_file
import os

# Flask setup
app = Flask(__name__)

# Display custom logo
def display_logo():
    logo = pyfiglet.figlet_format("QR-Fi Connect")
    print("\033[92m" + logo + "\033[0m")  # Green text

# Terminal input for Wi-Fi details
def get_wifi_details():
    ssid = input("\033[94m[+] Enter WiFi Name (SSID): \033[0m")
    password = input("\033[94m[+] Enter WiFi Password: \033[0m")
    return ssid, password

# Generate QR code and host it
@app.route('/generate', methods=['GET'])
def generate_wifi_qr():
    ssid, password = get_wifi_details()

    # Generate Wi-Fi QR Code
    wifi_qr_data = f"WIFI:T:WPA;S:{ssid};P:{password};;"
    qr = qrcode.make(wifi_qr_data)
    qr_file = "wifi_qr.png"
    qr.save(qr_file)

    # Print success message
    print("\033[92m[+] QR Code Generated Successfully!\033[0m")
    print(f"\033[93m[+] Hosted Link: http://127.0.0.1:5000/wifi_qr.png\033[0m")
    return jsonify({"link": "http://127.0.0.1:5000/wifi_qr.png"})

# Serve QR code file
@app.route('/wifi_qr.png', methods=['GET'])
def serve_qr_code():
    return send_file("wifi_qr.png", mimetype="image/png")

# Main function to run script
if __name__ == '__main__':
    display_logo()
    print("\033[96m[*] Starting WiFi Linker Tool...\033[0m")
    print("\033[96m[*] Visit: http://127.0.0.1:5000/generate to create a WiFi link.\033[0m")
    
    try:
        app.run(host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        print("\033[91m[!] Exiting...\033[0m")
        if os.path.exists("wifi_qr.png"):
            os.remove("wifi_qr.png")

