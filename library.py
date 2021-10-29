def scores(playersName, i):

    # list needed to put values in
    players = []
    substitute = []

    # Read all lines into list above
    fixedWidthFile = open("topPlayers.txt", "r")
    for eachLine in fixedWidthFile.readlines():
        players.append(eachLine)

    # Close so no mishaps occur
    fixedWidthFile.close()

    # Add new players score
    players.append(f"{i}         {playersName}")

    ###################### This is one way I tried but cannot figure out from here or if even right    ######################

    # for eachLine in players:
    #     [score, player] = eachLine.split(" ")
    #     score = "0000000000" + player
    #     score = score[-10:]
    #     player = player.strip()
    #     players.append(score + " " + player)

    # sort correctly
    ###################### I found this lambda function online, and it does what I want the first time but still issues  ######################
    # You can switch between my lambda and this one and see the results, not sure which is better at this point
    #players.sort(key = lambda x: int("".join([i for i in x if i.isdigit()]))) # If you use this one, it works the first time but then the txt file is messed up.
    players.sort(key = lambda x: (int(x[0])))
    # I can put substitute and it will work
    for eachLine in players[0:5]:
        score = eachLine[0:10]
        player = eachLine[10:20]
        players.append([score, player])
        print(eachLine)

    #We need to write new scores to the txt file
    fixedWidthFile = open("topPlayers.txt", "w")
    for eachLine in players:
        fixedWidthFile.write(eachLine)

    fixedWidthFile.close()
    #File assignment review and writing back out
