
"""
This program takes string input and checks if that string is in a list of strings

if string is in the list it removes the first instance from list
if string is not in the list the input gets appended to the list
if the string is empty then the last item is popped from the list
if the list becomes empty the program ends
if the user enters "quit" then the program ends
"""


class CheckStringList():

	def __init__(self, entity_list):
		self.entity_list = entity_list
		self.get_user_choice()

	def construct_entity_list(self, new_entity):
		if new_entity == "":
			  entity = entity_list.pop()
			  print(new_entity + " has been popped from list")
		elif new_entity.lower() in entity_list:
			  print(new_entity + " has been removed from list")
			  return entity_list.remove(new_entity)
		else:
			  print ("1 instance of " + new_entity + " has been appended to the list")
			  return entity_list.append(new_entity)

	def get_user_choice(self):
		while self.entity_list:
			new_entity = input("Please enter any entity name to add to list or press 'q' to quit program: ")
			if new_entity.lower() == "q":
				print("Quitting program now")
				break
			else:
				print("List of entitys: " + str(entity_list))
				self.construct_entity_list(new_entity)
				print (entity_list)
		print ("Goodbye!")


if __name__ == '__main__':
	entity_list = ["rabbit", "lion", "dog"]
	CheckStringList(entity_list)
					
