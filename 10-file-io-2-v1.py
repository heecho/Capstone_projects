

'''

A csv file is a very simple file that is used quite often. Usually a csv file will look something like this

A simple expenses csv file

---
name,amount,monthly
food,1000.00,y
rent,2000.00,y
braces,2000.00,n
---


A csv usually starts with a header line that lists the names of the fields so someone reading or importing it into a spreadsheet app knows what each column is for.

The task is to write a simple budget app. This application will have a simple interface that shows the list of commands to the user, and allows to enter a command and keep doing it until they say
quit. 

It will store the data it gets from the user in a csv file. 

The program will have the following commands

1. Open a file - should then ask the user for the file name to open
2. Save file
3. Show items in the budget - calculates the total amount of expenses
4. Add an item to the budget - should ask the user for each field name, amount, monthly
5. Remove an item from the budget

On open the program needs to read in the file data, and on save write out the changes. You can only use the tools shown, no extra modules.

To test you should be able to open the file in a spreadsheet application after closing.

'''
import os
from collections import OrderedDict

#Displays the menu options to the user
def print_menu():
	print "Menu options: "
	print "To open a file, Enter 'o'  "
	print "To Add an item to the Budget, Enter 'a' "
	print "To Remove an Item from the budget, enter 'r' "
	print "To Save a file, Enter 's' "
	print "To List Items in budget, Enter 'l' "
	print "To QUIT enter 'q' "

def user_input(string):
	return raw_input(string)


#Checks to see if the filename exists, if it does, read in the existing data and put in the data store
#if not a new file will be created in the save_file function
def open_file(filename):
	exist = os.path.exists(filename)
	data_in = []
	if exist == True:
		with open(filename,"r") as f:
			readin = f.readlines()
			for x in readin[1:]:
				y = x.strip('\n').split(',')
				create = OrderedDict({})
				create['Item'] = y[0]
				create['Cost'] = float(y[1])
				create['monthly'] = y[2]
				data_in.append(create)
		return data_in
	else:
		data_in = []
		return data_in

#Displays a header line based on the keys in create_item
#**GO BACK store header as a separate variable**
def header(data):
	category = data[0]
	x = category.keys()
	header = ",".join(x)
	return header

#Converts the data array to a string
# def data_to_string(data):
# 	data_string = ''
# 	for x in data:
# 		val = x.values()
# 		valstrg = [val[0], val[1]), val[2]]
# 		data_string += ','.join(valstrg) + "\n"
# 	display = header(data) + "\n" + data_string
# 	#print display
# 	return display

def data_to_string(data):
	data_string = ''
	for x in data:
		val = x.values()
		data_string += ','.join(val) + "\n"
	#display = header(data) + "\n" + data_string
	return data_string

#Writes the data(in string format) to the file
def save_file(filename,data):
 	with open(filename, "w") as f:
 		f.write(data_to_string(data))

#Calculates the budget total cost based on monthly or singular expenses
def total_cost(data):
    total = 0.00
    price  = 0.00
    monthly = 0.00
    for x in data:
    	answer = x["monthly"]
        if answer.lower() == 'y':
            monthly += x["Cost"] * 12
        else:
            price += x["Cost"]
        total = price + monthly
    return total

#Displays item lines in file and total cost
def display_list(data):
	print data_to_string(data)
	print "Total($):   " + str(total_cost(data))

#Creates a singular entry, stored as a dictionary
def create_item():
	item = OrderedDict()
	item["Item"] = user_input("Name of Item: ")
	item["Cost"] = user_input("Cost of Item: ")
	answer = user_input("Is this a monthly expense? Please enter y or n: ")
	item['monthly'] = answer.lower[0]
	
	return item

#Stores item dictionaries into the data array
def add_data(data):
	data.append(create_item())
	return data

#removes an entry from list or alerts user tha item is not in the list
def remove_line(data):
	remove = user_input("Please enter the name of the item you would like to remove: ")
	error_message = 0
	for x in data:
		if remove == x['Item']:
			data.remove(x)
		else:
			error_message += 1
	if error_message > 0:
		print "this item does not exist"
	return data

menu_dict = {'o': open_file,
		's': save_file,
		'r': remove_line,
		'l': display_list,
		'a': add_data}	

def ui_loop():
	state = {'filename' : "", 'data': []}
	while True:
		print_menu()
		user_selection = raw_input('Selection: ')
		if user_selection == 'q':
			break
		if menu_dict.has_key(user_selection):
			menu_dict[user_selection](state)
ui_loop()  

	# while True:
	# 	print_menu()
	# 	user_selection = raw_input('Selection: ')
	# 	if user_selection.lower() == "o":
	# 		filename = raw_input("What do you want to name your file? ")
	# 		open_file(filename)
	# 	elif user_selection.lower() == "s":
	# 		save_file(filename, data)
	# 	elif user_selection.lower() == "a":
	# 		add_data(data)
	# 	elif user_selection.lower() == "r":
	# 		remove_line(data)
	# 	elif user_selection.lower() == "l":
	# 		display_list(data)
	# 	elif user_selection.lower() == "q":
	# 		break
	# 	else:
	# 		print "your selection is not in the menu. please try again"

		
				
  
    
