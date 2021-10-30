# Hunter C. Sylvester
# Purpose: Function to save players, update best scores, and print the names of the top 5

# Function to take players name and i for the score
def scores(playersName, i):

    # list needed to put scores and names in
    players = []

    # Read all lines from current txt file into list above
    fixedWidthFile = open("topPlayers.txt", "r")
    for eachLine in fixedWidthFile.readlines():
        score = eachLine[0:10].rstrip().lstrip()
        player = eachLine[10:20].rstrip().lstrip()
        myList = [score, player]
        players.append(myList)

    # Close so no mishaps occur
    fixedWidthFile.close()

    # Add new players score
    players.append([str(i), playersName])

    # sort correctly
    players.sort(key = lambda x: (int(x[0])))

    # This creates a nice presentation for the scores when printed
    for eachLine in players[0:5]:
        [score, player] = eachLine
        score = score + "          "
        new = score + player
        players.append(new)
        print(f"{score}{player}")

    # We need to update the txt file with new top scores
    fixedWidthFile = open("topPlayers.txt", "w")
    for eachLine in players[0:5]:
        fixedWidthFile.write(eachLine[0] + "         ")
        fixedWidthFile.write(eachLine[1])
        fixedWidthFile.write("\n")

    fixedWidthFile.close()

# empty list to be used for storing values
temporary = []

# Function that shows the updated txt file to the player as they leave
def endersGame():
    
    # Read the file and write to the empty list
    fixedWidthFile = open("topPlayers.txt", "r")
    for eachLine in fixedWidthFile.readlines():
        score = eachLine[0:10].rstrip().lstrip()
        player = eachLine[10:20].rstrip().lstrip()
        myList = [score, player]
        temporary.append(myList)

    # Close file so no mishaps
    fixedWidthFile.close()
    
    # Prints each line of the list to show top scores and player names
    for eachLine in temporary[0:5]:
        [score, player] = eachLine
        score = score + "          "
        new = score + player
        temporary.append(new)
        print(f"{score}{player}")



