# Generates the animated hero scene: a teacher reading the Abrar book with four children around him.
def kid(x,y,s,skin,cloth,legs,head,headc,look,book,nod_begin,raise_hand=False):
    o=[f'<g transform="translate({x} {y}) scale({s})">']
    o.append(f'<ellipse cx="0" cy="-8" rx="44" ry="14" fill="{legs}"/>')
    o.append(f'<path d="M-30-8C-31-46-22-70 0-74C22-70 31-46 30-8Z" fill="{cloth}"/>')
    if raise_hand:
        o.append(f'''<g opacity="0"><animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;.35;.42;.78;.85;1" dur="7s" repeatCount="indefinite"/>
<g><animateTransform attributeName="transform" type="rotate" values="-120 -20 -60;-120 -20 -60;0 -20 -60;-8 -20 -60;4 -20 -60;-6 -20 -60;-120 -20 -60;-120 -20 -60" keyTimes="0;.35;.45;.55;.62;.72;.85;1" dur="7s" repeatCount="indefinite"/>
<path d="M-20-60L-30-128" stroke="{cloth}" stroke-width="12" stroke-linecap="round"/><circle cx="-31" cy="-133" r="7.5" fill="{skin}"/></g></g>''')
    o.append('<g><animateTransform attributeName="transform" type="rotate" values="0 0 -76;5 0 -76;0 0 -76;0 0 -76;-3 0 -76;0 0 -76" keyTimes="0;.12;.25;.6;.75;1" dur="3.6s" begin="%ss" repeatCount="indefinite"/>'%nod_begin)
    if head=='hijab':
        o.append(f'<path d="M-31-100C-35-70-26-60 0-56C26-60 35-70 31-100A31 31 0 0 0-31-100Z" fill="{headc}"/>')
        o.append(f'<ellipse cx="{look*.6}" cy="-98" rx="19" ry="21" fill="{skin}"/>')
    else:
        o.append(f'<circle cx="0" cy="-100" r="24" fill="{skin}"/>')
        if head=='kufi':
            o.append(f'<path d="M-22-110Q-21-132 0-132Q21-132 22-110Z" fill="{headc}"/><path d="M-22-110H22" stroke="#e8d9e1" stroke-width="2"/>')
        else:
            o.append(f'<path d="M-25-102Q-25-130 0-130Q25-130 25-102Q14-116 2-114Q-10-120-25-102Z" fill="{headc}"/>')
        o.append(f'<circle cx="-24" cy="-98" r="5" fill="{skin}"/><circle cx="24" cy="-98" r="5" fill="{skin}"/>' if head!='kufi' else '')
    for ex in (-8,8):
        o.append(f'<ellipse cx="{ex+look}" cy="-101" rx="2.9" ry="3.4" fill="#2a1823"><animate attributeName="ry" values="3.4;3.4;.4;3.4" keyTimes="0;.93;.96;1" dur="{4+nod_begin}s" repeatCount="indefinite"/></ellipse>')
    o.append(f'<circle cx="{-13+look}" cy="-91" r="4" fill="#ff8a8a" opacity=".4"/><circle cx="{13+look}" cy="-91" r="4" fill="#ff8a8a" opacity=".4"/>')
    o.append(f'<path d="M{-6+look}-90Q{look}-84 {6+look}-90" fill="none" stroke="#7a2e2e" stroke-width="2.2" stroke-linecap="round"/>')
    o.append('</g>')
    o.append(f'<path d="M-27-31L0-26L27-31L27-12L0-7L-27-12Z" fill="#fffaf6" stroke="{book}" stroke-width="3" stroke-linejoin="round"/><path d="M0-26V-7" stroke="{book}" stroke-width="2"/>')
    o.append(f'<path d="M-20-24h12M-20-19h10M8-24h12M10-19h10" stroke="#c9b6c1" stroke-width="2" stroke-linecap="round"/>')
    o.append(f'<circle cx="-26" cy="-15" r="6" fill="{skin}"/><circle cx="26" cy="-15" r="6" fill="{skin}"/>')
    o.append('</g>')
    return ''.join(o)

AR='font-family="Noto Naskh Arabic,Geeza Pro,serif" font-weight="700"'
def scene():
    o=['<svg class="scene-svg" viewBox="0 0 560 500" role="img" aria-labelledby="scnT"><title id="scnT">A teacher reads the Abrar book with four children</title>']
    o.append('<circle cx="280" cy="250" r="232" fill="var(--tint-2)"/>')
    # arch window
    o.append('<path d="M196 262V128Q196 66 280 42Q364 66 364 128V262Z" fill="#fff" opacity=".6"/><path d="M212 262V132Q212 82 280 60Q348 82 348 132V262" fill="none" stroke="#e7cfdc" stroke-width="3"/>')
    # sparkles
    for (sx,sy,b,c) in [(70,150,0,'#e8a821'),(492,120,1.2,'#13877c'),(470,250,2.1,'#d6303a'),(96,262,.6,'#13877c')]:
        o.append(f'<path d="M{sx} {sy-9}L{sx+2.5} {sy-2.5}L{sx+9} {sy}L{sx+2.5} {sy+2.5}L{sx} {sy+9}L{sx-2.5} {sy+2.5}L{sx-9} {sy}L{sx-2.5} {sy-2.5}Z" fill="{c}"><animate attributeName="opacity" values=".15;1;.15" dur="2.6s" begin="{b}s" repeatCount="indefinite"/></path>')
    # lantern
    o.append('<g><animateTransform attributeName="transform" type="rotate" values="-7 128 0;7 128 0;-7 128 0" dur="4.5s" repeatCount="indefinite" calcMode="spline" keySplines=".45 0 .55 1;.45 0 .55 1"/>'
             '<path d="M128 0V52" stroke="#c9a46a" stroke-width="2"/><path d="M118 52h20l-3 6h-14z" fill="#e8a821"/>'
             '<path d="M116 58h24l4 34h-32z" fill="#ffe7a3" stroke="#e8a821" stroke-width="3" stroke-linejoin="round"/>'
             '<ellipse cx="128" cy="76" rx="6" ry="9" fill="#ffb347"><animate attributeName="ry" values="9;7;9.5;8;9" dur="1.3s" repeatCount="indefinite"/></ellipse>'
             '<path d="M110 92h36l-6 8h-24z" fill="#e8a821"/></g>')
    # rug
    o.append('<ellipse cx="280" cy="436" rx="262" ry="58" fill="#13877c" opacity=".16"/><ellipse cx="280" cy="436" rx="232" ry="44" fill="none" stroke="#13877c" stroke-width="2.5" stroke-dasharray="2 9" stroke-linecap="round" opacity=".55"/>')
    # back kids
    o.append(kid(98,380,.92,'#f1c7a4','#7cc7bb','#4f9d92','hijab','#13877c',4,'#d6303a',0))
    o.append(kid(462,380,.92,'#c98b62','#ee7a2b','#b85a1c','hair','#3a2418',-4,'#e8a821',1.1))
    # teacher
    o.append('<ellipse cx="280" cy="352" rx="94" ry="27" fill="#4e1539"/>')
    o.append('<path d="M220 354C218 290 232 230 280 220C328 230 342 290 340 354Z" fill="#6b2150"/>')
    o.append('<path d="M264 222L280 248L296 222Z" fill="#fff"/>')
    o.append('<g><animateTransform attributeName="transform" type="rotate" values="0 280 214;-3 280 214;0 280 214;3 280 214;0 280 214" dur="6s" repeatCount="indefinite"/>')
    o.append('<circle cx="280" cy="178" r="34" fill="#e2a77f"/><circle cx="246" cy="180" r="6" fill="#e2a77f"/><circle cx="314" cy="180" r="6" fill="#e2a77f"/>')
    o.append('<path d="M247 170Q248 136 280 134Q312 136 313 170Z" fill="#fff"/><path d="M247 166Q280 160 313 166" fill="none" stroke="#e8d9e1" stroke-width="2.5"/>')
    o.append('<path d="M248 184Q250 224 280 228Q310 224 312 184Q302 202 280 203Q258 202 248 184Z" fill="#5b3a2a"/>')
    o.append('<path d="M263 192Q280 186 297 192" fill="none" stroke="#5b3a2a" stroke-width="5" stroke-linecap="round"/>')
    o.append('<ellipse cx="280" cy="201" rx="6.5" ry="2" fill="#3a1a12"><animate attributeName="ry" values="1.5;4;2;4.6;1.8;3.6;1.5;1.5" keyTimes="0;.1;.2;.3;.4;.5;.6;1" dur="2s" repeatCount="indefinite"/></ellipse>')
    o.append('<path d="M260 166q7-4 13 0M287 166q7-4 13 0" fill="none" stroke="#5b3a2a" stroke-width="2.6" stroke-linecap="round"/>')
    for ex in (267,293):
        o.append(f'<ellipse cx="{ex}" cy="176" rx="3.6" ry="4" fill="#2a1823"><animate attributeName="ry" values="4;4;.5;4" keyTimes="0;.94;.97;1" dur="5s" repeatCount="indefinite"/></ellipse>')
    o.append('<circle cx="257" cy="187" r="5" fill="#ff8a8a" opacity=".35"/><circle cx="303" cy="187" r="5" fill="#ff8a8a" opacity=".35"/></g>')
    # sleeves to the book
    o.append('<path d="M236 262Q214 286 212 306M324 262Q350 290 364 316" fill="none" stroke="#6b2150" stroke-width="20" stroke-linecap="round"/>')
    # open book
    o.append('<path d="M196 248L280 262L364 248L366 314L280 326L194 314Z" fill="#d6303a"/>')
    o.append('<path d="M204 252L280 265L280 318L202 308Z" fill="#fffaf6"/><path d="M356 252L280 265L280 318L358 308Z" fill="#fffaf6"/><path d="M280 265V318" stroke="#e8d9e1" stroke-width="2"/>')
    # letters on right page (read right to left) with highlight
    slots=[('ا',340,'#6b2150'),('ب',318,'#d6303a'),('ت',296,'#13877c')]
    for i,(ch,lx,c) in enumerate(slots):
        kt=['0','.333','.667','1']
        vals=['0']*4
        vals_str=';'.join(['1' if j==i else '0' for j in range(3)]+['1' if i==0 else '0'])
        o.append(f'<circle cx="{lx}" cy="288" r="12" fill="#ffe08a"><animate attributeName="opacity" values="{vals_str}" keyTimes="0;.333;.667;1" calcMode="discrete" dur="6s" repeatCount="indefinite"/></circle>')
        o.append(f'<text x="{lx}" y="296" text-anchor="middle" font-size="22" fill="{c}" {AR}>{ch}</text>')
    o.append(f'<text x="242" y="296" text-anchor="middle" font-size="20" fill="#13877c" {AR} opacity=".85">ث ج</text>')
    o.append('<path d="M214 306h56M292 306h56" stroke="#e8d9e1" stroke-width="2" stroke-linecap="round"/>')
    # pointer stick held in the right hand
    o.append('<line x1="372" y1="322" x2="342" y2="304" stroke="#8a5a2b" stroke-width="3.5" stroke-linecap="round">'
             '<animate attributeName="x2" values="342;342;320;320;298;298;342" keyTimes="0;.28;.36;.61;.69;.94;1" dur="6s" repeatCount="indefinite"/>'
             '<animate attributeName="y2" values="304;304;306;306;306;306;304" keyTimes="0;.28;.36;.61;.69;.94;1" dur="6s" repeatCount="indefinite"/></line>')
    o.append('<circle cx="208" cy="310" r="10" fill="#e2a77f"/><circle cx="368" cy="320" r="10" fill="#e2a77f"/>')
    # floating letters rising from the book
    for i,(ch,sx,dx,c) in enumerate([('أ',214,-80,'#e8a821'),('ب',346,70,'#d6303a'),('ت',226,-40,'#13877c'),('ث',334,100,'#6b2150'),('ج',206,-110,'#ee7a2b')]):
        b=i*1.4
        o.append(f'<text x="{sx}" y="244" text-anchor="middle" font-size="30" fill="{c}" {AR} opacity="0">{ch}'
                 f'<animate attributeName="opacity" values="0;1;1;0" keyTimes="0;.15;.7;1" dur="7s" begin="{b}s" repeatCount="indefinite"/>'
                 f'<animateTransform attributeName="transform" type="translate" values="0 0;{dx} -130" dur="7s" begin="{b}s" repeatCount="indefinite"/></text>')
    # speech bubble, synced with the highlighted letter
    o.append('<g transform="translate(352 96)"><path d="M0 0h64a14 14 0 0 1 14 14v28a14 14 0 0 1-14 14H26l-16 14 4-14H0a14 14 0 0 1-14-14V14A14 14 0 0 1 0 0Z" fill="#fff" stroke="#e7cfdc" stroke-width="2.5"/>')
    for i,(ch,lat) in enumerate([('اَ','a'),('بَ','ba'),('تَ','ta')]):
        vals=';'.join(['1' if j==i else '0' for j in range(3)]+['1' if i==0 else '0'])
        o.append(f'<g opacity="0"><animate attributeName="opacity" values="{vals}" keyTimes="0;.333;.667;1" calcMode="discrete" dur="6s" repeatCount="indefinite"/>'
                 f'<text x="18" y="40" text-anchor="middle" font-size="28" fill="#6b2150" {AR}>{ch}</text>'
                 f'<text x="52" y="38" text-anchor="middle" font-size="18" fill="#13877c" font-family="Lexend,system-ui,sans-serif" font-weight="700">{lat}</text></g>')
    o.append('</g>')
    # closed book with the real cover on the rug
    o.append('<g transform="translate(250 402) rotate(-7)"><rect x="4" y="6" width="66" height="93" rx="4" fill="#000" opacity=".15"/>'
             '<rect x="-4" y="0" width="8" height="93" rx="3" fill="#4e1539"/>'
             '<image href="buch/pages/001.webp" x="0" y="0" width="66" height="93" preserveAspectRatio="xMidYMid slice"/>'
             '<rect x="0" y="0" width="66" height="93" rx="2" fill="none" stroke="#4e1539" stroke-opacity=".3"/></g>')
    # front kids
    o.append(kid(176,458,1.05,'#e9b994','#e8a821','#b9831a','kufi','#ffffff',5,'#13877c',.5,raise_hand=True))
    o.append(kid(386,458,1.05,'#a8714f','#f6a5ab','#d6707a','hijab','#6b2150',-5,'#6b2150',1.7))
    o.append('</svg>')
    return '\n'.join(o)
if __name__=='__main__':
    print(scene())
