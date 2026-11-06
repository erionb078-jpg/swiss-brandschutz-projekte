# Hero scene: a tidy desk with a monitor, an iPad and a phone, each showing the Abrar book.
P='buch/pages/%03d.webp'
def img(n,x,y,w,h,extra=''):
    return f'<image href="{P%n}" x="{x}" y="{y}" width="{w}" height="{h}" preserveAspectRatio="xMidYMid slice"{extra}/>'

def scene():
    o=['<svg class="scene-svg" viewBox="0 0 600 470" role="img" aria-labelledby="scnT"><title id="scnT">The Abrar book on a computer, a tablet and a phone</title>']
    o.append('''<defs>
<linearGradient id="dkTop" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#d9b48a"/><stop offset="1" stop-color="#c79a6b"/></linearGradient>
<linearGradient id="dkFront" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a87a4f"/><stop offset="1" stop-color="#8d6440"/></linearGradient>
<linearGradient id="glare" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".22"/><stop offset=".45" stop-color="#fff" stop-opacity=".04"/><stop offset=".46" stop-color="#fff" stop-opacity="0"/></linearGradient>
<linearGradient id="frameG" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2c2a30"/><stop offset="1" stop-color="#17161a"/></linearGradient>
<linearGradient id="standG" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#b9bcc4"/><stop offset=".5" stop-color="#e6e8ec"/><stop offset="1" stop-color="#a9acb4"/></linearGradient>
<linearGradient id="leafG" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#e9e2e6"/></linearGradient>
<clipPath id="cMon"><rect x="160" y="50" width="310" height="190" rx="3"/></clipPath>
<clipPath id="cPad"><rect x="414" y="214" width="112" height="158" rx="6"/></clipPath>
<clipPath id="cPhone"><rect x="96" y="244" width="64" height="134" rx="9"/></clipPath>
<filter id="soft" x="-20%" y="-20%" width="140%" height="160%"><feGaussianBlur stdDeviation="6"/></filter>
</defs>''')
    # backdrop
    o.append('<circle cx="300" cy="215" r="225" fill="var(--tint-2)"/>')
    o.append('<rect x="372" y="24" width="150" height="110" rx="10" fill="#fff" opacity=".55"/><path d="M447 24v110M372 79h150" stroke="#fff" stroke-width="5" opacity=".9"/>')
    # plant (left back)
    o.append('<g><animateTransform attributeName="transform" type="rotate" values="-1.2 70 330;1.2 70 330;-1.2 70 330" dur="7s" repeatCount="indefinite"/>'
             '<path d="M70 330C58 300 40 286 26 282C40 300 50 312 62 332Z" fill="#2f8f6a"/>'
             '<path d="M72 330C70 290 78 262 94 246C90 276 84 304 78 332Z" fill="#13877c"/>'
             '<path d="M70 330C66 300 52 268 40 254C46 284 56 310 66 332Z" fill="#3aa57c"/>'
             '<path d="M74 332C86 306 104 296 120 294C106 310 92 320 80 334Z" fill="#2f8f6a"/>'
             '<path d="M71 330C72 296 66 270 58 250C70 266 78 294 76 332Z" fill="#4fb98f"/></g>')
    o.append('<path d="M48 330h46l-6 44H54Z" fill="#e8ddd4"/><path d="M46 326h50v8H46Z" fill="#d9cbbf"/>')
    # desk
    o.append('<ellipse cx="300" cy="392" rx="300" ry="20" fill="#000" opacity=".08" filter="url(#soft)"/>')
    o.append('<path d="M14 372H586L600 404H0Z" fill="url(#dkTop)"/><rect x="0" y="404" width="600" height="18" rx="2" fill="url(#dkFront)"/>')
    o.append('<path d="M40 380h120M230 392h180M460 384h110" stroke="#b88a5c" stroke-width="1.4" opacity=".5" stroke-linecap="round"/>')
    # monitor
    o.append('<ellipse cx="315" cy="374" rx="70" ry="6" fill="#000" opacity=".18" filter="url(#soft)"/>')
    o.append('<path d="M300 250h30l6 104h-42Z" fill="url(#standG)"/><rect x="262" y="352" width="106" height="12" rx="6" fill="url(#standG)"/>')
    o.append('<rect x="150" y="40" width="330" height="212" rx="12" fill="url(#frameG)"/>')
    o.append('<g clip-path="url(#cMon)"><rect x="160" y="50" width="310" height="190" fill="#f6eff3"/>')
    o.append('<rect x="160" y="50" width="310" height="16" fill="#fff"/><circle cx="170" cy="58" r="2.4" fill="#6b2150"/><rect x="178" y="55" width="54" height="6" rx="3" fill="#e8d9e1"/><rect x="395" y="54" width="34" height="8" rx="4" fill="#d6303a"/><rect x="433" y="54" width="30" height="8" rx="4" fill="#ee7a2b"/>')
    o.append('<rect x="262" y="226" width="106" height="10" rx="5" fill="#fff" stroke="#e8d9e1"/>')
    spreads=[(None,1),(16,17),(18,19)]
    for k,(a,b) in enumerate(spreads):
        vals=';'.join(['1' if j==k else '0' for j in range(3)]+['1' if k==0 else '0'])
        o.append(f'<g opacity="{1 if k==0 else 0}"><animate attributeName="opacity" values="{vals}" keyTimes="0;.333;.667;1" calcMode="discrete" dur="10.5s" repeatCount="indefinite"/>'
                 +(img(a,196,70,107,152) if a else '')+img(b,315,70,107,152)+'</g>')
    o.append('<path d="M315 70v152" stroke="#000" stroke-opacity=".12"/>')
    # turning leaf (right page flips to the left)
    o.append('<g transform="translate(315 0)"><g opacity="0"><animate attributeName="opacity" values="0;0;1;1;0" keyTimes="0;.74;.75;.97;1" dur="3.5s" repeatCount="indefinite"/>'
             '<animateTransform attributeName="transform" type="scale" values="1 1;1 1;-1 1;-1 1" keyTimes="0;.75;.97;1" dur="3.5s" repeatCount="indefinite"/>'
             '<rect x="0" y="70" width="107" height="152" fill="url(#leafG)" stroke="#e1d6dc"/></g></g>')
    # highlight pen on the monitor page
    o.append('<path d="M330 150h64" stroke="#f5b400" stroke-width="7" stroke-opacity=".45" stroke-linecap="round" stroke-dasharray="64" stroke-dashoffset="64">'
             '<animate attributeName="stroke-dashoffset" values="64;64;0;0;64" keyTimes="0;.15;.3;.9;1" dur="3.5s" repeatCount="indefinite"/></path>')
    o.append('<rect x="160" y="50" width="310" height="190" fill="url(#glare)"/></g>')
    o.append('<circle cx="315" cy="246" r="1.6" fill="#55525a"/>')
    # coffee mug (right)
    o.append('<ellipse cx="566" cy="374" rx="22" ry="4" fill="#000" opacity=".14"/>')
    o.append('<path d="M546 332h38v34a8 8 0 0 1-8 8h-22a8 8 0 0 1-8-8Z" fill="#6b2150"/><path d="M584 340c12 0 12 20 0 20" fill="none" stroke="#6b2150" stroke-width="5"/><ellipse cx="565" cy="332" rx="19" ry="4" fill="#4e1539"/>'
             '<text x="565" y="360" text-anchor="middle" font-size="13" fill="#f3d9e6" font-family="Noto Naskh Arabic,serif" font-weight="700">اقرأ</text>')
    for i,dx in enumerate((-6,4)):
        o.append(f'<path d="M{565+dx} 324c-5-8 5-12 0-20" fill="none" stroke="#b9a3af" stroke-width="2.4" stroke-linecap="round" opacity="0">'
                 f'<animate attributeName="opacity" values="0;.7;0" dur="3s" begin="{i*1.5}s" repeatCount="indefinite"/>'
                 f'<animateTransform attributeName="transform" type="translate" values="0 6;0 -10" dur="3s" begin="{i*1.5}s" repeatCount="indefinite"/></path>')
    # iPad on a stand (right front)
    o.append('<ellipse cx="470" cy="388" rx="64" ry="5" fill="#000" opacity=".18" filter="url(#soft)"/>')
    o.append('<path d="M452 372l-14 16h64l-14-16Z" fill="url(#standG)"/>')
    o.append('<rect x="406" y="206" width="128" height="174" rx="12" fill="url(#frameG)"/>')
    o.append('<g clip-path="url(#cPad)">'+img(17,414,214,112,158)+
             '<path d="M486 284c10-10 28-4 26 8s-24 14-30 4" fill="none" stroke="#d11a5f" stroke-width="2.6" stroke-linecap="round" stroke-dasharray="80" stroke-dashoffset="80">'
             '<animate attributeName="stroke-dashoffset" values="80;80;0;0;80" keyTimes="0;.2;.5;.92;1" dur="5s" repeatCount="indefinite"/></path>'
             '<path d="M432 330h40" stroke="#1b2a6b" stroke-width="2.2" stroke-linecap="round" stroke-dasharray="40" stroke-dashoffset="40">'
             '<animate attributeName="stroke-dashoffset" values="40;40;0;0;40" keyTimes="0;.55;.7;.92;1" dur="5s" repeatCount="indefinite"/></path>'
             '<rect x="414" y="214" width="112" height="158" fill="url(#glare)"/></g>')
    o.append('<circle cx="470" cy="210" r="1.4" fill="#55525a"/>')
    # pencil lying on the desk
    o.append('<g transform="rotate(-6 470 396)"><rect x="420" y="393" width="92" height="5.5" rx="2.75" fill="#f4f4f6"/><path d="M512 393l9 2.75-9 2.75Z" fill="#c9cbd1"/><rect x="420" y="393" width="92" height="2" rx="1" fill="#fff"/></g>')
    # phone (left front, on a small stand)
    o.append('<ellipse cx="128" cy="388" rx="44" ry="4" fill="#000" opacity=".18" filter="url(#soft)"/>')
    o.append('<path d="M112 376l-10 12h52l-10-12Z" fill="url(#standG)"/>')
    o.append('<rect x="90" y="238" width="76" height="146" rx="14" fill="url(#frameG)"/>')
    o.append('<g clip-path="url(#cPhone)"><rect x="96" y="244" width="64" height="134" fill="#f6eff3"/>')
    o.append('<g><animateTransform attributeName="transform" type="translate" values="0 0;0 0;0 -94;0 -94;0 -188;0 -188;0 0" keyTimes="0;.25;.33;.58;.66;.92;1" dur="9s" repeatCount="indefinite" calcMode="spline" keySplines="0 0 1 1;.45 0 .2 1;0 0 1 1;.45 0 .2 1;0 0 1 1;.45 0 .2 1"/>')
    for k,n in enumerate((1,16,24,1)):
        o.append(img(n,100,252+k*94,56,80))
        o.append(f'<rect x="100" y="{252+k*94}" width="56" height="80" fill="none" stroke="#e1d6dc"/>')
    o.append('</g><rect x="96" y="244" width="64" height="8" fill="#f6eff3"/><rect x="117" y="246" width="22" height="4" rx="2" fill="#17161a"/>')
    o.append('<rect x="96" y="244" width="64" height="134" fill="url(#glare)"/></g>')
    o.append('</svg>')
    return '\n'.join(o)
if __name__=='__main__':print(scene())
