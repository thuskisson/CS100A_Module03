#Create an empty list
store_list = []

#Ask the user for a list of items needed at the grocery store
#Enter "none" when complete

store_item = input('What do you need from the store? ')
while store_item != 'done':
#Add the new item to the grocery store list
    store_list.append(store_item)
    store_item = input('What else do you need at the store? Type "done" to exit: ')


#Display the grocery list
print("Your grocery list is: ")
for i in store_list:
    print("\t" + i)

#Tell the user to go to the store
print('Now go to the store. As you add items into the cart, input them below. ')

#Prompt the user for items they put in the cart, then remove them from the store list

while len(store_list) != 0:
    item = input("What did you put in your cart? ")

    if item in store_list:
        store_list.remove(item)
    else:
        print("You strayed from the list. ")
