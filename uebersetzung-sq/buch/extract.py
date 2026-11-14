import pymupdf, json, re, sys
AR_RE = re.compile('[؀-ۿݐ-ݿﭐ-﷿ﹰ-﻿]')
def extract(path):
    doc = pymupdf.open(path); out = []
    for pno, page in enumerate(doc):
        for bi, d in enumerate(page.get_text('dict')['blocks']):
            if d['type'] != 0: continue
            lines = []
            spans = []
            for ln in d['lines']:
                t = ''.join(('⟪AR⟫' if (AR_RE.search(sp['text']) or ('Arab' in sp['font'] or 'Naskh' in sp['font'] or 'Traditional' in sp['font'])) and sp['text'].strip() else sp['text']) for sp in ln['spans'])
                for sp in ln['spans']:
                    if sp['text'].strip():
                        spans.append(dict(r=list(sp['bbox']), ar=1 if AR_RE.search(sp['text']) else 0, size=sp['size'], font=sp['font'], color=sp['color'], flags=sp['flags']))
                if t.strip(): lines.append(t.strip())
            text = re.sub(r'\s+', ' ', ' '.join(lines)).strip()
            text = re.sub(r'^[••]\s*', '', text)
            if not re.search('[A-Za-z]', text.replace('⟪AR⟫','')): continue
            out.append(dict(p=pno, b=bi, bbox=list(d['bbox']), text=text, spans=spans, nlines=len(d['lines'])))
    return out
if __name__ == '__main__':
    bl = extract(sys.argv[1])
    if len(sys.argv) > 2:
        json.dump(bl, open(sys.argv[2], 'w'), ensure_ascii=False)
    print(len(bl))
