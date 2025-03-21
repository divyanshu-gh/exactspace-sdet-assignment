import time
import os
import json
from seleniumwire import webdriver
import argparse
from datetime import datetime

parser = argparse.ArgumentParser(description="Capture network traffic from a URL")
parser.add_argument("--url", default="https://exactspace.co", help="URL to visit and capture")
args = parser.parse_args()

OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def capture_traffic():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Looks pro + clean logs
    options.add_argument("--disable-logging")
    options.add_argument("--ignore-certificate-errors")

    driver = webdriver.Chrome(options=options)
    driver.get(args.url)
    time.sleep(12)

    har_data = []
    for req in driver.requests:
        if req.response:
            har_data.append({
                "url": req.url,
                "method": req.method,
                "status_code": req.response.status_code,
                "content_type": req.response.headers.get('Content-Type', '')
            })

    driver.quit()

    # ✅ Timestamp defined before use
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    har_path = os.path.join(OUTPUT_DIR, f"captured_{timestamp}.har")

    with open(har_path, "w") as f:
        json.dump(har_data, f, indent=2)

    print(f"HAR file saved at {har_path}")

if __name__ == "__main__":
    capture_traffic()
