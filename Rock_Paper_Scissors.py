import random#importing random to randomize the computers choice
computer_choice = random.choice(['rock','paper','scissors'])#this is a list in python,and we are passing in the list as a parameter in the choice function from the random module
user_choice = input('Do you want rock, paper,or scissors?')
print('computer choice:', computer_choice)

if computer_choice == user_choice:
    print('TIE')
elif user_choice == 'rock'and computer_choice == 'scissors':
    print ('WIN')    
elif user_choice == 'paper'and computer_choice == 'rock':
    print ('WIN') 
elif user_choice == 'scissors'and computer_choice == 'paper':
    print ('WIN')
else:
    print('you loose, computer wins')         
