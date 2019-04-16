
Usage
=====

    :: 
        
        from conjugar import acentuacion as acen
        from xdict.jprint import pobj,pdir


=====

- ACUTE_CHARS

    ::
    
        acen.ACUTE_CHARS
        >>>
        'áéíóú'

- ACUTE_CHARS_MIRROR_DICT
    
    ::
    
           pobj(acen.ACUTE_CHARS_MIRROR_DICT)
           >>>
           {
               'a': 'á',
               'e': 'é',
               'i': 'í',
               'o': 'ó',
               'u': 'ú',
               'á': 'a',
               'é': 'e',
               'í': 'i',
               'ó': 'o',
               'ú': 'u'
           }
       


- ACUTE_STRONG_VOWEL

    ::
        
        acen.ACUTE_STRONG_VOWEL
        >>>['á', 'é', 'ó']

- ACUTE_VOWEL

    ::
    
        acen.ACUTE_VOWEL
        >>>['á', 'é', 'í', 'ó', 'ú']


- ACUTE_WEAK_VOWEL
    
      ::
          
          acen.ACUTE_WEAK_VOWEL
          >>>['í', 'ú']


- AC_A
- AC_E
- AC_I
- AC_O
- AC_U

     ::
     
     >>> acen.AC_A
     'á'
     >>> acen.AC_E
     'é'
     >>> acen.AC_I
     'í'
     >>> acen.AC_O
     'ó'
     >>> acen.AC_U
     'ú'
     >>>        

- CE_C
    
    ::
        
        acen.CE_C
        >>>>'ç'

- DI_U
    
    ::
    
        acen.DI_U
        >>>'ü'

- ENE

    ::
    
        acen.ENE
        >>>'ñ'

- UD_EXCM

    ::
        
        acen.UD_EXCM
        >>>'¡'


- UD_QM
    
    ::
        
         acen.UD_QM
         >>>'¿'        

- ALPHABETA
    
    ::
    
        acen.ALPHABETA
        >>>'abcdefghijklmnopqrstuvwxyzáéíóúñü!¡?¿ç'


- BI_CONSONANT
    
    ::
    
        acen.BI_CONSONANT
        >>>['ch', 'll', 'rr', 'pl', 'bl', 'tl', 'dl', 'cl', 'gl', 'pr', 'br', 'tr', 'dr', 'cr', 'gr']

- CL_CONSONANT

    ::
    
        acen.CL_CONSONANT
        >>>['pl', 'bl', 'tl', 'dl', 'cl', 'gl', 'pr', 'br', 'tr', 'dr', 'cr', 'gr']

- DI_CONSONANT

    ::
    
        acen.DI_CONSONANT
        >>>['ch', 'll', 'rr']

   
- CONSONANT
    
    ::
        
        acen.CONSONANT
        >>>['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', 'ñ']



- DIPTRONGO


- TRIPTONGO

- Help

- NORMAL_STRONG_VOWEL
- NORMAL_VOWEL
- NORMAL_WEAK_VOWEL
- STRONG_VOWEL_CHARS


   



- VOWEL
- VOWEL_CHARS
- WEAK_VOWEL_CHARS
- Y_DIPTRONGO
- Y_LAST
- Y_TRIPTONGO
- acute
- araq
- arr_recvr_lasty
- arr_repl_lasty
- de_bi
- de_c
- de_dip
- de_engine
- de_trip
- de_v
- de_y
- deacute
- elel
- eses
- get_charloc
- get_clstarr_spans
- get_silabas
- get_spanloc
- get_stress
- get_stress_char
- is_acute_char
- is_biconstant
- is_conclst
- is_diptrongo
- is_triptongo
- is_vowclst
- symmtera
- to_acute_char
- to_non_acute_char
- word2clstarr
- word_recvr_lasty
- word_repl_lasty
