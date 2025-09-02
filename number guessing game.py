from random import randint
print("Welcome !\nI'm thinking of a number right now, can you guess it ?")

gn=randint(1,100)
emh={"easy" : 11,"medium" : 6,"hard" : 4}
print("Difficulty levels\nEasy : 10\nMedium : 5\nHard : 3")
while True:
    emH=input("\nEnter your choice in difficulty :").lower()
    if emH not in emh.keys():
          print(f"youre suppose to type either [easy|medium|hard]!! not {emH}")
    else:
          break
print(f"Great ! ,you have chosen {emH.capitalize()} difficulty level ! ! \n lets start the game!")

for i in range (1,emh[emH]):
    guess=int(input("Enter your guess :"))
    if guess==gn:
        print("Congratulations ! !\nYou got it in ",i," tries!")
        break
    elif guess>gn:
            print("INCORRECT !Lower !")
    else:
            print("INCORRECT !Higher !")
else:
      print(f"You lost !!\nThe number was {gn} !!")