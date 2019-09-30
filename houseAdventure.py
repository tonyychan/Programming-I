# Tony Chan
# Python House Adventure
# In the first part, there's 3 rooms in a house, one is locked. To get it unlocked, player must turn a dial to a specific colour and a lever to a certain position
# Once unlocking the door, there are 3 more rooms and player must get the plant to be fertilized by distracting a cat and feeding a mouse

def kitch(lever):
	# In the kitchen, there is a lever that you can turn to back or forward and one option is correct in opening the door
	kitchen = True
	while kitchen == True:

		print("\nYou are in the kitchen. You find a lever that can be set to forward or back.")
		print("Menu: \n1. Set the lever to back. \n2. Set the lever to forward. \n3. Return to entrance.")
		print("\nCurrent state of the lever: %s" %(lever))

		arm = str(input("\nWhich option: "))

		if arm == "1":
			print("The lever was set to back.")
			lever = "back"
		elif arm == "2":
			print("The lever was set to forward.")
			lever = "forward"
		elif arm == "3":
			print("You didn't touch the lever.")
			kitchen = False
		else:
			print("Invalid option")
	return lever

def pantry(dial):
	# In the pantry, you will encounter a dial that can be set to three different colours; one is correct for opening the locked door
	pantry = True
	while pantry == True:

		print("\nYou are in the pantry. You find a dial that can be set to blue, green or red.")
		print("""Menu: \n1. Switch the dial to blue. \n2. Switch the dial to green. \n3. Switch the dial to red. \n4. Return to entrance.""")
		print("\nCurrent state of the dial: %s" %(dial))

		switch = str(input("\nWhich option: "))

		if switch == "1":
				print("The dial was set to blue.")
				dial = "blue"
		elif switch == "2":
				print("The dial was set to green.")
				dial = "green"
		elif switch == "3":
				print("The dial was set to red.")
				dial = "red"
		elif switch == "4":
				print("You did not touch the dial")
				pantry = False
		else:
				print("Invalid option")
	return dial

def main():
  # Contains the locked door that can be unlocked via a correct combination
	dial = "green"
	lever = "forward"

	validInput = True
	while validInput == True:
		print("""\nYou are in the entrance hallway. The door you just came in from has disappeared. \nThere are three doors in this room:
		The one in front of you leads to the rest of the house. It is locked.
		To your left is the door that leads into the pantry.
		To your right is the door to the kitchen.""")

		print("""\nMenu: \n1. Try to open the door. \n2. Go through the left entryway. \n3. Go through the right entryway.""")
		option = int(input("which option: "))

		if option == 1:
			# Contains the locked door that can be unlocked via a correct combination
			if dial == "red" and lever == "back":
				print("The door unlocked!")
				validInput = False
			else:
				print("The door is locked.")
		elif option == 2:
			lever = kitch(lever)
		elif option == 3:
			dial = pantry(dial)
		else:
			print("Invalid option.")
main()


def attic(cheese,ball,cat):
  # In the attic, there is cheese you can obtain that can be used for feeding as well as a hole in the ground you can drop something through

	attic = True
	while attic == True:

		if ball == "picked" or ball == "none":
			print("""\nYou are in the attic.\nYou notice a hole in the ground, maybe you can drop something through it. \nYou also find a collection of cheeses.""")
			print("""\nMenu: \n1. Take some cheese. \n2. Drop some cheese in the hole. \n3. Drop the string through the hole. \n4. Return downstairs.""")
			cheehole = int(input("Which option: "))

			if cheehole == 1:
				cheese = "full"
				print("You took some cheese.")
			elif cheehole == 2:
			  if cheese == "full":
			    print("The cheese is too big to fit!")
			  else:
			    print("You have no cheese!")
			elif cheehole == 3:
				if ball == "picked":
					print("Your string disappears down the hole.")
					ball = "dropped"
					cat = "gone"
				else:
					print("You have no string!")
			elif cheehole == 4:
				print("You go back downstairs.")
				attic = False
			else:
				print("Invalid option.")

		elif ball == "dropped":
			print("""\nYou are in the attic.\nYou notice a hole in the ground, maybe you can drop something through it. \nYou also find a collection of cheeses.""")
			print("""\nMenu: \n1. Take some cheese. \n2. Drop some cheese in the hole.\n3. Return downstairs.""")
			cheehole2 = int(input("Which option: "))
			if cheehole2 == 1:
				cheese = "full"
				print("You took some cheese.")
			elif cheehole2 == 2:
			  if cheese == "full":
			    print("The cheese is too big to fit!")
			  else:
			    print("You have no cheese!")
			elif cheehole2 == 3:
				print("You go back downstairs.")
				attic = False
			else:
				print("Invalid option.")

	return cheese,ball,cat

def bedRoom(soil,cheese,ball,cat):
  # In the bedroom, you will encounter a mouse or a cat depending on certain conditions being met. Only when the cat is gone, can the mouse be present

	bedRoom = True
	while bedRoom == True:

		if ball == "none":
			print("\nYou are in the bedroom. You notice a cat that seems to be guarding something, perhaps a mouse hole?")
			print("\nMenu: \n1. Return to the living room.")
			catty = int(input("Which option: "))
			if catty == 1:
				bedRoom = False
			else:
				print("Invalid option.")
		elif ball == "picked":
			print("\nYou are in the bedroom. You notice a cat that seems to be guarding something, perhaps a mouse hole?")
			print("\nMenu: \n1. Return to the living room. \n2. Dangle the string in front of the cat.")
			catty = int(input("Which option: "))
			if catty == 1:
				bedRoom = False
			elif catty == 2:
				print("The cat takes its attention toward the string. It does not seem to want to budge however.")
			else:
				print("Invalid option.")
		elif cheese == "empty" and ball == "dropped":
			print("\nYou are in the bedroom. The cat is nowhere to be seen. Now you notice a mouse that is out of its mouse hole.")
			print("\n1. Return to the living room.")
			catty = int(input("Which option: "))
			if catty == 1:
				bedRoom = False
			else:
				print("Invalid option.")
		elif cheese == "full" and ball == "dropped":
			print("\nYou are in the bedroom. The cat is nowhere to be seen. Now you notice a mouse that is out of its mouse hole.")
			print("""\nMenu: \n1. Give the mouse some cheese. \n2. Return to living room.""")
			chefee = int(input("Which option: "))
			if chefee == 1:
				print("The mouse happily ate the cheese.")
				soil = "wet"
			elif chefee == 2:
				print("The mouse just stared.")
				bedRoom = False
			else:
				print("Invalid option.")

	return soil,cheese,ball,cat

def livRoom(soil,cheese,ball,cat):
# In the living room, you can look at a pot of soil, obtain a ball of string or choose to go to different room
	validInput = True
	while validInput == True:
		if ball == "picked" or ball == "dropped":
			print("""\nYou are in the living room. he door you just came in from has disappeared. \nYou notice a number of things:
				In front of you, you see a pot of soil on the table.
				To your left is a dark doorway.
				To your right are a set of stairs going up.""")
			print("""\nMenu: \n1. Look at the pot of soil. \n2. Go through the dark doorway. \n3. Go upstairs.""")
		else:
			print("""You are in the living room. The door you just came in from has disappeared. \nYou notice a number of things:
				In one corner, you see a pot of soil on the table.
				In the other corner, you see a ball of string.
				To your left is a dark doorway.
				To your right are a set of stairs going up.""")
			print("""\nMenu: \n1. Look at the pot of soil. \n2. Go through the dark doorway. \n3. Go upstairs. \n4. Pick up the ball of string.""")
		option2 = int(input("Which option: "))

		if option2 == 1:
			if soil == "dry":
				print("The soil looks rather dry.")
			elif soil == "wet":
				print("The soil is fertilized and a vine starts to grow! Thanks for playing!")
				validInput = False

		elif option2 == 2:
			soil,cheese,ball,cat = bedRoom(soil,cheese,ball,cat)
		elif option2 == 3:
			cheese,ball,cat = attic(cheese,ball,cat)
		elif option2 == 4:
			ball = "picked"
			print("You picked up the ball of string.")
		else:
			print("Invalid option.")

def main2():

	soil = "dry"
	cheese = "empty"
	ball = "none"
	cat = "present"
	livRoom(soil,cheese,ball,cat)

main2()
