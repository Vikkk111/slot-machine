import random 

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 10

ROWS = 3
COLM = 3

symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbol.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in  range(len(columns[0])):
        for  i, column in enumerate(columns):
            if i != len(column) - 1:
                print(column[row], "|")
            else:
                print(column[row])


def deposit():
    while True:
        amount = input("What would you like to deposit? £")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount should be greater than 0.")
        else:
            print("Please enter a number.")
            
    return amount

def get_number_lines():
    while True:
        lines = int(input("How many lines? (1 - 3)"))
        if lines:
            amount = int(lines)
            if 1 <= lines <= 3:
                break
            else:
                print("Enter the valid number.")
        else:
            print("Please enter a number.")
            
    return lines 

def get_bet():
    while True:
        amount = input("What would you like to bet? £")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount should be between ${MIN_BET} - {MAX_BET}.")
        else:
            print("Please enter a number.")
            
    return amount
    

def main():
    balance = deposit()
    lines = get_number_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines 
        if total_bet > balance:
            print(f"You do not have enough money on your balance, your current balance is ${balance}")
        else:
            break
        
    
    print(
        f"Tou are betting ${bet} on {lines} lines.Total bet is ${total_bet}")
    
    slots = get_slot_machine_spin(ROWS, COLM, symbol_count)
    
    
main()