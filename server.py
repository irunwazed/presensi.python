from mitmproxy import ctx
import socket
import json
from datetime import datetime
from mitmproxy import http
import netifaces

LOG_FILE = "log.txt"


def running():
    ips = get_all_local_ips()
    if ips:
        ctx.log.info(f"Mitmproxy running on local IPs: {', '.join(ips)}")
        print(f"Mitmproxy running on local IPs: {', '.join(ips)}")
    else:
        ctx.log.info("Mitmproxy running, but no local IPs found.")
        print("Mitmproxy running, but no local IPs found.")

def get_all_local_ips():
    ips = []
    for iface in netifaces.interfaces():
        addrs = netifaces.ifaddresses(iface)
        ipv4 = addrs.get(netifaces.AF_INET)
        if ipv4:
            for addr in ipv4:
                ip = addr.get('addr')
                if ip and (ip.startswith("192.") or ip.startswith("10.") or ip.startswith("172.")):
                    ips.append(ip)
    return ips

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

    if "/login" in req.path:
        log = separator("=")
        if req.content:
            log += "\n" + try_pretty_json(req.get_text()) + "\n"

        log_to_file(log)
        print(log)
