def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    res_1 = None
    res_2 = None
    frq = hand.copy()
    
    for x in word:
        frq[x] = frq.get(x,0) - 1
    
    if -1 not in frq.values():
        res_1 = True
    else:
        res_1 = False
    
    if word in wordList:
        res_2 = True
        
    else:
        res_2 = False
        
    #print(res_1)
    #print(res_2)
    #print(frq)
        
    if res_1 == True and res_2 == True:
        return True
    else:
        return False
