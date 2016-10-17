def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    val = hand.values()
    suma = 0    
    
    for i in val:
        if i > 0:
            suma += i
        
    return suma
