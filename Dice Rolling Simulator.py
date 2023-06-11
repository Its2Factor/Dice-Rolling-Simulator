import locale
import random

def roll_dice():
    print("- Dice Rolling Simulator -\n")
    
    # The balance you start off with.
    balance = 2099
    bet = 0
    
    # Set the locale for formatting currency
    locale.setlocale(locale.LC_ALL, '')
    
    while True:
        # Generates random numbers between 1 and 6 and adds dice1 + dice2 to get a total amount.
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        
        input("Press Enter to roll the dice...")
        
        print("\n\n\nDice 1:", dice1)
        
        # Checks the amount you bet to be equal to half of your balance or less.
        max_bet = balance // 2
        
        while True:
            print("\nCurrent Balance:", locale.currency(balance, grouping=True))
            bet = int(input(f"How much would you like to bet? (Maximum Bet: {locale.currency(max_bet)}): "))
            if bet <= max_bet:
                break
            print("Invalid amount. Please enter a valid bet.\n")
        
        if dice1 == 2:
            max_bet = min(balance // 4, 500)  # Maximum bet for X4 is $500 or 25% of balance, whichever is lower.
            double_down = input("Do you want to X4 your bet on both dice being equal to or greater than 8? Yes / No ").lower() == "y"
            if double_down:
                if total >= 8:
                    bet *= 4
                    print("You Won!")
                else:
                    print("You did not meet the requirements for the X4 bet.")
        
        if dice1 == 3:
            max_bet = min(balance // 3, 500)  # Maximum bet for X3 is $500 or 33.3% of balance, whichever is lower.
            triple_down = input("Do you want to X3 your bet on both dice being equal to or greater than 8? Yes / No ").lower() == "y"
            if triple_down:
                if total >= 8:
                    bet *= 3
                    print("You Won!")
                else:
                    print("You did not meet the requirements for the X3 bet.")
                    continue  # Skip to the next iteration of the loop
            
        if dice1 == 6 and dice2 == 6 and total == 12:
            print("\nDiamond Dice, you got X10 your bet.")
            bet *= 10
        
        plus_bal = balance + bet
        minus_bal = balance - bet
        
        if balance > 0:
            print("\nDice 1:", dice1)
            print("Dice 2:", dice2)
            print("Total:", total)

            # Checks if the total is equal to or above the winning threshold.
            if total >= 8 and not (dice1 == 2 and total >= 8):
                balance = plus_bal
                print("\nYou Won!")
                print("New Balance:", locale.currency(balance, grouping=True))
            else:
                balance = minus_bal
                print("\nYou Lost.")
                print("New Balance:", locale.currency(balance, grouping=True))
            
            play_again = input("\nPlay again: Yes / No ").lower() == "y"
            if not play_again:
                break
        else:
            print("You do not have enough money to play.")
            break

roll_dice()
