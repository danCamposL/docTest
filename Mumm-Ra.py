# -*- coding: utf-8 -*-

'''
Created on 04/09/2015

@author: Mono
'''


def edad(e):
    
    """
    Ademas de ser comentarios se pueden utilizar para hacer pruebas sencillas
    >>> edad(78)
    Eres adolescente
    """
    
    if e < 0:
        print ("No existes")
    elif e<=1 & e<=13:
        print ("Eres nino")
    elif e<18:
        print ("Eres adolescente")
    elif e<65:
        print ("Eres adulto")
    else:
        print ("Eres Mumm-Ra")
            
    
    
if __name__=="__main__":
    import doctest
    doctest.testmod()
