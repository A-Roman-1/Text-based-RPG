# Text-based-RPG
A text based game, where the player can go around a map and attack players or buy items.


The project involved creating a game by following the provided steps. We structured the project by splitting the functions across multiple files to make the program's construction easier to understand.

Base_class.py contains three key classes: Inspectable, Interactable, and Attack. These serve as base classes for other components of the game, allowing for inheritance and reuse in the project.

Room.py defines the map of the game world, connecting different spaces and placing the player and NPCs in specific locations.

Door.py ensures that connections between rooms are handled safely, preventing any issues with transitions from one room to another.

Player.py manages the player's attributes such as health, damage, and currency. We focused on encapsulating these characteristics to prevent them from being unintentionally altered.

Dealer.py introduces a new NPC class, the "Dealer." The player can earn money by defeating certain NPCs and then exchange this money with the Dealer for upgrades like improved health or increased power.

Game.py contains the main logic of the game, handling actions and interactions between the player and NPCs. For example, it manages the player's quest to find a way out, displays available doors, and handles interactions with the NPCs.

Main.py is where we defined all the NPCs, the player, and the connections between rooms. It serves as the central hub for initializing and organizing the game’s components.

The game we created is based on the popular tv series Breaking Bad. The player takes on the role of Walter White, exploring five different place: Walt's living room, the meth lab, the car wash, Gus' restaurant, and Jesse's basement. In these rooms, there are several NPCs, including Skyler, Jesse, Tuco and Hector Salamanca, a dealer (Skinny Pete) and others.The dealer allows Walt to exchange money (earned by defeating other NPCs) for life potions or a weapon with a stronger critical hit to defeat other enemies.

Testing:
The assignment involved a testing phase to ensure the proper functioning of all classes and functions. We implemented tests to verify that the code operates without errors and behaves as expected. In addition to individual unit tests for each class, we tested the interactions between them to ensure smooth functionality and to catch any potential issues.

Furthermore, we conducted an end-to-end test to simulate the entire game, ensuring that all elements, from gameplay mechanics to player interactions, worked without any errors. This helped confirm that the game runs smoothly without issues during execution.
