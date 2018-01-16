def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

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
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if isValidWord(i, hand, wordList)==True:
            
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

def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
# Keep track of the total score
    totalScore = 0
    score = 0
    compEntry = None
    
    # As long as there are still letters left in the hand:
    while sum(hand.values()) != 0: 
          
        # Display the hand
        print 'Current Hand:',
        displayHand(hand)
        #breaks if hand size is 1
        if sum(hand.values()) == 1:
            break 
        # Find best word
        compEntry = compChooseWord(hand,wordList,n)
        #exit game if none
        if compEntry == None:
            break
        #keep track of the score and loop once again
        else:
            score = getWordScore(compEntry, n)
            totalScore += score
            #print result
            print '"' + str(compEntry) + '" earned ' + str(score) + ' points. Total: ' + str(totalScore) + ' points'
            print
            # Update the hand 
            hand = updateHand(hand,compEntry)
    
    print 'Total score: ' + str(totalScore) + ' points.'
    return