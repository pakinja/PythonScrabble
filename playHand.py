def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # As long as there are still letters left in the hand:
    sscr = 0
    while calculateHandlen(hand) > 0:
        
        # Display the hand
        print()
        print("Current Hand: ", end="")
        displayHand(hand)
        # Ask user for input
        word = input( "Enter word, or a" + " " + '"."' + " " +
                "to indicate that you are finished: ")
        
        # If the input is a single period:
        # End the game (break out of the loop)
        if word == ".":
            print("Goodbye! Total score: " + str(sscr) + " " + "points.")
            break   
                
            # Otherwise (the input is not a single period):
        else:
            # If the word is not valid:
            if isValidWord(word, hand, wordList) == False:
                # Reject invalid word (print a message followed by a blank line)
                print ("Invalid word, please try again.", end=" ") 
                #Otherwise (the word is valid):
            else:
                # Tell the user how many points the word earned, and the
                #updated total score, in one line followed by a blank line
                                
                #getWordScore(word, n)
                sscr = sscr + getWordScore(word, n)
                print('"' + str(word) + '"' + " " + "earned"+ " "
                + str(getWordScore(word, n))
                + " " + "points." + " " + "Total: " 
                + str(sscr) + " points" )
                
                
                # Update the hand 
                hand = updateHand(hand, word)
                cond = 0
                for key in hand.values():
                    cond += key
                if cond == 0:
                    print()
                    print( "Run out of letters. Total score: " + str(sscr)
                    + " " + "points")
                    break
                    #print(hand)
            
                #updateHand(hand, word)
                #print(updateHand(hand, word))
                
    # Game is over (user entered a '.' or ran out of letters),
    #so tell user the total score
    #print("Goodbye! Total score: " + str(sscr) + " " + "points.")
