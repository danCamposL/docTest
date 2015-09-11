'''
Created on 07/09/2015

@author: Mono
'''

def tienda (compra):
    
    """
    >>> tienda(120)
    102.0
    """
    desc = compra *.15;
    total = compra - desc;
    
    return total


if __name__=="__main__":
    import doctest
    doctest.testmod()