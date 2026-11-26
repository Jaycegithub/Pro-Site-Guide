import json,re
F='/tmp/claude-0/-home-user-Pro-Site-Guide/b2ee1dc1-8052-5b08-8e58-bbc5993dc44a/scratchpad/fonts'
src=open('../v2/card-wordpress-job-board-wp-job-manager.html').read()
CSS=src.split('<style>')[1].split('</style>')[0]
BG='radial-gradient(circle at 78% 45%,#1E3A8A 0%,#0F172A 55%,#0B1120 100%)'
def page(e,t,s,ill): return f'<html><head><style>{CSS}</style></head><body style="background:{BG}"><div class="l"><div class="e">{e}</div><h1>{t}</h1><div class="s">{s}</div></div><div class="ill">{ill}</div><div class="b">ProSite<span style="color:#60A5FA">Guide</span></div></body></html>'
G='font-size:13px;color:#64748B;font-weight:700'
P={}
P['check-who-owns-a-domain']=('Domains · 2-minute check','Who Owns<br>Your Domain?','A free lookup every business owner should do',f'''<div style="position:relative;width:570px;height:470px">
<div class="card" style="position:absolute;left:0;top:10px;width:480px;padding:22px">
<div style="display:flex;align-items:center;gap:10px;border:2px solid #CBD5E1;border-radius:12px;padding:12px 14px"><svg width="22" height="22" viewBox="0 0 22 22"><circle cx="9" cy="9" r="7" stroke="#1D4ED8" stroke-width="3" fill="none"/><path d="m14 14 6 6" stroke="#1D4ED8" stroke-width="3" stroke-linecap="round"/></svg><b style="font-size:19px">yourbusiness.com</b><span style="margin-left:auto;background:#1D4ED8;color:#fff;font-size:14px;font-weight:700;padding:8px 14px;border-radius:8px">Lookup</span></div>
'''+''.join(f'<div style="display:flex;padding:13px 4px;border-bottom:1px solid #E2E8F0;font-size:16px"><span style="color:#64748B;font-weight:600;width:150px">{k}</span><b style="color:{c}">{v}</b></div>' for k,v,c in [('Registrar','Your registrar','#0F172A'),('Created','2018-03-14','#0F172A'),('Expires','2027-03-14','#0F172A'),('Status','Transfer locked','#15803D'),('Registrant','REDACTED','#94A3B8')])+f'''</div>
<div class="card" style="position:absolute;right:0;top:320px;width:240px;padding:16px 18px;display:flex;align-items:center;gap:12px">
<svg width="40" height="40" viewBox="0 0 40 40"><circle cx="20" cy="20" r="19" fill="#22C55E"/><path d="m11 21 6 6 12-13" stroke="#fff" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg><div><div style="{G}">YOUR ACCOUNT</div><div style="font-weight:700;font-size:17px">You own it</div></div></div></div>''')
P['hosting-renewal-prices']=('Black Friday · Hosting','Check the<br>Renewal Price','Before you buy a cheap hosting deal',f'''<div style="position:relative;width:570px;height:470px">
<div class="card" style="position:absolute;left:0;top:30px;width:330px;padding:24px;text-align:center">
<div style="display:inline-block;background:#111827;color:#FACC15;font-weight:700;font-size:15px;padding:6px 14px;border-radius:99px">BLACK FRIDAY</div>
<div style="{G};margin-top:18px">FIRST TERM</div><div style="font-size:64px;font-weight:700;color:#1D4ED8;letter-spacing:-2px">$1.99<span style="font-size:22px;color:#64748B">/mo</span></div>
<div style="height:2px;background:#E2E8F0;margin:16px 0"></div>
<div style="{G}">RENEWS AT</div><div style="font-size:52px;font-weight:700;color:#DC2626;letter-spacing:-2px">$17.99<span style="font-size:20px;color:#64748B">/mo</span></div>
<div style="font-size:13px;color:#94A3B8;font-weight:600;margin-top:6px">small print</div></div>
<div class="card" style="position:absolute;right:0;top:0;width:220px;padding:18px">
<div style="{G}">3-YEAR COST</div><svg width="184" height="150" viewBox="0 0 184 150" style="margin-top:10px">'''+''.join(f'<rect x="{8+i*62}" y="{140-h}" width="44" height="{h}" rx="6" fill="{c}"/>' for i,(h,c) in enumerate([(30,'#93C5FD'),(80,'#60A5FA'),(135,'#DC2626')]))+f'''</svg>
<div style="display:flex;justify-content:space-around;font-size:12px;color:#64748B;font-weight:700"><span>Yr 1</span><span>Yr 2</span><span>Yr 3</span></div></div>
<div class="card" style="position:absolute;right:10px;top:290px;width:230px;padding:16px 18px;display:flex;align-items:center;gap:12px">
<div style="width:42px;height:42px;border-radius:50%;background:#DC2626;color:#fff;font-size:24px;font-weight:700;display:flex;align-items:center;justify-content:center">9x</div><div><div style="{G}">PRICE JUMP</div><div style="font-weight:700;font-size:16px">At renewal</div></div></div></div>''')
P['check-website-on-mobile']=('Website tips · Mobile','Check Your<br>Site on Mobile','3 free ways, and what to look for',f'''<div style="position:relative;width:570px;height:500px">
<div style="position:absolute;left:30px;top:0;width:250px;height:500px;background:#0F172A;border:4px solid #475569;border-radius:40px;padding:14px;box-shadow:0 30px 60px rgba(0,0,0,.4)">
<div style="background:#fff;border-radius:28px;height:100%;padding:34px 16px 16px;color:#0F172A">
<div style="display:flex;align-items:center;gap:8px"><div style="width:26px;height:26px;border-radius:7px;background:#1D4ED8"></div><div style="height:10px;width:70px;background:#CBD5E1;border-radius:5px"></div><div style="margin-left:auto;width:22px">'''+'<div style="height:3px;background:#0F172A;margin:4px 0;border-radius:2px"></div>'*3+'''</div></div>
<div style="height:120px;border-radius:12px;background:linear-gradient(135deg,#DBEAFE,#93C5FD);margin-top:16px"></div>
<div style="height:14px;width:90%;background:#0F172A;border-radius:5px;margin-top:16px"></div><div style="height:9px;width:100%;background:#E2E8F0;border-radius:5px;margin-top:10px"></div><div style="height:9px;width:80%;background:#E2E8F0;border-radius:5px;margin-top:8px"></div>
<div style="background:#16A34A;color:#fff;font-weight:700;font-size:15px;text-align:center;padding:12px;border-radius:10px;margin-top:22px">📞 Call now</div>
<div style="border:2px solid #1D4ED8;color:#1D4ED8;font-weight:700;font-size:15px;text-align:center;padding:10px;border-radius:10px;margin-top:10px">Book online</div></div></div>
<div class="card" style="position:absolute;right:0;top:40px;width:260px;padding:18px 20px">
<div style="{G}">MOBILE CHECKLIST</div>'''+''.join(f'<div style="display:flex;align-items:center;gap:10px;margin-top:11px;font-size:15px;font-weight:600"><div style="width:22px;height:22px;border-radius:50%;background:#22C55E;color:#fff;font-size:13px;display:flex;align-items:center;justify-content:center">✓</div>{t}</div>' for t in ['Loads fast','Text readable','No pop-up','Buttons work','Details current'])+f'''</div>
<div class="card" style="position:absolute;right:20px;top:330px;width:220px;padding:16px 18px;display:flex;align-items:center;gap:12px">
<div style="width:44px;height:44px;border-radius:10px;background:#1D4ED8;color:#fff;font-size:15px;font-weight:700;display:flex;align-items:center;justify-content:center">3</div><div><div style="{G}">FREE WAYS</div><div style="font-weight:700;font-size:16px">Phone, Chrome, Firefox</div></div></div></div>''')
import random; random.seed(7)
N=21; fixed=set()
for ox,oy in [(0,0),(14,0),(0,14)]:
  for i in range(7):
    for j in range(7):
      if i in(0,6) or j in(0,6) or (2<=i<=4 and 2<=j<=4): fixed.add((ox+i,oy+j))
fp={(ox+i,oy+j) for ox,oy in [(0,0),(14,0),(0,14)] for i in range(7) for j in range(7)} | {(ox+i,oy+j) for ox,oy in [(0,0),(14,0),(0,14)] for i in range(-1,8) for j in range(-1,8)}
cells=[(x,y) for x in range(N) for y in range(N) if (x,y) in fixed or ((x,y) not in fp and random.random()<.5)]
qr=f'<svg width="210" height="210" viewBox="-1 -1 {N+2} {N+2}"><rect x="-1" y="-1" width="{N+2}" height="{N+2}" fill="#fff"/>'+''.join(f'<rect x="{x}" y="{y}" width="1.02" height="1.02" fill="#0F172A"/>' for x,y in cells)+'</svg>'
P['google-reviews-qr-code']=('Google reviews · Free','Google Reviews<br>QR Code','Free, straight from your Business Profile',f'''<div style="position:relative;width:570px;height:480px">
<div class="card" style="position:absolute;left:20px;top:10px;width:300px;padding:26px;text-align:center">
<div style="font-weight:700;font-size:21px">Enjoyed your visit?</div><div style="font-size:15px;color:#64748B;font-weight:600;margin-top:6px">Scan to leave a review</div>
<div style="margin-top:16px">{qr}</div>
<div style="font-size:30px;color:#FBBF24;letter-spacing:4px;margin-top:10px">★★★★★</div></div>
<div class="card" style="position:absolute;right:0;top:60px;width:240px;padding:18px">
<div style="display:flex;align-items:center;gap:10px"><div style="width:36px;height:36px;border-radius:50%;background:#DBEAFE;color:#1D4ED8;font-weight:700;display:flex;align-items:center;justify-content:center">M</div><div><div style="font-weight:700;font-size:15px">Maria L.</div><div style="color:#FBBF24;font-size:15px">★★★★★</div></div></div>
<div style="font-size:14px;color:#475569;font-weight:500;margin-top:10px;line-height:1.4">Friendly team and quick service. Highly recommend!</div></div>
<div class="card" style="position:absolute;right:20px;top:300px;width:230px;padding:16px 18px;display:flex;align-items:center;gap:12px">
<div style="width:44px;height:44px;border-radius:50%;background:#16A34A;color:#fff;font-size:22px;font-weight:700;display:flex;align-items:center;justify-content:center">+1</div><div><div style="{G}">NEW REVIEW</div><div style="font-weight:700;font-size:16px">In 30 seconds</div></div></div></div>''')
for k,v in P.items(): open(f'card-{k}.html','w').write(page(*v))
json.dump(list(P),open('slugs.json','w'))
