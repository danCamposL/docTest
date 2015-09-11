'''
Created on 07/09/2015

@author: Mono
'''

def sueldo(s, v1, v2, v3):
    
    
    """
    >>> sueldo(3500, 100, 1000, 10000)
    4610.0
    """
     
    ex1 = v1 * .10;
    ex2 = v2 * .10;
    ex3 = v3 * .10;
    
    suel = s + ex1 + ex2 + ex3;
              
    
    return suel


if __name__=="__main__":
    import doctest
    doctest.testmod()
