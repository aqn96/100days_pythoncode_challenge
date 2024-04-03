rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
comp_choice = random.randint(0,2)
  

if choice == 0:
  print(rock)
  if comp_choice == 0:
    print(f"Computer chose:\n{rock}\n")
    print("It's a draw")
  elif comp_choice == 1:
    print(f"Computer chose:\n{paper}\n")
    print("You lose")
  else:
    print(f"Computer chose:\n{scissors}\n")
    print("You win")
elif choice == 1:
  print(paper)
  if comp_choice == 0:
    print(f"Computer chose:\n{rock}\n")
    print("You win")
  elif comp_choice == 1:
    print(f"Computer chose:\n{paper}\n")
    print("It's a draw")
  else:
    print(f"Computer chose:\n{scissors}\n")
    print("You lose")
else:
  print(scissors)
  if comp_choice == 0:
    print(f"Computer chose:\n{rock}\n")
    print("You lose")
  elif comp_choice == 1:
    print(f"Computer chose:\n{paper}\n")
    print("You win")
  else:
    print(f"Computer chose:\n{scissors}\n")
    print("It's a draw")
    
