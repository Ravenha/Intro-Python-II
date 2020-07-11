from room import Room
from player import Player
from item import Item


# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mouth beckons"),

    'foyer':    Room("--- Foyer",
                     """Dim light filters in from the south. Dusty passages run north and east."""),

    'overlook': Room("--- Grand Overlook",
                     """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),

    'narrow':   Room("--- Narrow Passage",
                     """The narrow passage bends here from west to north. The smell of gold permeates the air."""),

    'treasure': Room("--- Treasure Chamber",
                     """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."""),

    'dragon':   Room("--- Dragons Chamber",
                     """Before you sits a White Dragon its golden eyes glinting in the dim light as he stares at you, 'Why do you come here? I have nothing for you.'""")

}

# Put items in rooms
room['outside'].add_item('rock')
room['foyer'].add_item('sword')
room['foyer'].add_item('bow')
room['foyer'].add_item('arrows')
room['foyer'].add_item('dagger')
room['overlook'].add_item('lantern')
room['narrow'].add_item('tarnished dragon figurine')
room['treasure'].add_item('rope')

# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# Main
name = input('What is your name, adventurer? ')

player = Player(name, room['outside'])

print(f'--- Welcome, {player.name}! Your current location is: {player.room_info()}')

def item(player, item):
    interact = input('What would you like to do? (HINT: You may "take" or "ignore" an item.) ')
    interact = interact.lower()

    if interact == 'take':
        player.inventory.append(item)
        print(f'--- You now have {player.inventory} in your inventory.')
        player.current_room.item_taken(item)
        gameplay(player)
    elif interact == 'ignore':
        print('--- You leave it there.')
        gameplay(player)
    else:
        print('--- There seems to have been an error. Please try again.')
        gameplay(player)

def gameplay(player):
    direction = input('What would you like to do? (N to go north, S to go south, E to go east, W to go west, I to investigate the room, IN to interact with your inventory, Q to quit) ')
    direction = direction.lower()

    if direction == 'n':
        location = player.current_room.n_to
        if location != None:
            player = Player(name, location)
            print(player.room_info())
            gameplay(player)
        else:
            print('--- There is nothing to the north. Please choose a different direction.')
            gameplay(player)
    elif direction == 's':
        location = player.current_room.s_to
        if location != None:
            player = Player(name, location)
            print(player.room_info())
            gameplay(player)
        else:
            print('There is nothing to the south. Please choose a different direction.')
            gameplay(player)
    elif direction == 'e':
        location = player.current_room.e_to
        if location != None:
            player = Player(name, location)
            print(player.room_info())
            gameplay(player)
        else:
            print('There is nothing to the east. Please choose a different direction.')
            gameplay(player)
    elif direction == 'w':
        location = player.current_room.w_to
        if location != None:
            player = Player(name, location)
            print(player.room_info())
            gameplay(player)
        else:
            print('There is nothing to the west. Please choose a different direction.')
            gameplay(player)

    elif direction == 'i':
        print(player.investigate())
        object = player.investigate()[14:-1]

        if player.investigate() != "--- There is nothing here.":
            item(player, object)
        else:
            gameplay(player)

    elif direction == 'in':
        if player.inventory != []:
            print(f'--- You currently have {player.inventory} in your inventory.')
            command = input('You can "drop" an item or "use" an item. Please name the item. (Example: "use rock") ')
            command = command.lower()
            action, thing = command.split(' ')[0], command.split(' ')[1]
            if action == 'drop':
                if thing in player.inventory:
                    player.inventory.remove(thing)
                    player.current_room.add_item(thing)
                    print(f'--- You currently have {player.inventory} in your inventory.')
                    gameplay(player)
                else:
                    print('--- There seems to have been an error. Please try again.')
                    gameplay(player)
            elif action == 'use':
                if thing == "rope":
                    if player.current_room.name == "--- Grand Overlook":
                        print('--- Success! You fashion a swing and lauch yourself across the chasm, landing safely on the other side.')
                        player.current_room = room['dragon']
                        print(player.room_info())
                        gameplay(player)
                    else:
                        print(f'The {thing} does not do anything here.')
                        gameplay(player)
                elif thing == "sword":
                    if player.current_room.name == "--- Dragons Chamber":
                        print('--- You draw your sword and charge forward.')
                        print('--- The dragon burns you mid step.')
                        print('--- Game Over!')
                    else:
                        print(f'--- The {thing} does not do anything here.')
                        gameplay(player)
                elif thing == "dagger":
                    if player.current_room.name == "--- Dragons Chamber":
                        print('--- You draw your dagger and charge forward.')
                        print('--- The dragon burns you mid step.')
                        print('--- Game Over!')
                    else:
                        print(f'--- The {thing} does not do anything here.')
                        gameplay(player)
                elif thing == "bow":
                    if player.current_room.name == "--- Dragons Chamber":
                        print('--- You nock an arrow and take aim and let loose a volly of arrows.')
                        print('--- The dragon screams and lashes out.')
                        print('--- His tail catches you in the temple and you collapse dead.')
                        print('--- Game Over!')
                    else:
                        print(f'--- The {thing} does not do anything here.')
                        gameplay(player)
                elif thing == "tarnished dragon figurine":
                    if player.current_room.name == "--- Dragons Chamber":
                        print('--- The dragon eyes the figurine and nods')
                        print('--- you may take as much as your pockets can hold')
                        print('--- You leave the cave richer than when you started')
                        print('--- Congratulations')
                    else:
                        print(f'--- The {thing} does not do anything here.')
                        gameplay(player)
                elif thing == "rock":
                    if player.current_room.name == "--- Grand Overlook":
                        print('you listen to the silence as you toss the rock down, it takes several minutes before you faintly hear it hit the bottom.')
                        print('--- you decide not to jump.')
                    else:
                        print(f'--- The {thing} does not do anything here.')
                        gameplay(player)
                else:
                    print(f'--- The {thing} does not do anything here.')
                    gameplay(player)
            else:
                print('--- There seems to have been an error. Please try again.')
                gameplay(player)
        else:
            print('You have nothing in your inventory.')
            gameplay(player)


    elif direction == 'q':
        print('--- Farewell, adventurer!')

    else:
        print('---There seems to have been an error. Please try again.')
        gameplay(player)

if __name__ == '__main__':
    gameplay(player)
