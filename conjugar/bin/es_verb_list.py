from efdir import fs
import elist.elist as elel
import xdict.CrtableLib.crtable as xcr
import ltdict.ltdict as ltlt


import pkg_resources
import conjugar


TEM = pkg_resources.resource_filename("conjugar","data/conjugar.crtable.json")


import sys

crtbd0 = fs.rjson(TEM)
#crtbd1 = fs.rjson("irregular.crtable.json")


words = list(crtbd0.keys())

def main():
    srch = sys.argv[1]
    arr = elel.cond_select_values_all(words,cond_func=lambda ele:(srch in ele))
    for each in arr:
        print(each)

