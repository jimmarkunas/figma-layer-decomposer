from pathlib import Path
from PIL import Image, ImageDraw
import hashlib, json, zipfile

ROOT = Path(__file__).parent
AUTH = ROOT.parent / 'authoritative'
W, H = 1586, 992
master = Image.open(AUTH/'master.png').convert('RGBA')
portrait = Image.open(AUTH/'portrait-lock5.png').convert('RGBA')

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def raster_svg(name, size):
    # Exact geometry from the authoritative Figma-exported SVGs; rasterized at
    # the native mask dimensions with Pillow, preserving alpha occupancy.
    a=Image.new('L',size,0); d=ImageDraw.Draw(a)
    if name == 'phone-alpha-mask.svg':
        d.rounded_rectangle((0,0,size[0]-1,size[1]-1), radius=21, fill=255)
    else:
        sx,sy=size[0]/534,size[1]/408.014
        poly=[(0,0),(533*sx,15*sy),(533*sx,365*sy),(0,365*sy)]
        d.polygon(poly,fill=255)
        d.polygon([(190.5*sx,365.514*sy),(335.5*sx,365.514*sy),(331.5*sx,382.514*sy),(387.5*sx,398.514*sy),(387.5*sx,407.514*sy),(130.5*sx,407.514*sy),(130.5*sx,398.514*sy),(186.5*sx,382.514*sy)],fill=255)
    return a

occ_portrait = Image.new('L', (W,H), 0)
pa = portrait.getchannel('A').resize((513,735), Image.Resampling.LANCZOS)
occ_portrait.paste(pa, (581,60), pa)
occ_tv = Image.new('L', (W,H), 0)
tv = raster_svg('tv-alpha-mask.svg', (533,407))
tv.save(AUTH/'tv-cutout.png')
occ_tv.paste(tv, (895+46,399+38), tv)
occ_phone = Image.new('L', (W,H), 0)
phone = raster_svg('phone-alpha-mask.svg', (126,282))
phone.save(AUTH/'phone-cutout.png')
occ_phone.paste(phone, (782+20,523+10), phone)

patches = {
 'A1': (480,0,650,700,occ_portrait,'PORTRAIT / CENTRAL CONCRETE'),
 'A2': (480,680,650,312,occ_portrait,'PORTRAIT / LOWER FLOOR'),
 'B1': (850,350,650,410,Image.frombytes('L',(W,H),bytes(max(a,b) for a,b in zip(occ_tv.tobytes(),occ_phone.tobytes()))),'TV + PHONE / WALL'),
 'B2': (730,730,800,262,Image.frombytes('L',(W,H),bytes(max(a,b) for a,b in zip(occ_tv.tobytes(),occ_phone.tobytes()))),'TV + PHONE / FLOOR'),
}
results={}
for k,(x,y,w,h,occ,label) in patches.items():
    mask=occ.crop((x,y,x+w,y+h)); out=master.crop((x,y,x+w,y+h)); pix=out.load(); mp=mask.load()
    for yy in range(h):
        for xx in range(w):
            if mp[xx,yy] > 0: pix[xx,yy]=(99,214,237,255)
    path=ROOT/f'{k}-corrected-edit-input.png'; out.save(path)
    results[k]={'semantic_role':label,'dimensions':[w,h],'mask_pixel_count':sum(v>0 for v in mask.getdata()),'sha256':sha(path),'full_canvas_placement':{'x':x,'y':y,'w':w,'h':h},'status':'CORRECTED_INPUTS_READY'}

sheet=Image.new('RGB',(1600,1250),(245,245,245)); d=ImageDraw.Draw(sheet)
pos={'A1':(20,70),'A2':(700,70),'B1':(20,700),'B2':(700,700)}
for k,(_,_,w,h,_,label) in patches.items():
    x,y=pos[k]; d.text((x,y),f'{k} — {label} — {w}×{h}',fill='black'); sheet.paste(Image.open(ROOT/f'{k}-corrected-edit-input.png').convert('RGB'),(x,y+35))
sheet.save(ROOT/'corrected-edit-inputs-contact-sheet.png')
(ROOT/'README.txt').write_text('DIRECTV CORRECTED EDIT INPUTS — AUTHORITATIVE ALPHA\n\nA1 — PORTRAIT / CENTRAL CONCRETE — 650×700: master crop x=480,y=0,w=650,h=700; portrait occupancy only.\nA2 — PORTRAIT / LOWER FLOOR — 650×312: master crop x=480,y=680,w=650,h=312; portrait occupancy only.\nB1 — TV + PHONE / WALL — 650×410: master crop x=850,y=350,w=650,h=410; TV + phone occupancy only.\nB2 — TV + PHONE / FLOOR — 800×262: master crop x=730,y=730,w=800,h=262; TV + phone occupancy only.\n\nEach PNG is an exact immutable-master crop with cyan #63D6ED replacing only authoritative alpha occupancy.\n')
with zipfile.ZipFile(ROOT/'DIRECTV-CORRECTED-EDIT-INPUTS.zip','w',zipfile.ZIP_DEFLATED) as z:
    for n in ['A1-corrected-edit-input.png','A2-corrected-edit-input.png','B1-corrected-edit-input.png','B2-corrected-edit-input.png','corrected-edit-inputs-contact-sheet.png','README.txt']: z.write(ROOT/n,n)
manifest={'canvas_dimensions':[W,H],'master':{'path':'handoff/directv/authoritative/master.png','sha256':sha(AUTH/'master.png'),'provenance':'Immutable DIRECTV master; local canonical input/directv-hero-01/master.png'},'authoritative_sources':[
 {'path':'handoff/directv/authoritative/portrait-lock5.png','semantic_role':'Portrait foreground alpha','dimensions':[1048,1501],'sha256':sha(AUTH/'portrait-lock5.png'),'provenance':'Accepted LOCK #5 asset; Figma node 278:2','source_figma_node':'278:2','placement':{'x':580.8200073242188,'y':59.880001068115234,'w':513.260009765625,'h':734.8800048828125}},
 {'path':'handoff/directv/authoritative/tv-cutout.png','semantic_role':'TV foreground alpha mask','dimensions':[533,407],'sha256':sha(AUTH/'tv-cutout.png'),'provenance':'Exact Figma-exported alpha mask SVG rasterized deterministically','source_figma_node':'236:16','parent_figma_node':'161:14','placement':{'x':941,'y':437,'w':533,'h':407}},
 {'path':'handoff/directv/authoritative/phone-cutout.png','semantic_role':'Phone foreground alpha mask','dimensions':[126,282],'sha256':sha(AUTH/'phone-cutout.png'),'provenance':'Exact Figma-exported alpha mask SVG rasterized deterministically','source_figma_node':'236:19','parent_figma_node':'236:18','placement':{'x':802,'y':533,'w':126,'h':282}}], 'patches':results,'status':'CORRECTED_INPUTS_READY'}
(ROOT/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
