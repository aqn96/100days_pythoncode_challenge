from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
print("Welcome to the secret auction program.")

user = {}

def add_user(name, bid):
  user[name] = bid

def highest_bidder(user_bid):
  highest_bid = 0
  winner = ""
  if user_bid == "":
    print("No bidders")
  else:
    for user in user_bid:
      curr_bid = user_bid[user]
      if curr_bid > highest_bid:
        highest_bid = curr_bid
        winner = user
  print(f"The winner is {winner} with a bid of ${highest_bid}")
    
more_User = True

while more_User:
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  add_user(name, bid)
  answer = input("Are there any other bidders? Type 'yes' or 'no'. ")
  if answer == 'no':
    more_User = False
  clear()
  print(logo)

highest_bidder(user)