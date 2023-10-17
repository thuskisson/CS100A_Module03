# Create an empty list
list = []

# ask the user for items
# enter 'done' when complete
item = ''
while item != 'done':
    item = input('Enter an item to add to the list: ')
    if item != 'done':
        #add the new item to the list
        list.append(item)

print('your list is : ')
for p in list:
    print("\t" + p)


