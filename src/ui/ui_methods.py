import sys


def display_title():
    with open('src/ui/title.txt', 'r') as f:
        sys.stdout.write(f.read())
        sys.stdout.flush()


def display_credit():
    with open('src/ui/credit.txt', 'r') as f:
        sys.stdout.write(f.read())
        sys.stdout.flush()


def main_menu():
    print("\033[1;36mCOMMANDS:\033[0m")
    print("\033[1;32m|advance|\033[0m - \033[1;37mAdvance in time within the simulation\033[0m")
    print("\033[1;32m|check package|\033[0m - \033[1;37mCheck the status of a specific package\033[0m")
    print("\033[1;32m|truck update|\033[0m - \033[1;37mView details for a specific truck\033[0m")
    print("\033[1;32m|exit|\033[0m - \033[1;37mTerminate the simulation\033[0m")
