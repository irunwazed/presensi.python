# intercept.py
from mitmproxy import http
import json
from datetime import datetime

LOG_FILE = "log.txt"

def separator(char="-", length=80):
    return char * length + "\n"

def format_headers(headers: dict) -> str:
    return "\n".join(f"{k}: {v}" for k, v in headers.items())

def try_pretty_json(text: str) -> str:
    try:
        return json.dumps(json.loads(text), indent=2)
    except:
        return text

def log_to_file(data: str):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(data)

def request(flow: http.HTTPFlow) -> None:
    req = flow.request
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    log = separator("=")
    log += f"[{timestamp}] >>> HTTP REQUEST <<<\n"
    log += separator()
    log += f"{req.method} {req.path} HTTP/1.1\n"
    log += f"Host: {req.host}\n"
    log += format_headers(req.headers) + "\n"

    if req.content:
        log += "\n" + try_pretty_json(req.get_text()) + "\n"

    log_to_file(log)
    print(log)

def response(flow: http.HTTPFlow) -> None:
    res = flow.response
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log = separator()
    log += f"[{timestamp}] <<< HTTP RESPONSE <<<\n"
    log += separator()
    log += f"HTTP/1.1 {res.status_code} {res.reason}\n"
    log += format_headers(res.headers) + "\n"

    if res.content:
        log += "\n" + try_pretty_json(res.get_text()) + "\n"

    log += separator("=") + "\n\n"

    log_to_file(log)
    print(log)
