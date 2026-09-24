def show_help():
    print("Type 'help' to get a list of all the things you can do")
    print("Type 'see' to get a list of all the animals")
    print("Type 'pet <animal>' to pet a particular animal")
    print("Type 'bye' to leave the zoo and exit the program")

def show_all_animals():
    print("The animals in the zoo are:")
    print("• Clover the Bunny 🐇")
    print("• Coco the Baby Goat 🐐")
    print("• Arno the Alligator 🐊")

def pet_animal(animal):
    if animal == "clover":
        print("You pet Clover the Bunny 🐇. She nuzzles your hand happily!")
    elif animal == "coco":
        print("You pet Coco the Baby Goat 🐐. She bleats joyfully!")
    elif animal == "arno":
        print("You pet Arno the Alligator 🐊. He gives you a toothy grin!")
    else:
        print(f"There is no animal named '{animal}' in the zoo. Please try again.")

print("Welcome to the Petting Zoo!")
print("Type 'help' to get a list of all the things you can do")
print()

while True:
    response = input("What would you like to do? ").strip().lower()

    if response == "help":
        show_help()

    elif response == "see":
        show_all_animals()

    elif response.startswith("pet "):
        animal = response[4:].strip()
        pet_animal(animal)

    elif response == "bye":
        print("Thanks for visiting the Petting Zoo! Goodbye!")
        break

    else:
        print("Invalid command. Type 'help' to see the list of available commands.")
