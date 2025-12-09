from room import Room
from treasure import Treasure

class Game:
    """An adventure game exploring Mark's house."""

    def __init__(self) -> None:
        #Create Rooms
        front_yard = Room("Front Yard", 
            "The cool Montana breeze hits your face as you stand on the walkway. "
            "You see your cozy home ahead — time to head inside.")
        
        porch = Room("Porch", 
            "A pile of shoes rests by the door. The faint smell of coffee drifts out from inside.")
        
        living_room = Room("Living Room", 
            "Soft light glows from a floor lamp. A big screen TV shows a Colorado Avalanche game replay.")
        
        kitchen = Room("Kitchen", 
            "Counters covered with snacks and a laptop open on a coding project. "
            "A pot of coffee bubbles quietly.")
        
        garage = Room("Garage", 
            "Tools, bikes, and a small workbench covered in sawdust. "
            "A half-finished woodworking project sits in the corner.")
        
        hallway = Room("Hallway", 
            "Family photos line the wall. You can hear faint music from one of the rooms ahead.")
        
        bedroom = Room("Bedroom", 
            "A messy desk setup faces the window, with a dual-monitor rig and notebooks open from CSCI classes.")
        
        bathroom = Room("Bathroom", 
            "Bright lights, clean mirror, and a towel neatly folded. Everything in its place.")
        
        backyard = Room("Backyard", 
            "Freshly cut grass and a peaceful view of the Yellowstone River The sun is setting — "
            "but the door locks behind you! Maybe this is the end of your adventure.")

        #Connect Rooms
        front_yard.add_exits([porch])
        porch.add_exits([front_yard, living_room])
        living_room.add_exits([porch, kitchen, hallway])
        kitchen.add_exits([living_room, garage])
        garage.add_exits([kitchen])
        hallway.add_exits([living_room, bedroom, bathroom])
        bedroom.add_exits([hallway, backyard])
        bathroom.add_exits([hallway])
        backyard.add_exits([])  #Dead end

        #Create Treasures
        coffee_mug = Treasure("Coffee Mug", 10, "A mug with a Colorado Avalanche logo.")
        coding_book = Treasure("Python Handbook", 25, "A well-used guide full of notes and tabs.")
        golden_hammer = Treasure("Golden Hammer", 50, "A shiny hammer resting on the garage workbench.")

        #Place Treasures in Rooms
        kitchen.treasure = coffee_mug
        bedroom.treasure = coding_book
        garage.treasure = golden_hammer

        #Starting Room & Backpack
        self.rooms = [front_yard, porch, living_room, kitchen, garage, hallway, bedroom, bathroom, backyard]
        self.current_room = front_yard
        self.backpack = []

    def play(self):
        """Explore the house, collect treasures, and escape to the backyard."""
        print("Welcome to Mark's House Adventure!")
        print("Explore the rooms, collect treasures, and see what you discover!\n")

        while True:
            print('')
            print(f'*** You are in {self.current_room.name}. ***')
            print('-----')
            print(self.current_room.description)

            #End condition
            if self.current_room.name == "Backyard":
                print("\nYou made it outside... but the door locks behind you!")
                break

            #Check for treasure
            if hasattr(self.current_room, 'treasure') and self.current_room.treasure:
                print(f"\nYou see a treasure here: {self.current_room.treasure}")

            #Player options
            print("\nOptions:")
            print("(e) Exit this room")
            print("(p) Pick up treasure")
            print("(i) Check inventory")
            print("(q) Quit the game")

            choice = input("\nWhat do you want to do?: ").lower()

            if choice == 'e':
                print("")
                counter = 1
                for room in self.current_room.exits:
                    print(f'{counter}) {room.name}')
                    counter += 1

                while True:
                    try:
                        selection = int(input("Which room would you like to go to?: "))
                        if 1 <= selection <= len(self.current_room.exits):
                            self.current_room = self.current_room.exits[selection - 1]
                            break
                        else:
                            print(f"Please enter a number between 1 and {len(self.current_room.exits)}.")
                    except ValueError:
                        print("Invalid input — please enter a number.")

            elif choice == 'p':
                if hasattr(self.current_room, 'treasure') and self.current_room.treasure:
                    treasure = self.current_room.treasure
                    self.backpack.append(treasure)
                    print(f"\nYou picked up {treasure.name}!")
                    self.current_room.treasure = None
                else:
                    print("\nThere’s nothing to pick up here.")

            elif choice == 'i':
                if self.backpack:
                    print("\nYour Backpack contains:")
                    total_value = 0
                    for item in self.backpack:
                        print(f" - {item.name} (worth {item.value} points)")
                        total_value += item.value
                    print(f"Total treasure value: {total_value} points")
                else:
                    print("\nYour backpack is empty.")

            elif choice == 'q':
                print("\nYou chose to quit the game.")
                break

            else:
                print("\nInvalid choice. Please enter e, p, i, or q.")

        #Game summary
        total = sum(item.value for item in self.backpack)
        print("\nGame Over!")
        print(f"You collected {len(self.backpack)} treasures worth {total} points total.")
        print("Thanks for playing Mark's House Adventure!")
