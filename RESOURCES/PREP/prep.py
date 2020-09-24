s = '''A 	To 	对于，朝向
Alrededor 	About 	关于
Ante 	Before 	在之前
Arriba 	Up 	在上端
Cabe,cerca 	Near 	靠近
Como,igual 	Like 	像
Con 	With 	同，用，以
Contra 	Against 	反对
De 	Of 	的，从
Debajo 	Under 	在下面
Desde 	From,since 	从，自从
Detrás 	After,behind 	在后面
En,junto 	In,at 	在，在里面
Entre 	Between,among 	在之间
Excepto 	Except 	除了
Fuera 	off 	（离）开，脱离
Hacia 	Toward,towards 	朝着
Hasta 	Till,until,to 	直到
Junto 	Beside 	除以外
Para 	For 	为了
Pero 	But 	除却之外
Por 	For,per,across,by 	因为，为了，每一，穿过
Según 	To according 	按照，依据
Sin 	Without 	无，没有
Sobre,encima 	Above,onto,upon,about 	在上面'''

import elist.elist as elel
import ltdict.ltdict as ltlt

def csv2lines(s):
    s = s.strip("\n")
    lines = s.split("\n")
    return(lines)

def line2ltdict(line,sp="\t"):
    l = line.split(sp)
    ltd = ltlt.list2ltdict(l)
    return(ltd)



def csv2table(s):
    lns = csv2lines(s)
    lns = elel.mapv(lns,line2ltdict)
    tbl = ltlt.list2ltdict(lns)
    return(tbl)

table = csv2table(s)
from xdict.CrtableLib  import crtable as xcr
crtb = xcr.crtable(table=table,colnameslist=["es","en","ch"],keynameslist=["en","ch"])
print(crtb)




# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# |           es|                    en|                    ch|
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# |           A |                   To |            对于，朝向|
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# |   Alrededor |                About |                  关于|
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# |        Ante |               Before |            在……之前|
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# |      Arriba |                   Up |            在……上端|
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# |  Cabe,cerca |                 Near |                  靠近|
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# |  Como,igual |                 Like |                    像|
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# |         Con |                 With |            同，用，以|
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# |      Contra |              Against |                  反对|
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# |          De |                   Of |                的，从|
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# |      Debajo |                Under |            在……下面|
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# |       Desde |           From,since |              从，自从|
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# |      Detrás |         After,behind |            在……后面|
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# |    En,junto |                In,at |        在，在……里面|
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# |       Entre |        Between,among |            在……之间|
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# |     Excepto |               Except |                  除了|
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# |       Fuera |                  off |        （离）开，脱离|
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# |       Hacia |       Toward,towards |                  朝着|
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# |       Hasta |        Till,until,to |                  直到|
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# |       Junto |               Beside |            除……以外|
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# |        Para |                  For |                  为了|
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# |        Pero |                  But |          除却……之外|
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# |         Por |    For,per,across,by |因为，为了，每一，穿过|
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# |       Según |         To according |            按照，依据|
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# |         Sin |              Without |              无，没有|
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# |Sobre,encima |Above,onto,upon,about |            在……上面|
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++










