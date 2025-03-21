import json
from collections import defaultdict

def load_har(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def get_category(code):
    if 100 <= code < 200: return "1XX"
    if 200 <= code < 300: return "2XX"
    if 300 <= code < 400: return "3XX"
    if 400 <= code < 500: return "4XX"
    if 500 <= code < 600: return "5XX"
    return "Unknown"

def analyze_data(data):
    summary = defaultdict(int)
    total = 0

    for entry in data:
        code = entry.get("status_code")
        if isinstance(code, int):
            cat = get_category(code)
            summary[cat] += 1
            total += 1

    result = {
        "total_requests": total,
        "status_summary": []
    }

    for cat in ["1XX", "2XX", "3XX", "4XX", "5XX"]:
        count = summary[cat]
        percent = round((count / total) * 100, 2) if total > 0 else 0.00
        result["status_summary"].append({
            "category": cat,
            "count": count,
            "percentage": f"{percent:.2f}"  # ✅ Ensures two decimal places
        })

    return result

def save_summary(data, path):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)
