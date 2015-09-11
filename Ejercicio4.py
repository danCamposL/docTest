'''
Created on 07/09/2015

@author: Mono
'''
from _ast import Str


def estudiantes(totalalu, totalm, totalh):
    """
    >>> estudiantes(30, 15, 15)
    Mujeres = 50 Hombres = 50
    """
    porH = totalh * 100;
    porM = totalm * 100;
    
    porcH = porH /totalalu
    porcM = porM / totalalu;
    
    print "Mujeres = " + str(porcM) + " Hombres = " + str(porcH);

if __name__=="__main__":
    import doctest
    doctest.testmod()