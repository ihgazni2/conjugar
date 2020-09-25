from conjugar import acentuacion as acen
from xdict.jprint import pobj,pdir
import sys


def main():
    word = sys.argv[1]
    print('-----------------------------')
    acen.show_stress(word)
    print('-----------------------------')
    pobj(acen.get_stress(word))
    print('-----------------------------')
    print(acen.get_silabas(word))


