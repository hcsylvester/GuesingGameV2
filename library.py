def scores(playersName, i):

    # list needed to put values in
    players = []
    substitute = []

    # Read all lines into list above
    fixedWidthFile = open("topPlayers.txt", "r")
    for eachLine in fixedWidthFile.readlines():
        score = eachLine[0:10].rstrip().lstrip()
        player = eachLine[10:20].rstrip().lstrip()
        myList = [score, player]
        players.append(myList)
        #players.append(eachLine)

    # Close so no mishaps occur
    fixedWidthFile.close()

    # Add new players score
    #players.append(f"{i}         {playersName}")
    players.append([str(i), playersName])

    # sort correctly
    players.sort(key = lambda x: (int(x[0])))

    # Replit Code 8 for reference
    for eachLine in players[0:5]:
        [score, player] = eachLine
        score = score + "          "
        new = score + player
        players.append(new)
        print(f"{score}{player}")
        #print(eachLine)


    #We need to write new scores to the txt file
    fixedWidthFile = open("topPlayers.txt", "w")
    for eachLine in players[0:5]:
        fixedWidthFile.write(str(eachLine) + "\n")

    fixedWidthFile.close()
    #File assignment review and writing back out

