import random
data = ['rock', 'paper', 'scissor']
rand = random.choice(data)
user = input("enter your chance: \nRock \nPaper \nScissor \n---------------------\n")
score = 0
num = 0
while score < 10 or num <10:
    if user.lower() == 'rock':
        if rand.lower() == 'paper':
            print("Paper \n You Lost!")
            num += 1
        elif rand.lower() == 'scissor':
            print("Scissor \n You Won!")
            score += 1
        else:
            print("Rock\n Tie ")
    elif user.lower() == 'paper':   
        if rand.lower() == 'scissor':
            print("Scissor \n You Lost!")
            num += 1
        elif rand.lower() == 'rock':
            print("Rock \n You Won!")
            score += 1
        else:
            print("Paper\n Tie ")
    elif user.lower() == 'scissor':
        if rand.lower() == 'rock':
            print("Rock \n You Lost!")
            num += 1
        elif rand.lower() == 'paper':
            print("Paper \n You Won!")
            score += 1
        else:
            print("Scissor\n Tie ")



print(f'Your score is {sum}')
print(f"Computer score is {num}")
if (sum > num):
    print("CONGRATULATIONS, YOU WON  \n*****************************************************\n")
else:
    print("You lost")