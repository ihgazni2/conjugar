from efdir import fs
import elist.elist as elel
import edict.edict as eded
full_verbs = fs.rjson("verbs-es.json")
kl,vl =  eded.d2kvlist(full_verbs)
verbs = kl
roots = elel.mapv(vl,lambda ele:ele['root'])
tems = elel.mapv(vl,lambda ele:ele['template'])


fs.touch("verbs.cat")
fs.touch("verbs.root.cat")
fs.touch("verbs.tem.cat")


for i in range(verbs.__len__()):
    fs.afile("verbs.cat",verbs[i]+"\n")
    fs.afile("verbs.root.cat",roots[i]+"\n")
    fs.afile("verbs.tem.cat",tems[i]+"\n")
