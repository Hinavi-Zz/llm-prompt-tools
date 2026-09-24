import json,re

def extract_json(text):
    m=re.search(r"\{.*\}",text,re.S)
    if not m: return None
    try: return json.loads(m.group(0))
    except Exception: return None
