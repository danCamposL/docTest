'''
Created on 07/09/2015

@author: Mono
'''

def calif(cal1, cal2, cal3):
    
    """
    >>> calif(9, 8, 7)
    8
    """
    
    
    sum = cal1 + cal2 +cal3 
    promedio= sum/3
    
    
    
    return promedio

if __name__=="__main__":
    import doctest
    doctest.testmod()
