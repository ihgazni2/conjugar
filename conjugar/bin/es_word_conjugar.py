






from efdir import fs
import elist.elist as elel
import xdict.CrtableLib.crtable as xcr
import ltdict.ltdict as ltlt


def _numize_md(md):
    nmd = {}
    for k in md:
        try:
            int(k)
        except:
            nmd[k] = md[k]
        else:
            nmd[int(k)] = md[k]
    return(nmd)


def _numize_table(table):
    ntb = {}
    for each in table:
        ntb[int(each)] = ltlt.json2ltdict(table[each])
    return(ntb)

def _numize(crtb):
    table = crtb['table']
    knimd = crtb['knimd']
    vnimd = crtb['vnimd']
    animd = crtb['animd']
    crtb['table'] = _numize_table(table)
    crtb['knimd'] = _numize_md(knimd)
    crtb['vnimd'] = _numize_md(vnimd)
    crtb['animd'] = _numize_md(animd)
    return(crtb)






def which_word(i):
    return(list(crtbd0.keys())[i])


def shword(i,args):
    if(isinstance(i,str)):
        word = i
    else:
        word = which_word(i)
    crtable = _numize(crtbd0[word]['crtb'])
    colnameslist = ['person'] + ['ip', 'ipi', 'ipps', 'ifi', 'cs', 'sp', 'sfi', 'spi', 'ia']+ ['prsn_abbr']
    keynameslist = ['person', 'prsn_abbr']
    table = crtable['table']
    crtb = xcr.crtable(colnameslist = colnameslist,table=table,keynameslist = keynameslist)
    dummy =  crtb.cols(['person'] + list(args)+ ['prsn_abbr'])
    return(dummy)


import sys
import pkg_resources

TEM = pkg_resources.resource_filename("conjugar","data/conjugar.crtable.json")

crtbd0 = fs.rjson(TEM)

#crtbd0 = fs.rjson('conjugar.crtable.json')
#crtbd1 = fs.rjson("irregular.crtable.json")


def main():
    print("""
        'ip':'indicativo presente',
        'ipps':'indictivo pretérito perfecto simple',
        'ipa':'indicativo pretérito anterior',
        'ipi':'indicativo pretérito imperfecto',
        'ifi':'indicativo futuro imperfecto',
        'sp':'subjuntivo presente',
        'spi':'subjuntivo pretérito imperfecto',
        'sfi':'subjuntivo futuro imperfecto',
        'cs':'condicional simple',
        'ia':'imperativo afirmativo',
    """)
    print('ip', 'ipi', 'ipps', 'ifi', 'cs', 'sp', 'sfi', 'spi', 'ia')
    try:
        i = int(sys.argv[1])
    except :
        i = sys.argv[1]
    else:
        pass
    args = sys.argv[1:]
    shword(i,args)

