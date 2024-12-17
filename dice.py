#Dice Rolling Game
import random
no_of_rolls = int(input("Enter the number of dice you want to roll: "))
count = 0
while True:
    roll = input("Roll the dice? (y/n): ")
    if (roll == "y") or (roll == "n"):
        if (roll == "y" or roll == "Y"):
            for i in range(no_of_rolls):     
                x = random.randint(1,6)
                y = random.randint(1,6)
                count += 1
                my_tuple = (x,y)
                print(my_tuple)
        if (roll == "n" or roll == "N"):
            print("Thanks for playing!")
            print(f"User has rolled the dice {count} times.")
            break
    else:
        print("Invalid choice!")


