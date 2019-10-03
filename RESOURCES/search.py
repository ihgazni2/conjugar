import sys
import copy
import re

import elist.elist as elel
import tlist.tlist as tltl
import estring.estring as eses
import edict.edict as eded

import xdict.CrtableLib.crtable as xcr
from xdict.jprint import pdir
from xdict.jprint import pobj

import navegador5.file_toolset as nvft


#http://doc.chacuo.net/ascii
DD_U = chr(252)
AC_A = chr(225)
AC_E = chr(233)
AC_O = chr(243)
AC_I = chr(237)
AC_U = chr(250)
ENE = chr(241)

R_QM = chr(191)
R_EXCM = chr(161)



ARRS = {}

def no_num_cond_func(ele):
    regex = re.compile("[0-9]")
    m = regex.search(ele)
    if(m):
        return(False)
    else:
        return(True)

def split_words_repo():
    ARRS[0] = nvft.read_json(fn='granada_es.all.arr',op='r+')
    ARRS[1] = elel.array_map(ARRS[0],lambda ele:str.strip(ele," "))
    ARRS[2] = elel.cond_select_values_all(ARRS[1],cond_func=lambda ele:not(" " in ele))
    ARRS[3] = elel.cond_select_values_all(ARRS[2],cond_func=lambda ele:not("!" in ele))
    ARRS[4] = elel.cond_select_values_all(ARRS[3],cond_func=lambda ele:not(R_EXCM in ele))
    ARRS[5] = elel.cond_select_values_all(ARRS[4],cond_func=lambda ele:not("?" in ele))
    ARRS[6] = elel.cond_select_values_all(ARRS[5],cond_func=lambda ele:not(R_QM in ele))
    ARRS[7] = elel.cond_select_values_all(ARRS[6],cond_func=lambda ele:not("-" in ele))
    ARRS[8] = elel.cond_select_values_all(ARRS[7],cond_func=lambda ele:not("," in ele))
    ARRS[9] = elel.cond_select_values_all(ARRS[8],cond_func=lambda ele:not("_" in ele))
    ARRS[10] = elel.cond_select_values_all(ARRS[9],cond_func=no_num_cond_func)
    nvft.write_json(fn='granada_es.all.single.nomark.arr',json=ARRS[10],op='w+')


def acenize(s):
    return(s.replace('a',AC_A).replace('e',AC_E).replace('o',AC_O).replace('i',AC_I).replace('u',AC_U))

def unacenize(s):
    return(s.replace(AC_A,'a').replace(AC_E,'e').replace(AC_O,'o').replace(AC_I,'i').replace(AC_U,'u'))


 
def cond_search(ele,cond,**kwargs):
    if('ignore_case' in kwargs):
        ignore_case = kwargs['ignore_case']
    else:
        ignore_case = True
    if('ignore_acen' in kwargs):
        ignore_acen = kwargs['ignore_acen']
    else:
        ignore_acen = True
    if('ignore_ddu' in kwargs):
        ignore_ddu = kwargs['ignore_ddu']
    else:
        ignore_ddu = True
    if('ignore_ene' in kwargs):
        ignore_ene = kwargs['ignore_ene']
    else:
        ignore_ene = True
    if(ignore_ddu):
        ele = ele.replace('ü','u').replace('Ü','u')
        cond = cond.replace('ü','u').replace('Ü','u')
    else:
        pass
    if(ignore_ene):
        ele = ele.replace('ñ','n')
        cond = cond.replace('ñ','n')
    else:
        pass
    if(ignore_case):
        ele = ele.lower()
        cond = cond.lower()
    else:
        pass
    if(ignore_acen):
        ele = unacenize(ele)
        cond = unacenize(cond)
    else:
        pass
    return(cond in ele)


def search(arr,s):
    indexes = elel.cond_select_indexes_all(arr,cond_func = cond_search,cond_func_args=[s])
    values = elel.select_indexes(arr,indexes)
    pobj(values,with_color=0)
    return(values)

try:
    search(sys.argv[2],sys.argv[1])
except:
    esd = nvft.read_json(fn='granada_es.all.single.nomark.arr',op='r+')
    search(esd,sys.argv[1])
else:
    pass

