import os
import sys


def display_title():
    script_dir = os.path.dirname(__file__)
    title_path = os.path.join(script_dir, 'title.txt')
    with open(title_path, 'r') as f:
        sys.stdout.write(f.read())
        sys.stdout.flush()


def display_credit():
    script_dir = os.path.dirname(__file__)
    credit_path = os.path.join(script_dir, 'credit.txt')
    with open(credit_path, 'r') as f:
        sys.stdout.write(f.read())
        sys.stdout.flush()


def main_menu():
    print("\033[1;36mCOMMANDS:\033[0m")
    print("\033[1;32m|advance|\033[0m - \033[1;37mAdvance in time within the simulation\033[0m")
    print("\033[1;32m|check package|\033[0m - \033[1;37mCheck the status of a specific package\033[0m")
    print("\033[1;32m|truck update|\033[0m - \033[1;37mView details for a specific truck\033[0m")
    print("\033[1;32m|exit|\033[0m - \033[1;37mTerminate the simulation\033[0m")
