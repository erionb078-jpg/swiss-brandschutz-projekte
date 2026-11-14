import json, sys, re, importlib
src, items_f, mod, out = sys.argv[1:5]
M = importlib.import_module(mod)
s = open(src, encoding='utf-8').read()
items = json.load(open(items_f, encoding='utf-8'))
miss = []
for it in sorted(items, key=lambda x: -x['s']):
    t = it['t']
    if t in M.D: s = s[:it['s']] + M.D[t] + s[it['e']:]
    elif t in M.SKIP or t.startswith(M.SKIP_PREFIX): pass
    else: miss.append(t)
for a, b in getattr(M, 'EXTRA', []):
    n = s.count(a)
    if n == 0: miss.append('EXTRA-NOTFOUND: ' + a)
    s = s.replace(a, b)
open(out, 'w', encoding='utf-8').write(s)
print('missing:', len(miss)); [print('  ', repr(m[:120])) for m in miss]
