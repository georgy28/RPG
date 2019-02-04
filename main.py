import random
from game import Person

# Returns True if a player from the list has died
def someone_died(players: list):
    dead = False
    for player in players:
        if player.hp == 0:
            dead = True
            break
    
    return dead

# Print stats of all the players
def show_stats(players: list):
    for player in players:
        player.get_stat()

# Initialize players
# More general way using list, so we can expand the game easily if we want to add more players
players = []
players.append(Person("Thor", 100, 100, 30))
players.append(Person("Thanos", 100, 100, 25))

# Game initial prints
print ("This game is ....")
for player in players:
    player.get_stat()

# Highlander Game "There can be only one!"
# This is the main game loop

while (len(players) > 1): # If there are more players than just ONE
    while not someone_died(players): # as long as they have health, then they fight
        for player in players:
            player.take_dmg(20) # for now
        show_stats(players)
    
    # Someone (or more) died
    # Print message and remove him/them from the list
