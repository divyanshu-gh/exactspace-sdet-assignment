# ExactSpace SDET Assignment – Divyanshu

## 📌 Objective

Automate network traffic capture and analysis for the website [https://exactspace.co](https://exactspace.co).  
The goal is to:
- Generate a `.har` file using Selenium
- Parse the `.har` to count total HTTP requests
- Categorize HTTP status codes into 1XX, 2XX, 3XX, 4XX, 5XX
- Generate a JSON summary with percentages (rounded to two decimal places)

---

## 🧰 Tech Stack

- Python 3.x
- Selenium & Selenium-Wire
- Chrome WebDriver
- JSON for output
- argparse for CLI control

---

## 🗂️ Project Structure

```
Divyanshu_SDET/
├── generate_summary.py              # Parses HAR and creates summary JSON
├── network_capture.py               # Captures network traffic and generates HAR
├── har_parser.py                    # HAR parsing logic with categorization
├── requirements.txt                 # Required Python libraries
├── resume.pdf                       # Candidate resume
├── output/
│   ├── captured_YYYY-MM-DD_HH-MM-SS.har   # Generated HAR file
│   └── network_summary.json               # Final required output
```

---

## 🚀 How to Run

### 🔹 Step 1: Install dependencies
```bash
pip install -r requirements.txt
```

### 🔹 Step 2: Capture network traffic
```bash
python network_capture.py --url https://exactspace.co
```

### 🔹 Step 3: Generate summary JSON
```bash
python generate_summary.py
```

---

## 📤 Output

The following files will be created inside the `output/` folder:
- `captured_YYYY-MM-DD_.har` – HAR file of captured requests
- `network_summary.json` – JSON file with status code summary

---


## 🙋 Author

**Divyanshu**  

