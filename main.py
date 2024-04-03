print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
print("You're at a crossroad. Where do you want to go? On your left a beatuiful lake, and on your right is a dark forest. Choose")

choice1 = input("left or right?")
if choice1 == "left":
  print("you've reached the lake. There is an island in the middle of the lake. Type 'wait' to wait")
  choice2 = input("You see a boat, \ntype wait to wait for the boat. Type swim to swim across river...")
  if choice2 == "wait":
    print("You arrive at the island on the boat unharmed. Now you see a castle with three doors. One red, one yellow and one blue. Which colour do you choose?")
    choice3 = input("red, yellow, or blue door?")
    if choice3 == "red":
      print("You walked into a pit of fire and fell down. You're burned by fire. Game over loser haha")
    elif choice3 == "blue":
      print("You walked into a room of blue beasts. They are hungry and ate you. Game over loser haha")
    elif choice3 == "yellow":
      print("You found the right door and smartly deduce yellow is the color of gold. You win the treasure!")
    else:
      print("You waited too long to choose and the archers station at the top of the castle shot you. You die. Game over... what a sad way to die")
  elif choice2 == "swim":
    print("You idiot why would you swim in a dark mysterious lake. You got attacked by sea monsters and die... Game over")
elif choice1 == "right":
  print("You really think it was a good idea to walk into a dark forest? It was too dark and you didn't see the trap hole laid out with spikes and fell in. Game over you die...")
