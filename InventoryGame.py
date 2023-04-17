

def display_title():    #define display title function
    print("Alyssa Chappell's Inventory Game")    #print title message
    print() #print blank line

def display_menu(): #define display menu function
    print("COMMAND MENU")   #print command menu
    print() #print blank line
    print("show - Show all items")  #print show all items 
    print("grab - Grab an item")    #print grab an item
    print("edit - Edit an item")    #print edit an item
    print("drop - Drop an item")    #print drop an item
    print("exit - Exit program")    #print exit program

def main(): #define main function
    display_title() #call the display title function
    display_menu()  #call the display menu function
    inventory = ["bag", "keys", "bottle"]   #create inventory list
    while True:        #create while loop for commands
        command = input("Command: ")        #command = user input  
        if command == "show":   #if command is show
            show(inventory) #show inventory list
        elif command == "grab": #if command is grab
            grab_item(inventory)    #append an item 
        elif command == "edit": #if command is edit
            edit_item(inventory) #edit an item from the list
        elif command == "drop": #if command is drop
            drop_item(inventory) #delete item
        elif command == "exit": #if command is exit
            break   #break program
        else:   #if anything else
            print("Not a valid command. Please try again.\n")   #display error message
    print("Bye!")   #print bye

def show(inventory):    #define inventory function
    for number, item in enumerate(inventory, start=1):  #create for loop, inventory starts at 1
        print(f"{number}. {item}")  #print index number and item
        print() #print blank line

def grab_item(inventory):   #define grab item function
    if len(inventory) >= 4: #if index num in inventory is greater than or equal to 4
        print("You can't carry any more items. Drop something first.\n")    #print error message
    else:   #else
        item = input("Name: ")  #allow user to enter new item name
        inventory.append(item)  #add to inventory
        print(f"{item} was added.\n")   #print new item name was added

def edit_item(inventory):   #define edit item function
    number = int(input("Number: ")) #allow user to input number
    if number < 1 or number > len(inventory):   #if number is less than 1 or greater than current inventory
        print("Invalid item number.\n") #print error message
    else:   
        item = input("Updated name: ")  #user input's updated name
        inventory[number-1] = item  #update item
        print(f"Item number {number} was updated.\n")   #display update message

def drop_item(inventory):   #define drop item inventory
    number = int(input("Number: ")) #number is user input
    if number < 1 or number > len(inventory):   #if number is less than 1 or greater than inventory
        print("Invalid item number.\n") #print error message
    else:
        item = inventory.pop(number-1)  #drop an item
        print(f"{item} was dropped.\n") #display item was dropped

#call the main function
if __name__ == "__main__":
    main()


