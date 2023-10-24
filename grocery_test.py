# Write a program that asks the user for items for a grocery list.
# Then, as the user is walking through the store, they can input what 
# they just put in their cart. If that item is in the list, remove that 
# item (using remove). Loop until the list is empty, then tell the user 
# they can check out now.

from emoji import emojize

print(emojize(':thumbs_up:'))

grocerylist = []
item = input('what do you need at the store? ')
while item != 'done':
    grocerylist.append(item)
    item = input('what else do you need at the store, or type "done" to stop? ')

if 'ice cream' in grocerylist:
    print('oh boy, I love ice cream')

print("Let's go to the store.")

cart = []
while len(grocerylist) > 0:
    item = input('what did you put in the cart? ')
    
    if item in grocerylist:
        grocerylist.remove(item)
    else:
        print('you strayed from the list')

    qty = int(input('how many did you get? '))
    cost = float(input('what is the unit price? '))

    cart.append((item, qty, cost))

print("time to check out")

totalcost = 0
for (item, qty, cost) in cart:
    print(f'\t{item} @ ${cost:.2f} X {qty} = ${cost*qty:.2f}')
    totalcost = totalcost + (qty*cost)
print('----------------------------------')
print(f'total: ${totalcost:.2f}')