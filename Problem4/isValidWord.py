def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    wordTest = word.lower()
    handcopy = hand.copy()
    for i in wordTest:
        if i not in 'abcdefghijklmnopqrstuvwxyz':
            return False
    if wordTest not in wordList:
        return False
    else:
        for i in word:
            if i not in handcopy:
                return False
            else:
                if handcopy[i]==0:
                    return False
                if handcopy.get(i,0) !=0:
                    handcopy[i]-=1
                if handcopy.get(i,0)<0:
                    return False
        return True
