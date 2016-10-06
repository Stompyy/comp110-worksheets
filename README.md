# COMP110 Worksheets

Worksheet B - psuedocode. Richard Steele
//Had to redo all the spacing and indents after copying and pasting so apologies if it plays up.

guessesTaken = 0
likenessScore = 0
secretWord = ...				            //pick the secret word, I assume from a predetermined list.
n = secretWord.length				        //number of letters i.e if the list was a list of arrays, n = arrayLength

print "The word to guess has " n " letters"

while (true) loop
	  if (guessesTaken < 4)	
		    guessesTaken += 1		        //repeat for loop 4 times for 4 guesses
		    guessAccepted = false

	    	while (guessAccepted == false) loop
			      print "Enter your " n " letter guess"
		      	read guess
	      		guessLength = guess.length
						                        //if read is reading a string, then will need to convert to same format as guess
						                        //i.e. stringToArray command. As long as each character can be read and the 
						                        //number of characters can be determined then is fine.
			      if (guessLength == n)
				        guessAccepted = true
			      else
				        print "guessed word must be " n " letters long, try again"
		
		
                                    //now we have the an applicable guess of the correct length we can compare it against the secret word
		    for (i) in range (n)        //comparing each letter in turn
			      if (guess[i] == secretWord[i])
				        likenessScore += 1

		    if (likenessScore == n)		  //i.e. if (guess == secretWord)
			      print "You win!"
			      print "You did it in " guessesTaken " guesses."
			      end			                //finish
		    else
			      print "incorrect"
			      print "Likeness score: " likenessScore
	
	  else
		    print "Game Over"
		    print "You have run out of guesses"
		    print "The correct answer was " secretWord
        end
