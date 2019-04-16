import conjugar.acentuacion as acen
from efdir import fs
import elist.elist as elel
from xdict.jprint import pobj,pdir


dummy = acen.show_stress('abstraer')
dummy = acen.show_stress('strass')
dummy = acen.show_stress('stretta')
dummy = acen.show_stress('stricto')
dummy = acen.show_stress('stripper')
dummy = acen.show_stress('ahuyentar')



words = fs.rjson("../RESOURCES/granada_es.all.single.nomark.arr")



def get_stress_arr(words):
    words  = elel.mapv(words,str.lower)
    failed = []
    stress_arr = []
    for i in range(words.__len__()):
        try:
            ele = acen.get_stress(words[i])
            if("yal" in ele['silabas']):
                print(ele)
            stress_arr.append(ele)
        except:
            failed.append(words[i])
        else:
            pass
    return(stress_arr)

stress_arr = get_stress_arr(words)
fs.wjson("es_stress.json",stress_arr)


def get_silaba_arr(stress_arr):
    silaba_set = set({})
    for each in stress_arr:
        silabas = each['silabas']
        for silaba in silabas:
            if(silaba in silaba_set):
                pass
            else:
                silaba_set.add(silaba)
    silabas = list(silaba_set)
    silabas.sort()
    return(silabas)


silaba_arr = get_silaba_arr(stress_arr)

fs.wjson("es_silaba_arr.json",silaba_arr)


# fs.touch("es_stress.txt")




silaba_splited_words = []
for each in stress_arr:
    silabas = each['silabas']
    word = elel.join(silabas,"-")
    silaba_splited_words.append(word)

silaba_splited_words.sort()


for each in stress_arr:
    if("ya" in each['silabas']):
        pobj(each)

####

y 比较特殊  还需要再 细分
    ay-u-dan-te
    a-yu-dan-te
究竟哪个对？

ay,ey,oy,uy只有后面有元音时才可以划分，
如果后面是辅音时，不可划分，如ha-ya 和 
muy就是两个代表的例子

####

