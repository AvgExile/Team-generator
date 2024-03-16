import random

#list of players
players = ["Martin", "Craig", "Sue",
           "Claire", "Dave", "Alice",
           "Sonakshi", "Harry", "Jack",
           "Rose", "Lexi", "Maria",
           "Thomas", "James", "William",
           "Ada", "Grace", "Jean",
           "Marrisa", "Alan"]

print("Welcome to the Team Allocator")
random.shuffle(players)

#Allocates 50% of players to Team1
team1 = players[:len(players)//2:]
print("Team 1 Captain: " + random.choice(team1))
print("Team 1:")
for players in team1:
    print(players)

#Allocates 50% of players to Team2
team2 = players[:len(players)//2:]
print("\nTeam 2 Captain: " + random.choice(team2))
print("Team 2:")
for players in team2:
    print(players)
