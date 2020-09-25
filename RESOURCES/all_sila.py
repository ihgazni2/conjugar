from conjugar.acentuacion import *
from efdir import fs
s = fs.rfile('words.cat')
lines = s.strip().split('\n')
from xlist.map import mapv

arr = []
fails = []
for word in lines:
    print(word)
    try:
        var = get_silabas(word)
        arr = arr + var 
    except:
        fails = fails + [word] 
    else:
        pass


from xlist.util import uniqualize

arr = uniqualize(arr)
