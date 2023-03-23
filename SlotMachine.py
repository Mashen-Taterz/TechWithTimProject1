import random #Random number genrator

#Main parameters
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

#Dictionary of symbols for the rows and columns of slot machine.
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
#Dictionary of the value of each symbol 
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0 #Initial value 
    winning_lines = [] #Initial empty list, will tell what lines matched.
    for line in range(lines): #Check only lines being bet on (0,1,2) AKA lines 1, 2, 3
        symbol = columns[0][line]#Check first symbol in each row then compare to the rest of the line
        for column in columns: #Loop through all columns
            symbol_to_check = column[line] # Check symbols in rows
            if symbol != symbol_to_check: # Check if symbols do not match
                break #if symbol does not match 
        else:
            winnings += values[symbol] * bet #Take the valueof the symbol times the bet.
            winning_lines.append(lines + 1)#Add 1 to check line number instead of index 0 for example.
    return winnings, winning_lines


#Loop through dict. symbol will be A, symbol count will be 2 then loop through symbol count and add A twice to all_symbols list. Continue to next symbol...
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = [] # [[], [], []]
    for _ in range (cols): #Generate a column for every column we have 3 times.
        column = [] #Picking a random value for each row/spot in column.
        current_symbols = all_symbols [:] #Create a copy of the list all_symbols.
        for _ in range(rows): #Loop through values we need to generate for each rows we have on slot machine.
            value = random.choice(current_symbols) #Pick a random value from the list.
            current_symbols.remove(value) #Remove symbol from coppied list so we don't pick it again.
            column.append(value) #Add the value to column.
        columns.append(column) #Add column to columns list
    return columns

def print_slot_machine(columns): #This function will transpose / flip the columns from horizontal to vertical and print them. 
    for row in range(len(columns[0])): #Loop through every single row.
        for i, column in enumerate(columns): #For every row we loop through every column. enumerate will check the index aswell as the item.
            if i != len(columns) - 1: #if i is not equal to len of columns print " | " 
                print(column[row], end = " | ") #End the line or row with Graphical " | " to sepparate columns visually.
            else:
                print(column[row], end = "") #For every column we only print current row we are on. row 0, row 1, row 2 
        print() #Empty print statement will bring us down to the next line. 

#User funds.
def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount

#User picks number of lines to place bets on. 
def get_number_of_lines():
    while True:
        lines = input("Enter number of lines to bet on. (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines

#Get bet amount from user funds.
def get_bet():
    while True:
        amount = input("How much would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is ${balance}.")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}.")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won {winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet #How much you won or lost from current round

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}.")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

        print(f"You left with ${balance}.")

main()