import re
import elist.elist as elel
import estring.estring as eses



def creat_or_from_sarr(sarr):
    regex_str = elel.join(sarr,'|')
    return(re.compile(regex_str))

def search_gen(regex,s,*args):
    args = list(args)
    arrlen = args.__len__()
    if(arrlen==0):
        start = 0
        end = s.__len__()
    elif(arrlen==1):
        start = args[0]
        end = s.__len__()
    else:
        start = args[0]
        end = args[1]
    cur = start
    while(True):
        m = regex.search(s,cur)
        if(m):
            if(m.start()<end):
                cur = m.end()
            else:
                pass
            yield(m)
        else:
            return(None)


def find_all_spans(regex,s):
    rslt = []
    g = search_gen(regex,s)
    for each in g:
        ele = (each.start(),each.end())
        rslt.append(ele)
    return(rslt)


def regex_split(regex,s):
    spans = find_all_spans(regex,s)
    arr = eses.get_substr_arr_via_spans(s,spans)
    return(arr)



#
def de_cond_and_engine(ele,*args):
    args = list(args)
    conds = args[0]
    lngth = conds.__len__()
    if(args.__len__()>1):
        funcs = args[1]
        if(isinstance(funcs,list)):
            pass
        else:
            func = funcs
            funcs = elel.init(func,lngth)
    else:
        func = lambda ele,cond:(ele in cond)
        funcs = elel.init(lngth,func)
    for i  in range(0,lngth):
        each = conds[i]
        tmp = funcs[i](each,ele)
        if(tmp):
            pass
        else:
            return(False)
    return(True)


def de_cond_or_engine(ele,*args):
    args = list(args)
    conds = args[0]
    lngth = conds.__len__()
    if(args.__len__()>1):
        funcs = args[1]
        if(isinstance(funcs,list)):
            pass
        else:
            func = funcs
            funcs = elel.init(func,lngth)
    else:
        func = lambda ele,cond:(ele in cond)
        funcs = elel.init(lngth,func)
    for i  in range(0,lngth):
        each = conds[i]
        tmp = funcs[i](each,ele)
        if(tmp):
            return(True)
        else:
            pass
    return(False)

#

