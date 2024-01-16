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
    print("\033[1;32m|check package|\033[0m - \033[1;37mView package details\033[0m")
    print("\033[1;32m|check truck|\033[0m - \033[1;37mView truck details\033[0m")
    print("\033[1;32m|check deliveries|\033[0m - \033[1;37mView completed deliveries\033[0m")
    print("\033[1;31m|exit|\033[0m - \033[1;37mExit the application\033[0m")


def check_truck():
    print("\033[1;36mCOMMANDS:\033[0m")
    print("\033[1;32m|check total mileage|\033[0m - \033[1;37mView truck mileages\033[0m")
    print("\033[1;32m|check location|\033[0m - \033[1;37mView truck location at a specific time\033[0m")
    print("\033[1;31m|exit|\033[0m - \033[1;37mExit the application\033[0m")


def check_total_mileage():
    print("\033[1;36mCOMMANDS:\033[0m")
    print("\033[1;32m|select truck|\033[0m - \033[1;37mSelect a specific truck\033[0m")
    print("\033[1;32m|total trucks mileage|\033[0m - \033[1;37mView total mileage of all trucks\033[0m")
    print("\033[1;31m|exit|\033[0m - \033[1;37mExit the application\033[0m")


def check_location():
    print("\033[1;36mCOMMANDS:\033[0m")
    print("\033[1;32m|select truck|\033[0m - \033[1;37mSelect a specific truck\033[0m")
    print("\033[1;32m|all trucks|\033[0m - \033[1;37mView location of all trucks\033[0m")
    print("\033[1;31m|exit|\033[0m - \033[1;37mExit the application\033[0m")


def check_package():
    print("\033[1;36mCOMMANDS:\033[0m")
    print("\033[1;32m|select package|\033[0m - \033[1;37mSelect a specific package by ID and designated time\033[0m")
    print("\033[1;32m|all packages|\033[0m - \033[1;37mView all packages at a designated time\033[0m")
    print("\033[1;31m|exit|\033[0m - \033[1;37mExit the application\033[0m")


def check_deliveries():
    print("\033[1;36mCOMMANDS:\033[0m")
    print("\033[1;32m|deliveries by truck|\033[0m - "
          "\033[1;37mView deliveries by specific truck and designated time\033[0m")
    print("\033[1;32m|all deliveries|\033[0m - \033[1;37mView all deliveries at a designated time\033[0m")
    print("\033[1;31m|exit|\033[0m - \033[1;37mExit the application\033[0m")
