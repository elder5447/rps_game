import random

possible_actions = ["rock" , "scissors" , "paper"]

human_turn = "rock"
computer_turn = random.choice(possible_actions)

if computer_turn == human_turn:
    print("niča\n"*10)
elif human_turn == "rock" and computer_turn == "scissors":
  print("winner wineer chicken dinner!!!\n"*100)
elif human_turn == "paper" and computer_turn == "rock":
  print("winner wineer chicken dinner!!!\n"*100)
elif human_turn == "scissors" and computer_turn == "paper":
  print("winner wineer chicken dinner!!!\n"*100)
else:
    print("Žeņas vaina\n"*38)
