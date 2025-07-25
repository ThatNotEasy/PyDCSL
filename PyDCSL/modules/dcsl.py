import requests, json
from PyDCSL.modules.logging import setup_logging

try:
    from rich import print as rprint
    from rich.table import Table
    rich_available = True
except ImportError:
    rich_available = False

def pretty(data):
    res = data.get("responseData", {})
    if not res: return print("No responseData found.")
    if rich_available:
        table = Table(title="Widevine Info", show_lines=False)
        table.add_column("Field", style="cyan"); table.add_column("Value", style="white")
        for k, v in res.items(): table.add_row(k, str(v))
        rprint(table)
    else:
        width = max(len(k) for k in res)
        for k, v in res.items(): print(f"{k:<{width}} : {v}")

def dcsl(wvd_file=None, client_id=None, private_key=None, output=None):
    log = setup_logging()
    url = "https://pari.malam.or.id/dev/widevine/dcsl"
    files = {
        'wvd': open(wvd_file, 'rb') if wvd_file else (None, ''),
        'client_id': open(client_id, 'rb') if client_id else (None, ''),
        'private_key': open(private_key, 'rb') if private_key else (None, '')
    }
    try:
        r = requests.post(url, headers={'accept': 'application/json'}, files=files)
        data = r.json(); pretty(data)
        if output:
            with open(output, "w", encoding="utf-8") as f: json.dump(data, f, indent=2)
            log.info(f"Saved to {output}")
    except Exception as e:
        log.error(f"Error: {e}")
    finally:
        for f in files.values():
            if hasattr(f, 'close'): f.close()
