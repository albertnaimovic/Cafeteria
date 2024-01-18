#  Create a user interface (UI) using the console module to facilitate user interaction with the reservation system.

#     Allow users to perform the following actions:

# a. View the restaurant's details and menu.
# b. Browse available tables and make reservations.
# c. View their existing reservations and cancel them if necessary.
# d. Manage their reservation details, such as adding or removing guests.
import os, time, database_moves as db


def main_menu() -> None:
    os.system("cls")
    print(f"\n\n")
    print(
        """   _____          ______ ______ _______ ______ _____  _____          
  / ____|   /\   |  ____|  ____|__   __|  ____|  __ \|_   _|   /\    
 | |       /  \  | |__  | |__     | |  | |__  | |__) | | |    /  \   
 | |      / /\ \ |  __| |  __|    | |  |  __| |  _  /  | |   / /\ \  
 | |____ / ____ \| |    | |____   | |  | |____| | \ \ _| |_ / ____ \ 
  \_____/_/    \_\_|    |______|  |_|  |______|_|  \_\_____/_/    \_\  .
                                                                     
                                                                     """
    )
    time.sleep(1)
    while True:
        os.system("cls")
        print("\n----------------\n|--Caffeteria--|\n----------------")
        category: str = input(
            "--Menu--\n1. View the restaurant's details and menu\n2. Make reservation\n3. View existing reservations\n4. Manage reservation details\n5. Exit\n\nEnter number of selection: "
        )
        if category.isnumeric() == True:
            if category == "1":
                db.get_food_menu()
            elif category == "2":
                pass
            elif category == "3":
                pass
            elif category == "4":
                pass
            elif category == "5":
                print("\nBye.")
                break
            else:
                print("\nThere is no such selection")
                time.sleep(1.5)
        else:
            print(
                "\nPlease enter number from list provided without any symbols and spaces."
            )
            time.sleep(2)


main_menu()
