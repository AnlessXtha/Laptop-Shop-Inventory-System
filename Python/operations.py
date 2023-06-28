# importing all the necessary function to run the program
from write import *


def welcome():
    """ Function that displays that greets the admin """

    print(
        "------------------------------------------------------------------------------------------------------------")
    print("\t\t\t\t Welcome Admin! I hope you have a good day ahead!!!")
    print(
        "------------------------------------------------------------------------------------------------------------")


def main_options():
    """ Function that displays the options for the user to select their desire choices in the system """

    print("\nOur Options:")
    print("\n1) To Sale Products")
    print("2) To Order Products")
    print("3) Exit\n")


def to_continue():
    """ Function that displays a message instructing the user to press any key to continue"""
    input("Press any key to continue...")


def main_exit():
    """ Function that displays a message when the user has exited from the system"""

    print("\nThanks you for using our system.\n")


def user_option():
    """ Function to get the choice from the user
    @return : option
    """

    try:
        option = int(input("Please enter you desired option with their corresponding number: "))
        if option in [1, 2, 3, 4]:
            return option
        else:
            print("\nThe option you have entered is invalid.Please, enter a valid option.\n")
    except:
        print("\nThe option you have entered is a character not a number.Please, enter a valid option.")


def sale_laptop(laptop_d):
    """ Function is used for gather input from the user to sell a laptop to a customer.
    This function also check for any errors in the entered value and holds the new value to be updated in txt file.
    It also calls other functions according to the action of the user.
    :param: laptop_d
    """

    print("\n")

    while True:
        client_name = input("Enter the name of the customer: ")
        if client_name.isalpha():  # checks if the entered value are letters and not numbers
            break
        else:
            print("\nThe name of the client should only contain letters.")

    while True:
        phone_no = input("Enter the Phone number of the customer:")
        if phone_no.isdigit():  # checks if the entered value are numbers and not letters
            break
        else:
            print("\nPhone number should be numeric.")

    address = input("Enter the Address of the customer:")

    more_loop = True

    temp_l = []  # This list is used to temporarily hold the new values to be updated

    while more_loop:
        '''
        This loop asks whether to sale more laptop or not
        if yes:
            the serial number and the quantity is asked and will be looped
        if no:
            it views the receipt of the purchased item
        '''

        no_quantity_loop = True
        while no_quantity_loop:

            validate = 1
            laptop_number = id_validation(laptop_d, validate)

            temp_l, no_quantity_loop = limit_check(laptop_d, laptop_number, temp_l, no_quantity_loop)

        print("\n")

        more_loop = add_more_items(more_loop)

    confirmation_bill(temp_l)

    if confirmation():
        update_file(laptop_d, True)
        generate_receipt(client_name, phone_no, address, temp_l)


def confirmation_bill(selected_laptops):
    """
    Function to display the selected laptops for selling with their name, quantity, price and total price.
    :param: selected_laptops
    """

    print("\n")
    print("You have selected these Laptops.")
    print("-------------------------------------------------------------------------")
    print("S.N.     Laptop Name              Quantity        Price           Amount")
    print("-------------------------------------------------------------------------")

    s_n = 1
    total_amount = 0
    for line in selected_laptops:
        print(s_n, "\t", line[0], "\t    ", line[1], "\t", line[2], "\t", line[3], "\t\t")
        s_n += 1
        total_int = int(line[3].replace('$', ''))
        total_amount += total_int
        total_amount_str = ' $' + str(total_amount)

    print("-------------------------------------------------------------------------")
    print("                                              Total Amount:     ", total_amount_str)
    print("-------------------------------------------------------------------------")
    print("\n")


def confirmation():
    """ Function to ask the user for their confirmation to move on to transaction and generate receipt."""

    conf_loop = True
    while conf_loop:
        confirm = input("Do you want to confirm this transaction(yes/no): ")
        if confirm.lower() == 'yes':
            return True
        elif confirm.lower() == 'no':
            conf_loop = False
        else:
            print("\nEither enter (yes) or (no).")


def order_laptops(laptop_d):
    """
    Function is used for gather input from the user to order laptops from supplier.
    This function also check for any errors in the entered value and holds the new value
    to be updated in txt file.
    It also calls other functions according to the action of the user.
    :param: laptop_d
    """

    print("\n")

    while True:
        supplier_name = input("Enter the name of the supplier: ")
        if supplier_name.isalpha():
            break
        else:
            print("\nThe name of the supplier should only contain letters.")

    more_loop = True

    temp_l = []     # This list is used to temporarily hold the new values to be updated

    while more_loop:
        '''
        This loop asks whether to order more laptop or not
        if yes:
            the serial number and the quantity is asked and will be looped
        if no:
            it views the receipt of the purchased item
        '''

        max_quantity_loop = True
        while max_quantity_loop:

            validate = 2
            laptop_number = id_validation(laptop_d, validate)

            temp_l, max_quantity_loop = amount_check(laptop_d, laptop_number, temp_l, max_quantity_loop)

        print("\n")

        more_loop = add_more_items(more_loop)

    if more_loop == False:
        confirmation_order_bill(temp_l)

        if confirmation():
            update_file(laptop_d, True)
            generate_order_receipt(supplier_name, temp_l)


def confirmation_order_bill(selected_laptops):
    """
    Function to display the selected laptops for ordering with their Laptop name, Brand Name,
    quantity, price and total price.
    :param: selected_laptops
    """
    print("\n")
    print("You have selected these Laptops.")
    print("--------------------------------------------------------------------------------------")
    print("S.N.     Laptop Name              Brand        Quantity       Price           Amount")
    print("--------------------------------------------------------------------------------------")

    s_n = 1
    total_amount = 0
    for line in selected_laptops:
        print(s_n, "\t", line[0], "\t", line[1], "\t", line[2], "\t    ", line[3], "\t    ", line[4])
        s_n += 1
        total_int = int(line[4].replace('$', ''))
        total_amount += total_int
        total_amount_str = ' $' + str(total_amount)

    print("--------------------------------------------------------------------------------------")
    print("                                                          Total Amount:     ", total_amount_str)
    print("--------------------------------------------------------------------------------------")
    print("\n")


def id_validation(laptop_d, validate):
    """
    This function is used to check whether the value of serial number is valid or not.
    It also uses Exception handling to get the proper value of laptop_number and avoid the
    termination of the program.
    :param: laptop_d
    @return : laptop_number
    """
    print("\n")

    serial_loop = True
    while serial_loop:
        '''
        This loop is used to check if the entered serial number is valid or not, the loop repeats when the
        required input is not given.
        '''
        try:
            if validate == 1:
                laptop_number = int(
                    input("Enter the serial number of the laptop that the customer wants to purchase: "))
            elif validate == 2:
                laptop_number = int(
                    input("Enter the serial number of the laptop that the shop wants to order: "))
            while serial_loop:
                if laptop_number > len(laptop_d) or laptop_number <= 0:
                    print("\nYou have enter an invalid serial number.")
                    laptop_number = int(input("Enter the serial number give in the table above: "))
                else:
                    serial_loop = False
        except:
            print("\nThe option you have entered is a character not a number.Please, enter a valid option.\n")

    return laptop_number


def limit_check(laptop_d, laptop_number, temp_l, no_quantity_loop):
    """
    This function is used to check the value of quantity is valid or not while selling.
    It also uses Exception handling to get the proper value of laptop_quantity and avoid the
    termination of the program.
    :param: laptop_d, laptop_number, temp_l, no_quantity_loop
    @return: temp_l(list), no_quantity_loop(boolean)
    """
    limit_loop = True

    while limit_loop:
        '''
        This loop is used to check whether the quantity of the required laptop matching the quantity
        available in the laptop shop
        '''
        try:
            laptop_quantity = int(input("\nEnter the quantity that the customer wants to purchase: "))
            while limit_loop:
                for key, value in laptop_d.items():
                    if key == laptop_number:
                        if int(value[0][3]) >= laptop_quantity > 0:
                            new_quantity = int(value[0][3]) - laptop_quantity
                            value[0][3] = " " + str(new_quantity)

                            # Storing the selected laptops in a 2D list
                            laptop_name = value[0][0]
                            sel_laptop_quantity = ' ' + str(laptop_quantity)
                            laptop_price = value[0][2]
                            total_laptop_price_int = int(laptop_price.replace('$', '')) * laptop_quantity
                            total_laptop_price = ' $' + str(total_laptop_price_int)

                            temp_l.append([laptop_name, sel_laptop_quantity, laptop_price, total_laptop_price])

                            limit_loop = False
                            no_quantity_loop = False

                        elif int(value[0][3]) == 0:
                            print("We do not have any stock of this laptop. Please pick something else.")
                            limit_loop = False
                        else:
                            print("\nYou have exceeded the quantity of this laptop.")
                            laptop_quantity = int(input("Enter the quantity that the customer wants to purchase: "))
        except:
            print("\nThe option you have entered is a character not a number.Please, enter a valid option.")

    return temp_l, no_quantity_loop


def amount_check(laptop_d, laptop_number, temp_l, max_quantity_loop):
    """
    This function is used to check the value of quantity is valid or not while ordering.
    It also uses Exception handling to get the proper value of laptop_quantity and avoid the
    termination of the program.
    :param: laptop_d, laptop_number, temp_l, max_quantity_loop
    @return: temp_l(list), max_quantity_loop(boolean)
    """

    amount_loop = True

    while amount_loop:
        '''This loop is used to check whether the quantity of the required laptop is needed to be ordered or not.
        i.e. Total quantity of each type of laptop must not exceed 50.
        '''

        try:
            laptop_quantity = int(input("Enter the quantity that you want to order: "))
            for key, value in laptop_d.items():
                if key == laptop_number:
                    if laptop_quantity > 0 and int(value[0][3]) + laptop_quantity <= 50:
                        # checks if the entered quantity is greater than 0 and total quantity of the laptops is less than 50 or not.
                        new_quantity = int(value[0][3]) + laptop_quantity
                        value[0][3] = " " + str(new_quantity)

                        # Storing the selected laptops in a 2D list
                        laptop_name = value[0][0]
                        laptop_brand = value[0][1]
                        sel_laptop_quantity = ' ' + str(laptop_quantity)
                        laptop_price = value[0][2]
                        total_laptop_price_int = int(laptop_price.replace('$', '')) * laptop_quantity
                        total_laptop_price = ' $' + str(total_laptop_price_int)

                        temp_l.append(
                            [laptop_name, laptop_brand, sel_laptop_quantity, laptop_price, total_laptop_price])

                        amount_loop = False
                        max_quantity_loop = False

                    elif int(value[0][3]) == 50:
                        print(
                            "We already have the max capacity of this laptop which is 50. Please order another laptop. ")
                        amount_loop = False

                    else:
                        print("\nYou have exceeded the quantity of this laptop that can be stored in our shop.")
        except:
            print("\nYour entered value is a character not a number.Please, enter a valid number.")

    return temp_l, max_quantity_loop


def add_more_items(more_loop):
    """
    This function is used to check whether the user wants to add more items or move on to
    transaction.
    :param: more_loop
    @return: more_loop(boolean)
    """

    continue_loop = True
    while continue_loop:
        '''
        This loop is used to check whether the user has entered one of the correct option
        '''

        add_more = input("Do you want to purchase anymore products(yes/no): ")

        if add_more.lower() == 'yes':
            continue_loop = False

        elif add_more.lower() == 'no':
            more_loop = False
            continue_loop = False

        else:
            print("\nEither enter (yes) or (no).")

    return more_loop
