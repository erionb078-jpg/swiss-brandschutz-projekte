import json, re, sys, html as H
import pymupdf
sys.path.insert(0, '/tmp/claude-0/-home-claude/133ba4ae-4316-560e-9041-7dc80082bb1c/scratchpad/sqbook')
from tr_sq import T, R, FORCE, SHIFT, SPANMODE, SR

S = '/tmp/claude-0/-home-claude/133ba4ae-4316-560e-9041-7dc80082bb1c/scratchpad'
SRC = f'{S}/sqbook/src3.pdf'
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{S}/sqbook/Abrar_Kurani_SQ.pdf'
ONLY = set(int(x) for x in sys.argv[2].split(',')) if len(sys.argv) > 2 else None
FD = f'{S}/fontwork'

blocks = json.load(open(f'{S}/sqbook/blocks.json'))
idx = {}
for ln in open(f'{S}/sqbook/unique.txt', encoding='utf-8'):
    i, pages, text = ln.rstrip('\n').split('\t', 2)
    idx[text] = int(i)

CSS = """
@font-face{font-family:L3;src:url(lato/lato-300-normal.ttf)}
@font-face{font-family:L3i;src:url(lato/lato-300-italic.ttf)}
@font-face{font-family:L4;src:url(lato/lato-400-normal.ttf)}
@font-face{font-family:L7;src:url(lato/lato-700-normal.ttf)}
@font-face{font-family:AR;src:url(naskh.ttf)}
* {margin:0;padding:0}
.ar{font-family:AR}
"""
ARCH = pymupdf.Archive(FD)
F = {k: pymupdf.Font(fontfile=f'{FD}/lato/{v}') for k, v in
     dict(L3='lato-300-normal.ttf', L4='lato-400-normal.ttf').items()}

AR_RE = re.compile('[؀-ۿݐ-ݿﭐ-﷿ﹰ-﻿]')

def fam(font):
    f = font.lower()
    if 'italic' in f: return 'L3i'
    if 'bold' in f or 'black' in f: return 'L7'
    if 'light' in f: return 'L3'
    return 'L4'

def hexc(c): return '#%06x' % c

def is_keep_dict(sp):
    t = sp['text']
    if sp['size'] > 20 and not AR_RE.search(t) and t.strip() in R: return False
    return sp['size'] > 20 or 'Wingdings' in sp['font'] or (sp['size'] > 14 and AR_RE.search(t))

def is_keep_json(s):
    return (s['ar'] and s['size'] > 14) or s['size'] > 20 or 'Wingdings' in s['font']

def markup(t, base, head):
    out = t
    out = re.sub(r'<h>(.*?)</h>', lambda m: f'<span style="font-family:{head[0]};font-size:{head[1]:.1f}px;color:{head[2]}">{m.group(1)}</span><br>', out)
    out = re.sub(r'<k c=(\d+)>(.*?)</k>', lambda m: f'<span style="color:{hexc(int(m.group(1)))}">{m.group(2)}</span>', out)
    out = re.sub(r'<ar>(.*?)</ar>', lambda m: f'<span class="ar" dir="rtl">{m.group(1)}</span>', out)
    out = out.replace('<sup>', f'<span style="font-size:{base[1]*0.62:.1f}px;vertical-align:super">').replace('</sup>', '</span>')
    out = out.replace('<i>', '<span style="font-family:L3i">').replace('</i>', '</span>')
    return out

def fit(page, rect, htmltext, css, maxgrow=0.0):
    r = pymupdf.Rect(rect)
    for grow in (0, 0.15, 0.3):
        if grow > maxgrow + 1e-9: break
        rr = pymupdf.Rect(r.x0, r.y0, r.x1, r.y1 + r.height * grow)
        # probe on a scratch doc to decide
        tmp = pymupdf.open(); tp = tmp.new_page(width=page.rect.width, height=page.rect.height)
        spare, scale = tp.insert_htmlbox(rr, htmltext, css=css, scale_low=0.72, archive=ARCH)
        tmp.close()
        if spare >= 0:
            return page.insert_htmlbox(rr, htmltext, css=css, scale_low=0.72, archive=ARCH)
    return page.insert_htmlbox(rr, htmltext, css=css, scale_low=0.4, archive=ARCH)

doc = pymupdf.open(SRC)
todo = {}  # page -> list of (rect, html, css, grow)
missR = set(); report = []
for bi, x in enumerate(blocks):
    if ONLY and x['p'] not in ONLY: continue
    tid = idx.get(x['text'])
    page = doc[x['p']]
    dblocks = page.get_text('dict')['blocks']
    d = dblocks[x['b']]
    assert abs(d['bbox'][0] - x['bbox'][0]) < 0.5, (bi, d['bbox'], x['bbox'])
    spans = [sp for ln in d['lines'] for sp in ln['spans']]
    jobs = todo.setdefault(x['p'], [])
    if tid in SPANMODE:
        for sp in spans:
            k = sp['text'].strip()
            if k not in SR: continue
            r = pymupdf.Rect(sp['bbox']); f = F['L4']
            tw = f.text_length(SR[k], fontsize=sp['size']*0.8) + 6
            cx = (r.x0 + r.x1) / 2; half = max(r.width, tw) / 2
            box = pymupdf.Rect(cx - half, r.y0 - 1, cx + half, r.y1 + 3)
            css = CSS + f"body{{font-family:L4;font-size:{sp['size']*0.8:.1f}px;color:{hexc(sp['color'])};line-height:1.15;text-align:center}}"
            jobs.append(('redact', [sp['bbox']]))
            jobs.append(('text', box, H.escape(SR[k]), css, 0))
        continue
    if tid not in FORCE and any(is_keep_json(s) for s in x['spans']):
        # Lauf-Modus
        for ln in d['lines']:
            sps = ln['spans']; run = []
            def flush(run, nxt_x):
                if not run: return
                txt = ''.join(s['text'] for s in run).strip()
                if not txt: return
                if txt not in R:
                    if re.search('[A-Za-z]{3,}', txt): missR.add(txt)
                    return
                rr = pymupdf.Rect(run[0]['bbox'])
                for s in run: rr |= pymupdf.Rect(s['bbox'])
                s0 = max(run, key=lambda s: len(s['text']))
                right = nxt_x if nxt_x is not None else max(rr.x1, d['bbox'][2]) + 30
                box = pymupdf.Rect(rr.x0, rr.y0 - 1, max(rr.x1, right) , rr.y1 + 2)
                css = CSS + f"body{{font-family:{fam(s0['font'])};font-size:{s0['size']:.1f}px;color:{hexc(s0['color'])};line-height:1.15}}"
                jobs.append(('redact', [s['bbox'] for s in run]))
                jobs.append(('text', box, H.escape(R[txt]), css, 0))
            for k, sp in enumerate(sps):
                if is_keep_dict(sp):
                    flush(run, sp['bbox'][0] - 1); run = []
                else:
                    run.append(sp)
            flush(run, None)
        continue
    if tid is None or tid not in T:
        continue
    t = T[tid]
    latin = [sp for sp in spans if not AR_RE.search(sp['text']) and sp['text'].strip()]
    if not latin: latin = spans
    base_sp = max(latin, key=lambda s: len(s['text']))
    head_sp = max(latin, key=lambda s: s['size'])
    base = (fam(base_sp['font']), base_sp['size'], hexc(base_sp['color']))
    head = (fam(head_sp['font']), head_sp['size'], hexc(head_sp['color']))
    bb = pymupdf.Rect(d['bbox'])
    # Ausrichtung
    lines = [pymupdf.Rect(l['bbox']) for l in d['lines'] if ''.join(s['text'] for s in l['spans']).strip()]
    cx = (bb.x0 + bb.x1) / 2
    align = 'left'
    if len(lines) > 1 and max(l.x0 for l in lines) - min(l.x0 for l in lines) > 6 and all(abs((l.x0 + l.x1) / 2 - cx) < 5 for l in lines):
        align = 'center'
    elif len(lines) == 1 and abs(cx - page.rect.width / 2) < 6 and bb.x0 > 90:
        align = 'center'
    nl = max(1, len(lines))
    lh = 1.2
    if nl > 1:
        lh = max(1.05, min(1.7, (bb.height / nl) / base[1]))
    if t.startswith('TOC:'):
        title = t[4:]
        num = re.search(r'(\d+)\s*$', x['text']).group(1)
        f = F['L3' if base[0] == 'L3' else 'L4']
        w = bb.width - 4
        tw = f.text_length(title + '  ' + num, fontsize=base[1])
        dw = f.text_length('.', fontsize=base[1])
        n = max(3, int((w - tw) / dw))
        body = H.escape(title) + ' ' + '.' * n + ' ' + num
        grow = 0
    else:
        body = markup(t, base, head)
        grow = 0.3
    css = CSS + f"body{{font-family:{base[0]};font-size:{base[1]:.1f}px;color:{base[2]};line-height:{lh:.2f};text-align:{align}}}"
    jobs.append(('redact', [sp['bbox'] for sp in spans]))
    box = pymupdf.Rect(bb.x0, bb.y0 - 1, bb.x1 + 3, bb.y1 + 2)
    if tid in SHIFT: box.y0 += 8; box.y1 += 8
    if nl == 1 and not t.startswith('TOC:'):
        plain = re.sub(r'<ar>.*?</ar>', 'xx', t); plain = re.sub(r'<[^>]+>', '', plain)
        tw = F['L3' if base[0] == 'L3' else 'L4'].text_length(plain, fontsize=base[1]) + 6
        if '<h>' not in t and tw > box.width:
            lim = page.rect.width - 40
            if align == 'center':
                half = min(tw / 2, cx - 40, lim - cx)
                box = pymupdf.Rect(cx - half, box.y0, cx + half, box.y1)
            else:
                box.x1 = min(lim, box.x0 + tw)
            grow = 0
    jobs.append(('text', box, body, css, grow))

for pno, jobs in todo.items():
    page = doc[pno]
    for j in jobs:
        if j[0] == 'redact':
            for r in j[1]:
                r = pymupdf.Rect(r)
                h = r.height
                page.add_redact_annot(pymupdf.Rect(r.x0 + 0.2, r.y0 + h * 0.3, r.x1 - 0.2, r.y1 - h * 0.3), fill=False)
    page.apply_redactions(images=pymupdf.PDF_REDACT_IMAGE_NONE, graphics=pymupdf.PDF_REDACT_LINE_ART_NONE, text=pymupdf.PDF_REDACT_TEXT_REMOVE)
    for j in jobs:
        if j[0] == 'text':
            _, box, body, css, grow = j
            sp, sc = fit(page, box, body, css, grow)
            if sc < 0.8: report.append((pno + 1, round(sc, 2), body[:50]))

doc.subset_fonts()
doc.save(OUT, garbage=4, deflate=True)
print('saved', OUT)
print('missing R:', missR)
for r in report: print('small', r)
