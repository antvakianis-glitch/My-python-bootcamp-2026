import random

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
my_list = [rock, paper, scissors]
mine = input("Type 0 for rock, 1 for paper, 2 for scissors:")
comp = random.choice(my_list)
if mine == "0":
    mine = rock
elif mine == "1":
    mine = paper
elif mine == "2":
    mine = scissors

print(f"you chose: {mine}")
print(f"computer chose: {comp}")

if mine == comp:
    print("its a draw!")
elif (mine == rock and comp == scissors) or \
        (mine == paper and comp == rock) or \
        (mine == scissors and comp == paper):
    print("You win!")
else:
    print("You lose!")
