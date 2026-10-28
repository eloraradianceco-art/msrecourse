import sys, json
import os; HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,os.path.join(HERE,'content'))
import n1,n2,n3,n4,n5
order = n1.UNITS+n2.UNITS+n3.UNITS+n4.UNITS+n5.UNITS
# National first (N1..N11), then Mississippi
nat=[u for u in order if u['part']=='National']; ms=[u for u in order if u['part']=='Mississippi']
nat.sort(key=lambda u:int(u['id'][1:])); ms.sort(key=lambda u:int(u['id'][1:]))
units=[]
nq=0
for u in nat+ms:
    qs=[]
    for i,(q,c,w,why) in enumerate(u['quiz']):
        opts=[c]+list(w); assert len(set(opts))==4,(u['id'],i)
        qs.append(dict(id=f"{u['id']}-{i+1}",q=q,o=opts,a=0,why=why)); nq+=1
    lessons=[]
    for l in u['lessons']:
        lessons.append(dict(title=l['title'],body=l['body'],key=l.get('key',[]),example=l.get('example',''),confirm=l.get('confirm',[])))
    units.append(dict(id=u['id'],part=u['part'],title=u['title'],objectives=u['objectives'],lessons=lessons,quiz=qs,drill=bool(u.get('drill'))))
sources=[
 ("MREC License Law, revised July 1, 2026 (Miss. Code Title 73, Ch. 35)","https://www.mrec.ms.gov/wp-content/uploads/2026/07/MREC_LICENSE_LAW_2026_REVISED-7-01-2026.pdf"),
 ("MREC Form A: Working With a Real Estate Broker (June 2023)","https://www.mrec.ms.gov/wp-content/uploads/2023/06/WWREB-fillable-Legal-size-06-05-2023.pdf"),
 ("MREC: PCDS Q&A from the Administrator (2023)","https://www.mrec.ms.gov/pcds-qa-from-administrator-2023-2"),
 ("30 Miss. Admin. Code Pt. 1601, Rule 4.3 Disclosure Requirements (Cornell LII)","https://law.cornell.edu/regulations/mississippi/30-Miss-Code-R-SS-1601-4-3"),
 ("Mississippi State University Extension: Understanding Mississippi Property Taxes","https://extension.msstate.edu/publications/understanding-mississippi-property-taxes"),
 ("The Mississippi Bar: Homestead Rights","https://msbar.org/article/homestead-rights/"),
 ("Miss. Code §89-1-55 (FindLaw)","https://codes.findlaw.com/ms/title-89-real-and-personal-property/ms-code-sect-89-1-55/"),
 ("TurboTenant: Mississippi lease and landlord-tenant summary (secondary; verify against Miss. Code Title 89, Ch. 8)","https://www.turbotenant.com/rental-lease-agreement/mississippi/"),
 ("Kin Insurance: Mississippi Windstorm Underwriting Association eligibility (secondary; verify with MWUA)","https://www.kin.com/blog/mississippi-windstorm-mwua-eligibility/"),
]
data=dict(units=units,nq=nq,sources=sources,disclaimer="Study aid only. Not legal advice and not an official MREC or PSI publication. Verify current law, forms, fees and exam rules with the Mississippi Real Estate Commission (mrec.ms.gov) and the current PSI candidate bulletin.")
html=open(os.path.join(HERE,'template.html')).read()
out=html.replace('__DATA_JSON__',json.dumps(data,ensure_ascii=False).replace('</','<\\/'))
open(os.path.join(HERE,'..','index.html'),'w').write(out)
print('units',len(units),'lessons',sum(len(u['lessons']) for u in units),'questions',nq,'bytes',len(out))
