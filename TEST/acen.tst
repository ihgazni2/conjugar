from conjugar.acentuacion import show_stress,get_stress
from efdir import fs
import elist.elist as elel
words = fs.rjson("../RESOURCES/conjugar.words.json")

第38个 'abstraer'
['a', 'b', 's', 'tr', 'a', 'e', 'r']   ----------------------

三个辅音  前两个 归前  后两个 归后面  

stress_arr = elel.mapv(words,get_stress)
fs.wjson("es_stress.json",stress_arr)






fs.touch("es_stress.txt")
