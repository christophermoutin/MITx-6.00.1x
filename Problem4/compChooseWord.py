def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    returns: string or None
    """
 # Create a new variable to store the maximum score seen so far (initially 0)
    maxScore = 0
    score = 0
    # Create a new variable to store the best word seen so far (initially None)  
    bestWord = None
    # For each word in the wordList
    for i in wordList:
        
        # If you can construct the word from your hand
        if isValidWord(i, hand, wordList) == True:
            
            # Find out how much making that word is worth
            score = getWordScore(i, n)
            #print score,
            #print i,
            #print maxScore,
            #print bestWord
            # If the score for that word is higher than your best score
            if score > maxScore:
                # Update your best score, and best word accordingly
                maxScore = score
                bestWord = i
                

    # return the best word you found.
    #print maxScore
    return bestWord
