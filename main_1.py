'''
/// Rock Paper Scissors Game ///

Rules:
s for scissors 
p for paper
r for rock

'''
import random

computer=random.choice([1,0,-1])
print("Welcome to Rock Paper Scissors Game!")
print("Rules: \ns for scissors \np for paper \nr for rock")
you=input("Enter your choice : ")

# input validation
if you not in ['s','p','r']:
    print("Invalid input! \nPlease enter 's', 'p', or 'r'.")
    exit()

youdirt={"s":-1,"p":0,"r":1}
reversed={-1:"scissors",0:"paper",1:"rock"}

youstr=youdirt[you]
print(f"your choice is {reversed[youstr]}")
print(f"computer choice is {reversed[computer]}")

# main logic
if(youstr==-1 or youstr==0 or youstr==1) :
  
  if (youstr==computer):
    print("It's a tie!")
  else:
    if(youstr==1 and computer==-1):
      print("You win!")
    elif(youstr==0 and computer==1):
        print("You win!")
    elif(youstr==-1 and computer==0):
        print("You win!")
    else:
        print("Computer wins!")

   