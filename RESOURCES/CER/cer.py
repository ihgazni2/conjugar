s="""abastecer
ablandecer
aborrecer
abravecer
acaecer
aciarecer
acontecer
acrecer
adolecer
adormecer
adyacer
afacer
agradecer
altivecer
amanecer
amarecer
amarillecer
amohecer
amorecer
amortecer
anochecer
apacer
aparecer
apetecer
aplacer
arbolecer
arborecer
aridecer
atardecer
atorcer
autosatisfacer
blanquecer
calecer
carecer
clarecer
cocer
coercer
cognocer
colicuecer
compadecer
comparecer
complacer
conocer
contrafacer
contrahacer
convalecer
convencer
crecer
decrecer
desabastecer
desadormecer
desagradecer
desaparecer
desbravecer
descaecer
descocer
desconocer
desembravecer
desenfurecer
desenmohecer
desenmudecer
desenrudecer
desensoberbecer
desentorpecer
desentumecer
desfallecer
desfavorecer
desflorecer
desfortaiecer
desguarnecer
deshacer
deshumedecer
desmerecer
desobedecer
desparecer
desplacer
destorcer
desvanecer
dispiacer
ejercer
embarbecer
embastecer
embebecer
embellecer
embermejecer
emblandecer
emblanquecer
embobecer
embosquecer
embravecer
embrutecer
empalidecer
empavorecer
empecer
empequeñecer
emplastecer
emplebeyecer
emplumecer
empobrecer
empodrecer
empretecer
emputecer
enaltecer
enamarillecer
enardecer
encallecer
encalvecer
encandecer
encanecer
encarecer
encarnecer
enceguecer
encloquecer
encorecer
encrudecer
encruelecer
endentecer
endurecer
enflaquecer
enflorecer
enfranquecer
enfurecer
engrandecer
engravecer
enllentecer
enlobreguecer
enloquecer
enlustrecer
enmagrecer
enmalecer
enmohecer
enmollecer
enmudecer
ennegrecer
ennoblecer
ennudecer
enorgullecer
enralecer
enrarecer
enrigidecer
enriquecer
enrojecer
enronquecer
enrudecer
enruinecer
ensandecer
ensarnecer
ensoberbecer
ensombrecer
ensordecer
entallecer
entenebrecer
enternecer
entestecer
entontecer
entorpecer
entreyacer
entristecer
entullecer
entumecer
envaguecer
envanecer
envejecer
enverdecer
envilecer
enzurdecer
escaecer
escamecer
esclarecer
escocer
esmorecer
establecer
estorcer
estremecer
evanecer
evanescer
excandecer
facer
fallecer
favorecer
fenecer
florecer
fortalecer
fosforecer
fosforescer
frutecer
grandifacer
guamecer
guarecer
hacer
herbecer
hermanecer
humedecer
jacer
languidecer
licuefacer
lividecer
lobreguecer
malfacer
mecer
merecer
mohecer
nacer
negrecer
obedecer
obscurecer
ofrecer
oscurecer
pacer
padecer
palidecer
parecer
perecer
permanecer
pertenecer
pimpollecer
placer
plastecer
preconocer
preestablecer
prevalecer
pubescer
rarefacer
reaparecer
reblandecer
recocer
reconocer
reconvalecer
recrecer
recrudecer
refacer
reflorecer
reguarnecer
rehacer
rehumedecer
rejuvenecer
relentecer
remanecer
remecer
renacer
repacer
resplandecer
restablecer
retallecer
retorcer
retoñecer
revejecer
reverdecer
robustecer
satisfacer
sobrecrecer
subyacer
tallecer
tardecer
torcer
trasparecer
tullecer
tumefacer
vencer
verdecer
yacer"""

import elist.elist as elel
import ltdict.ltdict as ltlt

def to_lines(s):
    s = s.strip("\n")
    lines = s.split("\n")
    return(lines)


def line2entry(line):
    entry = "esconju" + " " + line + " ip | egrep yo >> cer.ip.yo"
    return(entry)

def creat(s):
    lns = to_lines(s)
    lns = elel.mapv(lns,line2entry)
    for ln in lns:
        print(ln)

creat(s)
