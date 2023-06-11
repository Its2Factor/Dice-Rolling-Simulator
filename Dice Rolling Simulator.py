import random

def roll_dice():
    print("- Dice Rolling Simulator -\n")
    
    # The balance you start off with.
    balance = 1000
    bet = 0
    
    while True:
    
        input("Press Enter to roll the dice...")
        
        # Generates random numbers between 1 and 6 and adds dice1 + dice2 to get a total amount.
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
    
        # Displays the current balance.
        print("\n\n\nCurrent Balance:", "$" + str(balance))
        
        print("\nDice 1: ", dice1)
    
                
        # Checks the amount you bet to be equal to half of your balance or less.        
        while True:
            bet = int(input("How much would you like to bet: "))
            if bet <= balance / 2:
                break
            print("\nInvalid amount, you can only bet half your balance or less.\n")
            
        if dice1 == 2:
            double_down = input("Do you want to X4 your bet on both dice being equal to or greater than 8? Yes / No ").lower() == "y"
            if double_down:
                bet *= 4
                
        if dice1 == 3:
            triple_down = input("Do you want to X3 your bet on both dice being equal to or greater than 8? Yes / No ").lower() == "y"
            if triple_down:
                bet *= 3
                
        if dice1 == 6 and dice2 == 6:
            print("\nDiamond Dice, you got X10 your bet.")
            bet *= 10
        
        plus_bal = balance + bet
        minus_bal = balance - bet
        
        if balance > 0:
            print("\n\n\nPrevious Balance:", "$" + str(balance))
            print("Dice 1:", dice1)
            print("Dice 2:", dice2)
            print("Total:", total)

            # Checks if the total is equal to or above the winning threshold.
            if total >= 8:
                if dice1 == 6 and dice2 == 6:
                    balance = plus_bal
                    print("\nDiamond Dice, you won X10 your bet!")
                    print("\nNew Balance:", "$" + str(balance))
                else:
                    balance = plus_bal
                    print("\nYou Won!")
                    print("New Balance:", "$" + str(balance))
                
            else:
                balance = minus_bal
                print("\nYou Lost.")
                print("New Balance:", "$" + str(balance))

            play_again = input("\nPlay again: Yes / No ").lower() == "y"
            if not play_again:
                break
            
        else:
            print("You do not have enough money to play.")
            break
       
roll_dice()
