import random

possible_actions = ["rock" , "scissors" , "paper"]

human_turn = input("enter your turn\n")
computer_turn = random.choice(possible_actions)

print(f'Human:{human_turn} vs. Computer:{computer_turn}')
if computer_turn == human_turn:
    print("niča\n"*10)
elif human_turn == "rock" and computer_turn == "scissors":
  print("winner wineer chicken dinner!!!\n"*10)
elif human_turn == "paper" and computer_turn == "rock":
  print("winner wineer chicken dinner!!!\n"*10)
elif human_turn == "scissors" and computer_turn == "paper":
  print("winner wineer chicken dinner!!!\n"*10)
else:
    print("You loose\n"*10)
