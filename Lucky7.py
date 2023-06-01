import random  # importing the random module
print("LUCKY SEVEN")
choice = "yes"
profit = 0
loss = 0
error = 0
while (choice == "yes" or choice == "y"):
    bet_amount = int(input("Enter your bet: "))

    # entering a number in the range of 1 to 12
    selected_number = int(input("Enter a number from the range of 1 to 12: "))

    if (selected_number <= 0):  # Checking if the  selected nummber is lessthan 0
        error = 1
        print("\nPlease enter a nummber greater than 1\n ")
        break
    elif selected_number > 12:  # Checking if the  selected nummber is greater than 12
        error = 1
        print("\nPlease enter a number less than 12\n ")
        break

    # generating a random number in the range of 1 to 6
    dice_1 = random.randint(1, 6)
    # generating a random number in the range of 1 to 6
    dice_2 = random.randint(1, 6)

    print("Value of first dice is: ", dice_1)
    print("Value of first dice is: ", dice_2)
    dice_roll = dice_1 + dice_2

    if (selected_number < 7) and dice_roll < 7:
        print("\n Congratulations,you have won")
        profit = profit+bet_amount*2-loss
        print("You have won %d Rupees" % (profit))

    elif (selected_number > 7) and dice_roll > 7:
        print("\n Congratulations,you have won")
        profit = profit+bet_amount*2-loss
        print("You have won %d Rupees" % (profit))

    elif selected_number == 7 and dice_roll == 7:
        print("\n Congratulations,you have won")
        profit = profit+bet_amount*2-loss
        print("You have won %d Rupees" % (profit))

    else:
        print("\n Sorry,better luck next time")
        loss = loss+bet_amount
        print("you have lost %d Rupees" % (loss))

    choice = input("Do you want to continue : ")

if (error == 0):
    print("Total profit: ", profit-loss)
else:
    print("Invalid number")
