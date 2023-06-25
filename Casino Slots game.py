import random

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1
COLS = 3
ROWS = 3

sybmol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

sybmol_values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def main():
    balance = deposit()
    while True:
        print(f"Your balance is ${balance}.")
        q = input("Press any key to play, '0' to quit : ")
        if q == '0':
            break
        wl = game(balance)
        balance += wl


def game(balance):
    lines = get_lines()

    while True:
        bet = get_bet()
        bet_amount = bet*lines
        if (bet_amount > balance):
            print(
                f"You don't have enough balance, your current balance is ${balance}")
        else:
            break

    print(
        f"you are betting ${bet} on {lines} lines total bet is ${bet_amount}.")

    printed_columns = get_spin(ROWS, COLS, sybmol_count)
    print_column(printed_columns)

    winnings, winning_lines = check_won(
        printed_columns, lines, bet, sybmol_values)
    print(f"you won {winnings}.")
    print(f"you win on lines :", *winning_lines)
    return winnings - bet_amount


def deposit():
    while True:
        amount = input("Enter the deposit amount : $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please enter amount greater than 0.")
        else:
            print("Please enter a valid number.")
    return amount


def get_lines():
    while True:
        lines = input(
            "Enter the number of lines to bet on (1-" + str(MAX_LINES) + ") ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter number between 1 and " + str(MAX_LINES) + ".")
        else:
            print("Please enter a valid number.")
    return lines


def get_bet():
    while True:
        amount = input("Enter the bet on each line: ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(
                    f"Please enter a bet between ${MIN_BET} and ${MAX_BET}. ")
        else:
            print("Please enter a valid bet amount.")
    return amount


def get_spin(rows, cols, symbols):

    all_symbols = []
    for symbol, symbols_count in symbols.items():
        for _ in range(symbols_count):
            all_symbols.append(symbol)

    columns = []

    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns


def print_column(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


def check_won(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol_to_check = columns[0][line]
        for column in columns:
            symbol = column[line]
            if symbol_to_check != symbol:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


main()
