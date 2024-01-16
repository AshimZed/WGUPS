# .----------------------------------------------------------------------------------------------------------.
# |__/\\\______________/\\\_____/\\\\\\\\\\\\__/\\\________/\\\__/\\\\\\\\\\\\\_______/\\\\\\\\\\\___        |
# | _\/\\\_____________\/\\\___/\\\//////////__\/\\\_______\/\\\_\/\\\/////////\\\___/\\\/////////\\\_       |
# |  _\/\\\_____________\/\\\__/\\\_____________\/\\\_______\/\\\_\/\\\_______\/\\\__\//\\\______\///__      |
# |   _\//\\\____/\\\____/\\\__\/\\\____/\\\\\\\_\/\\\_______\/\\\_\/\\\\\\\\\\\\\/____\////\\\_________     |
# |    __\//\\\__/\\\\\__/\\\___\/\\\___\/////\\\_\/\\\_______\/\\\_\/\\\/////////_________\////\\\______    |
# |     ___\//\\\/\\\/\\\/\\\____\/\\\_______\/\\\_\/\\\_______\/\\\_\/\\\_____________________\////\\\___   |
# |      ____\//\\\\\\//\\\\\_____\/\\\_______\/\\\_\//\\\______/\\\__\/\\\______________/\\\______\//\\\__  |
# |       _____\//\\\__\//\\\______\//\\\\\\\\\\\\/___\///\\\\\\\\\/___\/\\\_____________\///\\\\\\\\\\\/___ |
# |        ______\///____\///________\////////////_______\/////////_____\///________________\///////////_____|
# '----------------------------------------------------------------------------------------------------------'
# By Alexander D. Steele ------------------------------- Student ID: 011226486 -------------- DATE: 1/14/2024
import sys
import threading
from pathlib import Path

from src.bootstrap import bootstrap
from src.services.print_package import print_package
from src.ui.load_animation import loading_animation
from src.ui.ui_methods import display_title, display_credit, main_menu, check_truck, check_package, check_total_mileage, \
    check_location, check_deliveries

if __name__ == '__main__':

    # Start Title Screen display
    display_title()
    display_credit()

    # Start the threading for the loading animation while the main algorithm starts with the program
    stop = threading.Event()
    load = threading.Thread(target=loading_animation, args=(stop,))
    load.start()

    # Run a bootstrap for the assignment data
    trucks, packages = bootstrap()

    # Grab log file for queries
    log_file = Path.cwd() / 'data/package_log.csv'

    # Stop the loading animation thread
    stop.set()
    load.join()
    print("\n")

    # Run main application loop
    while True:

        # Main Menu
        main_menu()
        command = input("Enter command: ").lower().strip()

        match command:
            case "exit":
                sys.exit()

            # Check Package Menu
            case "check package":
                check_package()
                command = input("Enter command: ").lower().strip()

                match command:
                    case "exit":
                        sys.exit()

                    case "select package":
                        package_id = input("Enter package id: ").lower().strip()
                        check_time = input("Enter time: ").lower().strip()
                        print_package(log_file, packages, check_time, package_id)

                    case "all packages":
                        check_time = input("Enter time: ").lower().strip()
                        for idx, pkg in enumerate(packages):
                            print_package(log_file, packages, check_time, str(idx + 1))

            # Check Truck Menu
            case "check truck":
                check_truck()
                command = input("Enter command: ").lower().strip()

                match command:
                    case "exit":
                        sys.exit()

                    case "check total mileage":
                        check_total_mileage()
                        command = input("Enter command: ").lower().strip()

                        match command:
                            case "exit":
                                sys.exit()

                            case "select truck":
                                truck_id = input("Enter truck id: ").lower().strip()
                                truck = trucks[(int(truck_id) - 1)]
                                print(f"Truck: {truck.truck_id} | Total Miles: {truck.current_mileage}")

                            case "total trucks mileage":
                                total_miles = 0
                                for truck in trucks:
                                    total_miles += truck.current_mileage
                                print(f"Total Miles: {total_miles}")

                    case "check location":
                        check_location()
                        command = input("Enter command: ").lower().strip()

                        match command:
                            case "exit":
                                sys.exit()

                            case "select truck":
                                truck_id = input("Enter truck id: ").lower().strip()
                                check_time = input("Enter time: ").lower().strip()
                                print("PLACEHOLDER")

                            case "all trucks":
                                check_time = input("Enter time: ").lower().strip()
                                print("PLACEHOLDER")

            # Check Deliveries Menu
            case "check deliveries":
                check_deliveries()
                command = input("Enter command: ").lower().strip()

                match command:
                    case "exit":
                        sys.exit()

                    case "deliveries by truck":
                        truck_id = input("Enter truck id: ").lower().strip()
                        check_time = input("Enter time: ").lower().strip()
                        print("PLACEHOLDER")

                    case "all deliveries":
                        check_time = input("Enter time: ").lower().strip()
                        print("PLACEHOLDER")
