from efdir import fs
import elist.elsit as elel
arr = fs.rjson("granada_es.all.single.nomark.arr")
arr = elel.mapv(arr,str.lower)
arr.sort()

fs.touch("words.cat")
for i in range(arr.__len__()):
    fs.afile("words.cat",arr[i]+"\n")
