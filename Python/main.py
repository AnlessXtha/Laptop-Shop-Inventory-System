# importing all the necessary function to run the program
from operations import *
from read import *

go = True  # makes the program loop until the user wants to exit

welcome()

while go:
    main_options()
    user_entered = user_option()

    # This option is used for selling laptops.
    if user_entered == 1:

        table_of_laptops()

        laptop_dictionary = read_file()
        sale_laptop(laptop_dictionary)

        to_continue()

    # This option is used for ordering laptops.
    elif user_entered == 2:
        table_of_laptops()

        laptop_dictionary = read_file()
        order_laptops(laptop_dictionary)

        to_continue()

    # This option is used exiting the system.
    elif user_entered == 3:
        main_exit()
        break
