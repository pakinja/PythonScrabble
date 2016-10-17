def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1
    """
    
    gtype = raw_input("Enter n to deal a new hand, r to replay the last hand"  
                    + ",or e to end game: ")
    gtype = str(gtype)
    HAND_SIZE = 9    
    #global hand_1    
    
   
    if gtype == "n":
        global hand_1 
        hand_1 = dealHand(HAND_SIZE)
        playHand(hand_1, wordList, HAND_SIZE)
        playGame(wordList)
        
    
    elif gtype == "r":
        
        try:        
            playHand(hand_1, wordList, HAND_SIZE)
            playGame(wordList)            
            
            
        except:
            print("You have not played a hand yet." 
            + "Please play a new hand first!")
            playGame(wordList)
                 
        
    elif gtype == "e":
        del hand_1
        return None
    
    else:
        print("Invalid word, please try again")
        playGame(wordList)
