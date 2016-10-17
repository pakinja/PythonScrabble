def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    #HAND_SIZE = 4 
    gtype = input("Enter n to deal a new hand, r to replay the last hand"  
                    + ",or e to end game: ")
    gtype = str(gtype)
    global hand_1 
    if gtype != "n" and gtype !="r" and gtype !="e":
        print("Invalid word, please try again")
        playGame(wordList)
        
    
    elif gtype == "n":
         
        #global hand_1 
        hand_1 = dealHand(HAND_SIZE)
        
        while True:        
        
            gtype_2 = input("Enter u to have yourself play,"   
            + " c to have the computer play:")
               
            gtype_2 = str(gtype_2)
                    
            if gtype_2 != "u" and gtype_2 !="c":
                print("Invalid word, please try again")
            else:
                break
            
                
        
        if gtype_2 == "u":
            
            playHand(hand_1, wordList, HAND_SIZE)
            playGame(wordList)
           
        elif gtype_2 == "c":
            
            #global hand_1 
            #hand_1 = dealHand(HAND_SIZE)
            
            compPlayHand(hand_1, wordList, HAND_SIZE)
            playGame(wordList)
        
    
    elif gtype == "r":
        
        try:
            prueba = len(hand_1.values())
            
            if prueba > 0:
                gtype_2 = input("Enter u to have yourself play,"   
                                         + " c to have the computer play:")
                gtype_2 = str(gtype_2)            
                  
                if gtype_2 == "u":
                    playHand(hand_1, wordList, HAND_SIZE)
                    playGame(wordList)
                     
                elif gtype_2 == "c":
                    compPlayHand(hand_1, wordList, HAND_SIZE)
                    playGame(wordList)
        
        except:
            print("You have not played a hand yet." 
            + "Please play a new hand first!")
            playGame(wordList)
            
    
    elif gtype == "e":
        try:        
            del hand_1
            return None        
        except:
            return None
