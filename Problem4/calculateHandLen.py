def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    handLength = 0
    for i in hand.keys():
        if hand[i] < 0:
            return 'error'
        else:
            handLength += hand[i]
    return handLength
