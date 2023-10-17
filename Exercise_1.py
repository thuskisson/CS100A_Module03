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

#Print the roster in reverse order
print('Your team roster in reverse is: ')
team.reverse()
for p in team:
    print("\t" + p)

#Search the roster for "Travis" and return a statement
if 'Travis' in team:
    print("I can't wait to play! ")
else:
    print("Put me in coach, I'm ready to play. ")







