import copy
import re

import elist.elist as elel
import tlist.tlist as tltl
import estring.estring as eses
import edict.edict as eded

import xdict.CrtableLib.crtable as xcr
from xdict.jprint import pdir
from xdict.jprint import pobj
from xdict import ltdict


#########################

ALPHABETA ='abcdefghijklmnopqrstuvwxyzáéíóúñü!?ç'


########时态的缩写#######
TENSES = {
    'ip':'indicativo presente',
    'ippc':'indicaativo pretérito perfecto compuesto',
    'ipps':'indictivo pretérito perfecto simple',
    'ipa':'indicativo pretérito anterior',
    'ipi':'indicativo pretérito imperfecto',
    'ippp':'indicativo pretérito pluscuam perfecto',
    'ifi':'indicativo futuro imperfecto',
    'ifp':'indicativo futuro perfecto',
    'sp':'subjuntivo presente',
    'spp':'subjuntivo pretérito perfecto',
    'spi':'subjuntivo pretérito imperfecto',
    'sppp':'subjuntivo pretérito pluscuam perfecto',
    'sfi':'subjuntivo futuro imperfecto',
    'sfp':'subjuntivo futuro perfecto',
    'cs':'condicional simple',
    'cc':'condicional compuesto',
    'ia':'imperativo afirmativo',
    'in':'imperativo negativo',
    'pp':'paticipio pasado',
    'g':'gerundio',
    'i':'infinitivo',
}
#
def tense_abbr_help(abbr=''):
    nd = eded.str_key_fuzzy(TENSES,abbr)
    pobj(nd)

def tense_full_help(full=''):
    nd = eded.str_value_fuzzy(TENSES,full)
    pobj(nd)

def tense_help(aorf=''):
    ndk = eded.str_key_fuzzy(TENSES,aorf)
    ndv = eded.str_value_fuzzy(TENSES,aorf)
    nd = eded._union(ndk,ndv)
    pobj(nd)

def fmt_tense_abbr(tense_abbr):
    tense_abbr = tense_abbr.lower()
    return(tense_abbr)

################



########陈述式现在时规则变化表#########


#IP 
def creat_regular_ip_table():
    '''
        Indicativo Presente
        陈述式 现在时
    '''
    cnl = ['person','-ar','-er','-ir','prsn_abbr']
    knl = ['person','prsn_abbr']
    table = {}
    crtb = xcr.crtable(colnameslist = cnl,table=table,keynameslist = knl)
    crtb.append_row(['yo','-o','-o','-o','s1'])
    crtb.append_row(['tú','-as','-es','-es','s2'])
    crtb.append_row(['él,ella,usted','-a','-e','-e','s3'])
    crtb.append_row(['nostros','-amos','-emos','-imos','pl1'])
    crtb.append_row(['vostros','-áis','-éis','-ís','pl2'])
    crtb.append_row(['ellos,ustedes','-an','-en','-en','pl3'])
    return(crtb)

TBL_IP = creat_regular_ip_table()

#################




#######陈述式 现在完成时############

#IPPC 
def creat_regular_ippc_table():
    '''
        Indicaativo Pretérito Perfecto Compuesto
        陈述式 现在完成时
    '''
    cnl = ['person','-ar','-er','-ir','prsn_abbr']
    knl = ['person','prsn_abbr']
    table = {}
    crtb = xcr.crtable(colnameslist = cnl,table=table,keynameslist = knl)
    crtb.append_row(['yo','he-ado','he-ido','he-ido','s1'])
    crtb.append_row(['tú','has-ado','has-ido','has-ido','s2'])
    crtb.append_row(['él,ella,usted','ha-ado','ha-ido','ha-ido','s3'])
    crtb.append_row(['nostros','hemos-ado','hemos-ido','hemos-ido','pl1'])
    crtb.append_row(['vostros','habéis-ado','habéis-ido','habéis-ido','pl2'])
    crtb.append_row(['ellos,ustedes','han-ado','han-ido','han-ido','pl3'])
    return(crtb)

TBL_IPPC = creat_regular_ippc_table()
###################



#############陈述式 简单过去时####################
#IPPS
#https://es.hujiang.com/new/p167462/


def creat_regular_ipps_table():
    '''
        Indictivo Pretérito Perfecto Simple
        陈述式 简单过去时
    '''
    cnl = ['person','-ar','-er','-ir','prsn_abbr']
    knl = ['person','prsn_abbr']
    table = {}
    crtb = xcr.crtable(colnameslist = cnl,table=table,keynameslist = knl)
    crtb.append_row(['yo','-é','-í','-í','s1'])
    crtb.append_row(['tú','-aste','-iste','-iste','s2'])
    crtb.append_row(['él,ella,usted','-ó','-ió','-ió','s3'])
    crtb.append_row(['nostros','-amos','-imos','-imos','pl1'])
    crtb.append_row(['vostros','-asteis','-isteis','-isteis','pl2'])
    crtb.append_row(['ellos,ustedes','-aron','-ieron','-ieron','pl3'])
    return(crtb)

TBL_IPPS = creat_regular_ipps_table()

############################################################


#########陈述式 近逾过去时########


#IPA
#

def creat_regular_ipa_table():
    '''
        Indicativo Pretérito Anterior
        陈述式 近逾过去时
    '''
    cnl = ['person','-ar','-er','-ir','prsn_abbr']
    knl = ['person','prsn_abbr']
    table = {}
    crtb = xcr.crtable(colnameslist = cnl,table=table,keynameslist = knl)
    crtb.append_row(['yo','hube-ado','hube-ido','hube-ido','s1'])
    crtb.append_row(['tú','hubiste-ado','hubiste-ido','hubiste-ido','s2'])
    crtb.append_row(['él,ella,usted','hubo-ado','hubo-ido','hubo-ido','s3'])
    crtb.append_row(['nostros','hubimos-ado','hubimos-ido','hubimos-ido','pl1'])
    crtb.append_row(['vostros','hubisteis-ado','hubisteis-ido','hubisteis-ido','pl2'])
    crtb.append_row(['ellos,ustedes','hubieron-ado','hubieron-ido','hubieron-ido','pl3'])
    return(crtb)

TBL_IPA = creat_regular_ipa_table()




###########陈述式 过去未完成时########


#IPI
#https://es.hujiang.com/new/p167758/

def creat_regular_ipi_table():
    '''
        Indicativo Pretérito Imperfecto
        陈述式 过去未完成时
    '''
    cnl = ['person','-ar','-er','-ir','prsn_abbr']
    knl = ['person','prsn_abbr']
    table = {}
    crtb = xcr.crtable(colnameslist = cnl,table=table,keynameslist = knl)
    crtb.append_row(['yo','-aba','-ía','-ía','s1'])
    crtb.append_row(['tú','-abas','-ías','-ías','s2'])
    crtb.append_row(['él,ella,usted','-aba','-ía','-ía','s3'])
    crtb.append_row(['nostros','-ábamos','-íamos','-íamos','pl1'])
    crtb.append_row(['vostros','-abais','-íais','-íais','pl2'])
    crtb.append_row(['ellos,ustedes','-aban','-ían','-ían','pl3'])
    return(crtb)

TBL_IPI = creat_regular_ipi_table()

##############################################


#########陈述式 过去完成时###########
#IPPP

def creat_regular_ippp_table():
    '''
        Indicativo Pretérito Pluscuam Perfecto
        陈述式 过去完成时
    '''
    cnl = ['person','-ar','-er','-ir','prsn_abbr']
    knl = ['person','prsn_abbr']
    table = {}
    crtb = xcr.crtable(colnameslist = cnl,table=table,keynameslist = knl)
    crtb.append_row(['yo','había-ado','había-ido','había-ido','s1'])
    crtb.append_row(['tú','habías-ado','habías-ido','habías-ido','s2'])
    crtb.append_row(['él,ella,usted','había-ado','había-ido','había-ido','s3'])
    crtb.append_row(['nostros','habíamos-ado','habíamos-ido','habíamos-ido','pl1'])
    crtb.append_row(['vostros','habíais-ado','habíais-ido','habíais-ido','pl2'])
    crtb.append_row(['ellos,ustedes','habían-ado','habían-ido','habían-ido','pl3'])
    return(crtb)

TBL_IPPP = creat_regular_ippp_table()
#####################




########陈述式 将来未完成时#######
#IFI
#https://es.hujiang.com/new/p167464/
#ifitbl = creat_regular_ifi_table()

def creat_regular_ifi_table():
    '''
        Indicativo Pretérito Imperfecto
        陈述式 将来未完成时
    '''
    cnl = ['person','-ar','-er','-ir','prsn_abbr']
    knl = ['person','prsn_abbr']
    table = {}
    crtb = xcr.crtable(colnameslist = cnl,table=table,keynameslist = knl)
    crtb.append_row(['yo','-aré','-eré','-iré','s1'])
    crtb.append_row(['tú','-arás','-erás','-irás','s2'])
    crtb.append_row(['él,ella,usted','-ará','-erá','-irá','s3'])
    crtb.append_row(['nostros','-aremos','-eremos','-iremos','pl1'])
    crtb.append_row(['vostros','-aréis','-eréis','-iréis','pl2'])
    crtb.append_row(['ellos,ustedes','-arán','-erán','-irán','pl3'])
    return(crtb)

TBL_IFI = creat_regular_ifi_table()

################



#########陈述式 将来完成时#########
#IFP

def creat_regular_ifp_table():
    '''
        Indicativo Futuro Perfecto
        陈述式 将来完成时
    '''
    cnl = ['person','-ar','-er','-ir','prsn_abbr']
    knl = ['person','prsn_abbr']
    table = {}
    crtb = xcr.crtable(colnameslist = cnl,table=table,keynameslist = knl)
    crtb.append_row(['yo','habré-ado','habré-ido','habré-ido','s1'])
    crtb.append_row(['tú','habrás-ado','habrás-ido','habrás-ido','s2'])
    crtb.append_row(['él,ella,usted','habrá-ado','habrá-ido','habrá-ido','s3'])
    crtb.append_row(['nostros','habremos-ado','habremos-ido','habremos-ido','pl1'])
    crtb.append_row(['vostros','habréis-ado','habréis-ido','habréis-ido','pl2'])
    crtb.append_row(['ellos,ustedes','habrán-ado','habrán-ido','habrán-ido','pl3'])
    return(crtb)


TBL_IFP = creat_regular_ifp_table()

#################



######虚拟式 现在时####
#SP 
#https://wenku.baidu.com/view/4d28cb888e9951e79a89275c.html


def creat_regular_sp_table():
    '''
        Subjuntivo Presente
        虚拟式 现在时
    '''
    cnl = ['person','-ar','-er','-ir','prsn_abbr']
    knl = ['person','prsn_abbr']
    table = {}
    crtb = xcr.crtable(colnameslist = cnl,table=table,keynameslist = knl)
    crtb.append_row(['yo','-e','-a','-a','s1'])
    crtb.append_row(['tú','-es','-as','-as','s2'])
    crtb.append_row(['él,ella,usted','-e','-a','-a','s3'])
    crtb.append_row(['nostros','-emos','-amos','-amos','pl1'])
    crtb.append_row(['vostros','-éis','-áis','-áis','pl2'])
    crtb.append_row(['ellos,ustedes','-en','-an','-an','pl3'])
    return(crtb)

TBL_SP =  creat_regular_sp_table()
##########



########虚拟式 现在完成时#########
#SPP
#https://wenku.baidu.com/view/9228f599f8c75fbfc77db2a9.html

def creat_regular_spp_table():
    '''
        Subjuntivo Pretérito Perfecto
        虚拟式 现在完成时
    '''
    cnl = ['person','-ar','-er','-ir','prsn_abbr']
    knl = ['person','prsn_abbr']
    table = {}
    crtb = xcr.crtable(colnameslist = cnl,table=table,keynameslist = knl)
    crtb.append_row(['yo','haya-ado','haya-ido','haya-ido','s1'])
    crtb.append_row(['tú','hayas-ado','hayas-ido','hayas-ido','s2'])
    crtb.append_row(['él,ella,usted','haya-ado','haya-ido','haya-ido','s3'])
    crtb.append_row(['nostros','hayamos-ado','hayamos-ido','hayamos-ido','pl1'])
    crtb.append_row(['vostros','hayáis-ado','hayáis-ido','hayáis-ido','pl2'])
    crtb.append_row(['ellos,ustedes','hayan-ado','hayan-ido','hayan-ido','pl3'])
    return(crtb)

TBL_SPP = creat_regular_spp_table()
#################


########虚拟式 过去未完成时#######
#SPI 
#https://wenku.baidu.com/view/6e35df02a417866fb84a8e95.html


def creat_regular_spi_table():
    '''
        Subjuntivo Presente
        虚拟式 过去未完成时
    '''
    cnl = ['person','-ar','-er','-ir','prsn_abbr']
    knl = ['person','prsn_abbr']
    table = {}
    crtb = xcr.crtable(colnameslist = cnl,table=table,keynameslist = knl)
    crtb.append_row(['yo','-ara','-iera','-iera','s1'])
    crtb.append_row(['tú','-aras','-ieras','-ieras','s2'])
    crtb.append_row(['él,ella,usted','-ara','-iera','-iera','s3'])
    crtb.append_row(['nostros','-áramos','-iéramos','-iéramos','pl1'])
    crtb.append_row(['vostros','-arais','-ierais','-ierais','pl2'])
    crtb.append_row(['ellos,ustedes','-aran','-ieran','-ieran','pl3'])
    return(crtb)

TBL_SPI = creat_regular_spi_table()

###############



#######虚拟式 过去完成时########
#SPPP
#http://es.kekenet.com/lesson/201109/153316.shtml


def creat_regular_sppp_table():
    '''
        Subjuntivo Pretérito Pluscuam Perfecto
        虚拟式 过去完成时
    '''
    cnl = ['person','-ar','-er','-ir','prsn_abbr']
    knl = ['person','prsn_abbr']
    table = {}
    crtb = xcr.crtable(colnameslist = cnl,table=table,keynameslist = knl)
    crtb.append_row(['yo','hubiera-ado','hubiera-ido','hubiera-ido','s1'])
    crtb.append_row(['tú','hubieras-ado','hubieras-ido','hubieras-ido','s2'])
    crtb.append_row(['él,ella,usted','hubiera-ado','hubiera-ido','hubiera-ido','s3'])
    crtb.append_row(['nostros','hubiéramos-ado','hubiéramos-ido','hubiéramos-ido','pl1'])
    crtb.append_row(['vostros','hubierais-ado','hubierais-ido','hubierais-ido','pl2'])
    crtb.append_row(['ellos,ustedes','hubieran-ado','hubieran-ido','hubieran-ido','pl3'])
    return(crtb)

TBL_SPPP = creat_regular_sppp_table()
#######################################

#######虚拟式 将来未完成时########
#SFI


def creat_regular_sfi_table():
    '''
        Subjuntivo Futuro Imperfecto
        虚拟式 将来未完成时
    '''
    cnl = ['person','-ar','-er','-ir','prsn_abbr']
    knl = ['person','prsn_abbr']
    table = {}
    crtb = xcr.crtable(colnameslist = cnl,table=table,keynameslist = knl)
    crtb.append_row(['yo','-are','-iere','-iere','s1'])
    crtb.append_row(['tú','-ares','-ieres','-ieres','s2'])
    crtb.append_row(['él,ella,usted','-are','-iere','-iere','s3'])
    crtb.append_row(['nostros','-áremos','-iéremos','-iéremos','pl1'])
    crtb.append_row(['vostros','-areis','-iereis','-iereis','pl2'])
    crtb.append_row(['ellos,ustedes','-aren','-ieren','-ieren','pl3'])
    return(crtb)

TBL_SFI = creat_regular_sfi_table()
#####################################

########################################################
#SFP

def creat_regular_sfp_table():
    '''
        Subjuntivo Futuro Perfecto
        虚拟式 将来完成时
    '''
    cnl = ['person','-ar','-er','-ir','prsn_abbr']
    knl = ['person','prsn_abbr']
    table = {}
    crtb = xcr.crtable(colnameslist = cnl,table=table,keynameslist = knl)
    crtb.append_row(['yo','hubiere-ado','hubiere-ido','hubiere-ido','s1'])
    crtb.append_row(['tú','hubieres-ado','hubieres-ido','hubieres-ido','s2'])
    crtb.append_row(['él,ella,usted','hubiere-ado','hubiere-ido','hubiere-ido','s3'])
    crtb.append_row(['nostros','hubiéremos-ado','hubiéremos-ido','hubiéremos-ido','pl1'])
    crtb.append_row(['vostros','hubiereis-ado','hubiereis-ido','hubiereis-ido','pl2'])
    crtb.append_row(['ellos,ustedes','hubieren-ado','hubieren-ido','hubieren-ido','pl3'])
    return(crtb)

TBL_SFP = creat_regular_sfp_table()
#########################################################


###############条件式 简单时态###########################
#CS
#http://es.kekenet.com/lesson/201202/161696.shtml

def creat_regular_cs_table():
    '''
        Condicional Simple
        条件式 简单时态
    '''
    cnl = ['person','-ar','-er','-ir','prsn_abbr']
    knl = ['person','prsn_abbr']
    table = {}
    crtb = xcr.crtable(colnameslist = cnl,table=table,keynameslist = knl)
    crtb.append_row(['yo','-aría','-ería','-iría','s1'])
    crtb.append_row(['tú','-arías','-erías','-irías','s2'])
    crtb.append_row(['él,ella,usted','-aría','-ería','-iría','s3'])
    crtb.append_row(['nostros','-aríamos','-eríamos','-iríamos','pl1'])
    crtb.append_row(['vostros','-aríais','-eríais','-iríais','pl2'])
    crtb.append_row(['ellos,ustedes','-arían','-erían','-irían','pl3'])
    return(crtb)

TBL_CS = creat_regular_cs_table()

#######################################################


################条件式 复合时态#####################
#CC

def creat_regular_cc_table():
    '''
        Condicional Compuesto
        条件式 复合时态
    '''
    cnl = ['person','-ar','-er','-ir','prsn_abbr']
    knl = ['person','prsn_abbr']
    table = {}
    crtb = xcr.crtable(colnameslist = cnl,table=table,keynameslist = knl)
    crtb.append_row(['yo','habría-ado','habría-ido','habría-ido','s1'])
    crtb.append_row(['tú','habrías-ado','habrías-ido','habrías-ido','s2'])
    crtb.append_row(['él,ella,usted','habría-ado','habría-ido','habría-ido','s3'])
    crtb.append_row(['nostros','habríamos-ado','habríamos-ido','habríamos-ido','pl1'])
    crtb.append_row(['vostros','habríais-ado','habríais-ido','habríais-ido','pl2'])
    crtb.append_row(['ellos,ustedes','habrían-ado','habrían-ido','habrían-ido','pl3'])
    return(crtb)

TBL_CC = creat_regular_cc_table()
###################################################



#############命令式 肯定形式#######################
#IA


def creat_regular_ia_table():
    '''
        Imperativo Afirmativo
        命令式 肯定形式
    '''
    cnl = ['person','-ar','-er','-ir','prsn_abbr']
    knl = ['person','prsn_abbr']
    table = {}
    crtb = xcr.crtable(colnameslist = cnl,table=table,keynameslist = knl)
    crtb.append_row(['yo',  None,None,None,'s1'])
    crtb.append_row(['tú','-a','-e','-e','s2'])
    crtb.append_row(['él,ella,usted','-e','-a','-a','s3'])
    crtb.append_row(['nostros','-emos','-amos','-amos','pl1'])
    crtb.append_row(['vostros','-ad','-ed','-id','pl2'])
    crtb.append_row(['ellos,ustedes','-en','-an','-an','pl3'])
    return(crtb)

TBL_IA = creat_regular_ia_table()
###############################################



#############命令式 否定形式###################
#IN


def creat_regular_in_table():
    '''
        Imperativo Negativo
        命令式 否定形式
    '''
    cnl = ['person','-ar','-er','-ir','prsn_abbr']
    knl = ['person','prsn_abbr']
    table = {}
    crtb = xcr.crtable(colnameslist = cnl,table=table,keynameslist = knl)
    crtb.append_row(['yo',  None,None,None,'s1'])
    crtb.append_row(['tú','no -es','no -as','no -as','s2'])
    crtb.append_row(['él,ella,usted','-e','-a','-a','s3'])
    crtb.append_row(['nostros','no -emos','no -amos','no -amos','pl1'])
    crtb.append_row(['vostros','no -éis','no -áis','no -áis','pl2'])
    crtb.append_row(['ellos,ustedes','no -en','no -an','no -an','pl3'])
    return(crtb)

TBL_IN = creat_regular_in_table()
##########################################


#############过去分词##############
#PP


def creat_regular_pp_table():
    '''
        Paticipio Pasado
        过去分词
    '''
    cnl = ['person','-ar','-er','-ir','prsn_abbr']
    knl = ['person','prsn_abbr']
    table = {}
    crtb = xcr.crtable(colnameslist = cnl,table=table,keynameslist = knl)
    crtb.append_row(['yo','-ado','-ido','-ido','s1'])
    crtb.append_row(['tú','-ado','-ido','-ido','s2'])
    crtb.append_row(['él,ella,usted','-ado','-ido','-ido','s3'])
    crtb.append_row(['nostros','-ado','-ido','-ido','pl1'])
    crtb.append_row(['vostros','-ado','-ido','-ido','pl2'])
    crtb.append_row(['ellos,ustedes','-ado','-ido','-ido','pl3'])
    return(crtb)

TBL_PP = creat_regular_pp_table()
###############################################


############副动词##################
#G
#

def creat_regular_g_table():
    '''
        Gerundio
        副动词
    '''
    cnl = ['person','-ar','-er','-ir','prsn_abbr']
    knl = ['person','prsn_abbr']
    table = {}
    crtb = xcr.crtable(colnameslist = cnl,table=table,keynameslist = knl)
    crtb.append_row(['yo','-ando','-iendo','-iendo','s1'])
    crtb.append_row(['tú','-ando','-iendo','-iendo','s2'])
    crtb.append_row(['él,ella,usted','-ando','-iendo','-iendo','s3'])
    crtb.append_row(['nostros','-ando','-iendo','-iendo','pl1'])
    crtb.append_row(['vostros','-ando','-iendo','-iendo','pl2'])
    crtb.append_row(['ellos,ustedes','-ando','-iendo','-iendo','pl3'])
    return(crtb)

TBL_G = creat_regular_g_table()

#################################

TBLS = {
 'ip': TBL_IP,
 'ippc': TBL_IPPC,
 'ipps': TBL_IPPS,
 'ipa': TBL_IPA,
 'ipi': TBL_IPI,
 'ippp': TBL_IPPP,
 'ifi': TBL_IFI,
 'ifp': TBL_IFP,
 'sp': TBL_SP,
 'spp': TBL_SPP,
 'spi': TBL_SPI,
 'sppp': TBL_SPPP,
 'sfi': TBL_SFI,
 'sfp': TBL_SFP,
 'cs': TBL_CS,
 'cc': TBL_CC,
 'ia': TBL_IA,
 'in': TBL_IN,
 'pp': TBL_PP,
 'g': TBL_G
}


####################
def table_help(abbr):
    arr = list(TENSES.keys())
    arr.pop(-1)
    ks = elel.str_fuzzy_search(arr,abbr)
    for k in ks:
        print('{0}:{1}'.format(k,TENSES[k]))
        print(TBLS[k].__repr__())

####################



################
#严格区分的话yo,tú,vos,ustedes,"él,ella","nostros,nostras","vostros,vostras","ustedes" "ellos,ellas"
#九种，但是实际应用中没这么严格

PERSON = {
    'yo':'s1',
    'y':'s1',
    'tú':'s2',
    'vos':'s22',
    'usted':'s23',
    't':'s2',
    'él':'s3',
    'el':'s3',
    'ella':'s3',
    'él,ella':'s3',
    'él,ella,usted':'s3',
    'nostros':'pl1',
    'nostras':'pl1',
    'nostros,nostras':'pl1',
    'nos':'pl1',
    'vostros':'pl2',
    'vostras':'pl2',
    'vostros,vostras':'pl2',
    'vost':'pl2',
    'ellos':'pl3',
    'ustedes':'pl3',
    'ellos,ustedes':'pl3',
    'ellos,ellas':'pl3',
    'ellas':'pl3'
}

def prsn_full_help(full=''):
    nd = eded.str_key_fuzzy(PERSON,full)
    pobj(nd)

def prsn_abbr_help(abbr=''):
    nd = eded.str_value_fuzzy(PERSON,abbr)
    pobj(nd)

def prsn_help(aorf=''):
    ndk = eded.str_key_fuzzy(PERSON,aorf)
    ndv = eded.str_value_fuzzy(PERSON,aorf)
    nd = eded._union(ndk,ndv)
    pobj(nd)

def fmt_prsn(prsn):
    prsn = prsn.lower()
    return(PERSON[prsn])

################

#################

def get_suffix(verbo):
    verbo = verbo.lower()
    suffix = verbo[-2:]
    return('-'+suffix)

def get_regular_tense(verbo,tense_abbr,prsn):
    suffix = get_suffix(verbo)
    prsn = fmt_prsn(prsn)
    prefix = verbo[:-2]
    tbl = TBLS[tense_abbr]
    ptrn = tbl[{'prsn_abbr':prsn}][0][suffix]
    if(ptrn):
        arr = ptrn.split('-')
        rslt = arr[0] + prefix + arr[1]
    else:
        rslt = None
    return(rslt)

def get_regular_tense2(tense_abbr,verbo,prsn):
    suffix = get_suffix(verbo)
    prsn = fmt_prsn(prsn)
    prefix = verbo[:-2]
    tbl = TBLS[tense_abbr]
    ptrn = tbl[{'prsn_abbr':prsn}][0][suffix]
    if(ptrn):
        arr = ptrn.split('-')
        rslt = arr[0] + prefix + arr[1]
    else:
        rslt = None
    return(rslt)

def get_regular_row(verbo,prsn,col = ['ip', 'ipi', 'ipps', 'ifi', 'cs', 'sp', 'sfi', 'spi', 'ia']):
    arr = [prsn]
    tmp = elel.array_map(col,get_regular_tense2,verbo,prsn)
    arr = arr + tmp + [PERSON[prsn]]
    return(arr)

def get_regular_row2(prsn,verbo,col = ['ip', 'ipi', 'ipps', 'ifi', 'cs', 'sp', 'sfi', 'spi', 'ia']):
    arr = [prsn]
    tmp = elel.array_map(col,get_regular_tense2,verbo,prsn)
    arr = arr + tmp + [PERSON[prsn]]
    return(arr)

def get_regular_crtb(verbo,col = ['ip', 'ipi', 'ipps', 'ifi', 'cs', 'sp', 'sfi', 'spi', 'ia']):
    rnl = ['yo','tú','él,ella,usted','nostros','vostros','ellos,ustedes']
    rows = elel.array_map(rnl,get_regular_row2,verbo,col)
    cnl = ['person', 'ip', 'ipi', 'ipps', 'ifi', 'cs', 'sp', 'sfi', 'spi', 'ia', 'prsn_abbr']
    knl = ['person','prsn_abbr']
    table = rows
    crtb = xcr.crtable(colnameslist = cnl,table=table,keynameslist = knl)
    return(crtb)

#################



#################
def get_dle_crtb(verbo,cache):
    crtb  = xcr.crtable(crtable=cache[verbo]['crtb'])
    return(crtb)

def spi_dle2eu(spi):
    spi = spi.strip(" ")
    arr = spi.split(" ")
    return(arr[0])

def tu_dle2eu(tuvos):
    tuvos = tuvos.replace("\x20","")
    arr = tuvos.split("/")
    return(arr[0])

def dle2eudict(crtb,**kwargs):
    if('deepcopy' in kwargs):
        deepcopy = kwargs['deepcopy']
    else:
        deepcopy = True
    if(deepcopy):
        ncrtb = copy.deepcopy(crtb)
    else:
        ncrtb = crtb
    #####
    print(ncrtb.crtable)
    #####
    spi = ncrtb.col('spi')
    spi = elel.array_map(spi,spi_dle2eu)
    spi = ltdict.list_to_ltdict(spi)
    ncrtb.modify_col('spi',spi)
    cnl = ncrtb.colnameslist
    knl = ['person','prsn_abbr']
    table = {}
    #debug
    print(ncrtb.crtable)
    #debug
    table[0] = ncrtb.crtable['table'][0]
    table[1] = ncrtb.crtable['table'][1]
    table[1][0] = tu_dle2eu(ncrtb.crtable['table'][1][0])
    table[1][1] = tu_dle2eu(ncrtb.crtable['table'][1][1])
    table[1][9] = tu_dle2eu(ncrtb.crtable['table'][1][9])
    table[2] = ncrtb.crtable['table'][3]
    table[2][0] = "él,ella,usted"
    table[3] = ncrtb.crtable['table'][4]
    table[3][0] = "nostros"
    table[4] = ncrtb.crtable['table'][5]
    table[4][0] = "vostros"
    table[5] = ncrtb.crtable['table'][7]
    table[5][0] = "ellos,ustedes"
    nncrtb = xcr.crtable(colnameslist = cnl,table=table,keynameslist = knl)
    return(nncrtb)

def cr_value(crtb,rowname,colname):
    cnl = crtb.colnameslist
    rnl = crtb.col(cnl[0])
    rownum = rnl.index(rowname)+1
    col = crtb.col(colname)
    return(col[rownum-1])

def tbl_diff(verbo,cache,col = ['ip', 'ipi', 'ipps', 'ifi', 'cs', 'sp', 'sfi', 'spi', 'ia']):
    crtb1 = get_regular_crtb(verbo)
    crtb2 = get_dle_crtb(verbo,cache)
    crtb2 = dle2eudict(crtb2)
    rnl = crtb1.col('person')
    diff_pair_list = []
    for colname in col:
        for rowname in rnl:
            print((colname,rowname))
            v1 = cr_value(crtb1,rowname,colname)
            v2 = cr_value(crtb2,rowname,colname)
            if(v1 == None):
                pass
            elif(v2 == None):
                pass
            elif(v1 == v2):
                pass
            else:
                diff_pair = (colname,rowname)
                diff_pair_list.append(diff_pair)
    return(diff_pair_list)

##################

def load_dict(fn):
    cache = nvft.read_json(fn='conjugar.crtable.json',op='r+')
    ncache = eded.intize_json(cache)
    return(ncache)

#########################

#CACHE = sys.argv[1]

def get_irregular(cache):
    DIFF = {}
    for verbo in cache:
        tmp = tbl_diff(verbo,cache)
        if(tmp.__len__() == 0):
            pass
        else:
            DIFF[verbo] = tmp
    return(DIFF)


#
def get_lefted(DIFF,cache):
    kl = list(DIFF.keys())
    lefted = eded.sub_algo(cache,kl)
    return(lefted)


#####################
#nvft.write_json(fn='irregular.crtable.json',json=lefted,op='w+')
#nvft.write_json(fn='diff.crtable.json',json=DIFF,op='w+')
#####################

def get_irr_via_lngth(lefted,lngth):
    arr = []
    for word in lefted:
        if(lngth == word.__len__()):
            arr.append(word)
    return(arr)

IR4 = ['asir', 'caer', 'fiar', 'huir', 'leer', 'liar', 'oler', 'piar', 'roer']
IR5 = ['aguar', 'aliar', 'alzar', 'andar', 'aunar', 'aviar', 'caber', 'cagar', 'cazar', 'cegar', 'ceñir', 'cocer', 'coger', 'creer', 'criar', 'decir', 'doler', 'errar', 'estar', 'fluir', 'gañir', 'gemir', 'gozar', 'guiar', 'haber', 'hacer', 'helar', 'herir', 'hozar', 'jugar', 'legar', 'ligar', 'lucir', 'mecer', 'medir', 'moler', 'morir', 'mover', 'mugir', 'nacer', 'negar', 'nevar', 'pacer', 'pagar', 'pecar', 'pedir', 'pegar', 'picar', 'poder', 'poner', 'regar', 'regir', 'rezar', 'reñir', 'rizar', 'rodar', 'rogar', 'rozar', 'rugir', 'saber', 'sacar', 'salir', 'secar', 'segar', 'solar', 'soler', 'sonar', 'soñar', 'tañer', 'tener', 'teñir', 'tocar', 'traer', 'ungir', 'vagar', 'valer', 'venir', 'volar', 'yacer']



