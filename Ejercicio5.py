'''
Created on 07/09/2015

@author: Mono
'''

def dolares(peso, dolar):
    """
    >>> dolares(30, 15)
    450
    """
    equi= peso * dolar;
    
    return equi
    
if __name__=="__main__":
    import doctest
    doctest.testmod()
