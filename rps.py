import random
userLosses = 0
ties = 0
userWins = 0
playCount = 0

def convertUserChoice():
    userChoice = input("(R)ock, (P)aper, or (S)cissors? ")
    if userChoice.lower() == "rock" or userChoice.lower() == "r" :
        userChoice = 1
        return userChoice
    elif userChoice.lower() == "paper" or userChoice.lower() == "p" :
        userChoice = 2
        return userChoice
    elif userChoice.lower() == "scissors" or userChoice.lower() == "s" :
        userChoice = 3
        return userChoice  
    else:
        print("Please choose a valid option.")

def determineWinner():
    cpuResult = random.randint(1,3)
    userResult = convertUserChoice()
    global userLosses
    global ties
    global userWins
    global playCount
    
    if userResult == cpuResult:
        print("It was a tie!") 
        ties = ties + 1
    elif userResult == 1 and cpuResult == 2:
        print('You lost! The CPU chose Paper and you chose Rock.')
        userLosses = userLosses + 1
    elif userResult == 1 and cpuResult == 3:
        print('Victory! The CPU chose Scissors but you chose Rock!')
        userWins = userWins + 1
    elif userResult == 2 and cpuResult == 1:
        print('Victory! The CPU chose Rock, but you chose Paper!')
        userWins = userWins + 1
    elif userResult == 2 and cpuResult == 3:
        print('You lost! The CPU chose Scissors and you chose Paper.')
        userLosses = userLosses + 1
    elif userResult == 3 and cpuResult == 1:
        print('You lost! The CPU chose Rock and you chose Scissors!')
        userLosses = userLosses + 1
    elif userResult == 3 and cpuResult == 2:
        print('Victory! The CPU chose Paper, but you chose Scissors!')
        userWins = userWins + 1
    playCount = playCount + 1
    playTheGame()   
    
def playTheGame():

    play = input("Would you like to play? (Y)es or (N)o? The current score is " + str(userWins) + " wins, " + str(userLosses) + " losses, and " + str(ties) + " ties. " )
    if play.lower() == 'yes' or play.lower() == 'y':
        determineWinner()
    else:
        print('Farewell!')

determineWinner()
