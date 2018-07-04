"""
Reads a CVS document full of 18 children who have signed up for the league
Divides the children into three even teams - Dragons, Sharks and Raptors
Generates a new text file displaying the three teams
Author: Zachary Collins
Date: July, 2018
"""

players_new = []
players = []
experienced_players = [] 
not_experienced_players = []
Sharks = []
Dragons = []
Raptors = []

#Reads the CSV document and adds each line into a list of players
with open("soccer_players.csv", "r") as file:
    for line in file:
        players_new.append(line)
        
def remove_height(players_new):
    """Formats the string so that height is no longer included in each player's string"""
    
    for player in players_new[1:]:
        player = ''.join([i for i in player if not i.isdigit()])
        player = player.replace(",", "", 1)
        players.append(player)
    #Adds a next line after the final player in the list
    players[-1] = players[-1] + "\n"
        
                

def group_players(players):
    """Groups players and splits the experienced and non-experienced players into teams evenly"""
    
    #Groups players into experienced and not experienced groups
    for player in players:
        if "YES" in player:
            experienced_players.append(player)
        if "NO" in player:
            not_experienced_players.append(player)
    
    #Groups Experienced players onto teams        
    for player in experienced_players[0:3]:
        Sharks.append(player)
    for player in experienced_players[3:6]:
        Dragons.append(player) 
    for player in experienced_players[6:]:
        Raptors.append(player)
        
    #Groups Non-Experienced players onto teams
    for player in not_experienced_players[0:3]:
        Sharks.append(player)
    for player in not_experienced_players[3:6]:
        Dragons.append(player)
    for player in not_experienced_players[6:]:
        Raptors.append(player)



if __name__ == "__main__":
    remove_height(players_new)
    group_players(players)
    #Writes the teams to a teams.txt file
    with open("teams.txt", "w") as file:
        file.write("Sharks\n")
        for player in Sharks:
            file.write(player)
        file.write("\nDragons\n")
        for player in Dragons:
            file.write(player)
        file.write("\nRaptors\n")
        for player in Raptors:
            file.write(player)
            
