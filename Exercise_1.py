#Create an empty list
team = []

#Ask the user for team member names
#Enter "done" when complete
player = ''
while player != 'done':
    player = input('Enter a player name: ')
    if player != 'done':
        #Add the new player to the team roster
        team.append(player)

print('Your team roster in reverse is: ')
team.reverse()
for p in team:
    print("\t" + p)







