import re, json, sys
src = open(sys.argv[1], encoding='utf-8').read()
out = sys.argv[2]
# split at <script> ... </script>
items = []  # (start, end, text, kind)
def germanish(t):
    if not re.search(r'[A-Za-zÄÖÜäöüß]{2,}', t): return False
    if re.search(r'[ÄÖÜäöüß„“]', t): return True
    if ' ' in t.strip(): return True
    if re.fullmatch(r'[A-ZÄÖÜ][a-zäöüß]+[!?.]?', t.strip()): return True
    return False
for m in re.finditer(r'<script[^>]*>(.*?)</script>', src, re.S):
    s0 = m.start(1); js = m.group(1)
    i = 0
    while i < len(js):
        c = js[i]
        if js.startswith('//', i) and (i == 0 or js[i-1] != ':' ):
            j = js.find('\n', i); i = j if j > 0 else len(js); continue
        if js.startswith('/*', i):
            i = js.find('*/', i) + 2; continue
        if c in '"\'':
            j = i + 1
            while js[j] != c:
                if js[j] == '\\': j += 1
                j += 1
            t = js[i+1:j]
            if germanish(t): items.append((s0+i+1, s0+j, t, 'js'))
            i = j + 1; continue
        if c == '`':
            j = i + 1; depth = 0
            while True:
                if js[j] == '\\': j += 2; continue
                if js.startswith('${', j): depth += 1; j += 2; continue
                if js[j] == '}' and depth: depth -= 1; j += 1; continue
                if js[j] == '`' and not depth: break
                j += 1
            t = js[i+1:j]
            # translate only static pieces? keep whole template, translator keeps ${}
            if germanish(re.sub(r'\$\{[^}]*\}', '', t)): items.append((s0+i+1, s0+j, t, 'tpl'))
            i = j + 1; continue
        i += 1
# html outside scripts/styles: text nodes and some attributes
mask = [(m.start(), m.end()) for m in re.finditer(r'<(script|style)[^>]*>.*?</\1>', src, re.S)]
def inmask(p): return any(a <= p < b for a, b in mask)
for m in re.finditer(r'>([^<>]+)<', src):
    t = m.group(1)
    if inmask(m.start()) or not t.strip(): continue
    if germanish(t): items.append((m.start(1), m.end(1), t, 'html'))
for m in re.finditer(r'\b(title|alt|aria-label|placeholder|content)="([^"]*)"', src):
    if inmask(m.start()): continue
    if germanish(m.group(2)): items.append((m.start(2), m.end(2), m.group(2), 'attr'))
items.sort()
json.dump([dict(s=a, e=b, t=t, k=k) for a, b, t, k in items], open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
print(len(items), sum(len(x[2]) for x in items))
