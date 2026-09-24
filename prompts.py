import re

def render(template,**kw):
    def rep(m):
        k=m.group(1).strip()
        return str(kw.get(k,m.group(0)))
    return re.sub(r"\{\{\s*(\w+)\s*\}\}",rep,template)

def truncate(text,n=4000):
    return text if len(text)<=n else text[:n]+"..."
