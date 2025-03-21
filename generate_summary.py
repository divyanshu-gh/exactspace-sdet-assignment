import os
import json
from datetime import datetime
from har_parser import load_har, analyze_data, save_summary

# DEBUG INFO
print("Current working dir:", os.getcwd())
print("Files in directory:", os.listdir())

# Get the latest .har file in the output folder
har_files = [f for f in os.listdir("output") if f.endswith(".har")]
if not har_files:
    raise FileNotFoundError("❌ No HAR file found in output directory.")
har_file = os.path.join("output", sorted(har_files)[-1])  # Most recent one
print(f"📄 Using HAR file: {har_file}")

# Create output file name with hyphen-based timestamp
timestamp = datetime.now().strftime("%Y-%m-%d")
output_file = os.path.join("output", f"network_summary_{timestamp}.json")

# Load HAR data
data = load_har(har_file)

# Analyze and summarize status codes
summary = analyze_data(data)

# Save final JSON output
save_summary(summary, output_file)

print(f"✅ Summary saved to {output_file}")
