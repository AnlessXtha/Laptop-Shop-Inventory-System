# importing functions to generate bills with date, time and order number
import datetime
import string, random


def update_file(laptop_d, confirm):
    """
    This function is used to update the list of laptops in text file for both selling and ordering.
    @return: laptop_d(dictionary)
    """
    if confirm == True:
        with open("Laptops.txt", "w") as file:
            for value in laptop_d.values():
                a_line = ','.join(value[0])
                file.write(a_line)
                file.write('\n')


def generate_receipt(client_name, phone_no, address, finalized_laptops):
    """
    Function to display a receipt that contains all the details of the customer as well as
    the purchased laptops and tax, total price and the total price with tax.
    :param: client_name, phone_no, address, finalized_laptops
    """

    # Date and Time : Provides the time and date when a transaction takes place
    now = datetime.datetime.now()
    date = now.strftime("Date of Purchase:- %Y/%m/%d")
    time = now.strftime("Time of Purchase:- %H:%M")

    # Order number : Generate a unique order number for each transaction
    num = 7
    order_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=num))

    print("\n")
    print("\t\t This final receipt will be saved and printed.")
    print("-------------------------------------------------------------------------")
    print("                         DynasTech  Laptop  Shop                         ")
    print("                          Putalisadak, Kathmandu                         ")
    print("-------------------------------------------------------------------------")
    print("Order No.", str(order_number))
    print(date)
    print(time)
    print("-------------------------------------------------------------------------")
    print("Customer Name:-", str(client_name))
    print("Customer Phone No:-", str(phone_no))
    print("Customer Address:-", str(address))
    print("-------------------------------------------------------------------------")
    print("S.N.     Laptop Name           Quantity           Price           Amount")
    print("-------------------------------------------------------------------------")

    # Total Amount : This gives total amount of the finalized laptops
    s_n = 1
    total_amount = 0
    for line in finalized_laptops:
        print(s_n, "\t", line[0], "\t", line[1], "\t\t", line[2], "\t", line[3], "\t\t")
        s_n += 1
        total_int = int(line[3].replace('$', ''))
        total_amount += total_int
        total_amount_str = ' $' + str(total_amount)

    print("-------------------------------------------------------------------------")
    print("                                              Total Amount:     ", total_amount_str)
    print("-------------------------------------------------------------------------")

    # VAT and Shipping cost: This portion adds the tax and shipping cost of the purchased goods
    vat = round(total_amount * .13, 2)
    ship = 25
    grand_total = round(total_amount + vat + ship, 2)

    vat_str = '$' + str(vat)
    ship_str = '$' + str(ship)
    grand_total_str = '$' + str(grand_total)

    print("                                                 VAT (13%):    ", vat_str)
    print("                                             Shipping Cost:        ", ship_str)
    print("-------------------------------------------------------------------------")
    print("                                               Grand Total:    ", grand_total_str)
    print("-------------------------------------------------------------------------")
    print("                  Thank you for purchasing from our shop                 ")
    print("\n")

    store_receipt(date, time, order_number, client_name, phone_no, address, finalized_laptops, total_amount_str,
                  vat_str, ship_str, grand_total_str)


def store_receipt(date, time, order_number, client_name, phone_no, address, finalized_laptops, total_amount_str,
                  vat_str, ship_str, grand_total_str):
    """
    This function is used to create a new text file saving the bill while selling.
    :param: date, time, order_number, client_name, phone_no, address, finalized_laptops,
            total_amount_str, vat_str, ship_str, grand_total_str
    """

    with open(f"{client_name}{phone_no}.txt", 'w') as receipt:
        receipt.write("\n")
        receipt.write("               This final receipt will be saved and printed.\n")
        receipt.write("-------------------------------------------------------------------------\n")
        receipt.write("                          DynasTech Laptop Shop                          \n")
        receipt.write("                          Putalisadak, Kathmandu                         \n")
        receipt.write("-------------------------------------------------------------------------\n")
        receipt.write("Order No. " + str(order_number) + "\n")
        receipt.write(date + "\n")
        receipt.write(time + "\n")
        receipt.write("-------------------------------------------------------------------------\n")
        receipt.write("Customer Name:- " + str(client_name) + "\n")
        receipt.write("Customer Phone No:- " + str(phone_no) + "\n")
        receipt.write("Customer Address:- " + str(address) + "\n")
        receipt.write("-------------------------------------------------------------------------\n")
        receipt.write("S.N.     Laptop Name              Quantity        Price           Amount\n")
        receipt.write("-------------------------------------------------------------------------\n")

        # Total Amount : This gives total amount of the finalized laptops
        s_n = 1
        for line in finalized_laptops:
            receipt.write(f"{s_n}         {line[0]}         {line[1]}              {line[2]}          {line[3]} \n")
            s_n += 1

        receipt.write("-------------------------------------------------------------------------\n")
        receipt.write("                                              Total Amount:      " + total_amount_str + "\n")
        receipt.write("-------------------------------------------------------------------------\n")
        receipt.write("                                                 VAT (13%):     " + vat_str + "\n")
        receipt.write("                                             Shipping Cost:         " + ship_str + "\n")
        receipt.write("-------------------------------------------------------------------------\n")
        receipt.write("                                               Grand Total:     " + grand_total_str + "\n")
        receipt.write("-------------------------------------------------------------------------\n")
        receipt.write("                  Thank you for purchasing from our shop                 ")


def generate_order_receipt(supplier_name, finalized_laptops):
    """
    Function to display a receipt that contains all the details of the supplier as well as
    the ordered laptops and tax, total price and the total price with tax.
    :param: supplier_name, finalized_laptops
    """

    # Date and Time : Provides the time and date when a transaction takes place
    now = datetime.datetime.now()
    date = now.strftime("Date of Purchase:- %Y/%m/%d")
    time = now.strftime("Time of Purchase:- %H:%M")

    # Order number : Generate a unique order number for each transaction
    num = 7
    order_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=num))

    print("\n")
    print("                       This final receipt will be saved and printed.                  ")
    print("--------------------------------------------------------------------------------------")
    print("                               DynasTech  Laptop  Shop                                ")
    print("                                Putalisadak, Kathmandu                                ")
    print("--------------------------------------------------------------------------------------")
    print("Bill to:-", str(supplier_name))
    print("--------------------------------------------------------------------------------------")
    print("Order No.", str(order_number))
    print(date)
    print(time)
    print("--------------------------------------------------------------------------------------")
    print("S.N.     Laptop Name              Brand        Quantity           Price       Amount")
    print("--------------------------------------------------------------------------------------")

    s_n = 1
    total_amount = 0
    for line in finalized_laptops:
        print(s_n, "\t", line[0], "\t", line[1], "\t", line[2], "\t\t", line[3], "    ", line[4])
        s_n += 1
        total_int = int(line[4].replace('$', ''))
        total_amount += total_int
        total_amount_str = ' $' + str(total_amount)

    print("--------------------------------------------------------------------------------------")
    print("                                                          Total Amount:     ", total_amount_str)
    print("--------------------------------------------------------------------------------------")

    # VAT and Shipping cost: This portion adds the tax and shipping cost of the purchased goods
    vat = round(total_amount * .13, 2)
    total_amount_vat = round(total_amount + vat, 2)
    supplier_discount = round(total_amount * .10, 2)
    grand_total = round(total_amount + vat - supplier_discount, 2)

    vat_str = '$' + str(vat)
    total_amount_vat_str = '$' + str(total_amount_vat)
    supplier_discount_str = '$' + str(supplier_discount)
    grand_total_str = '$' + str(grand_total)

    print("                                                            VAT (13%):    ", vat_str)
    print("                                          Total Amount with VAT (13%):    ", total_amount_vat_str)
    print("--------------------------------------------------------------------------------------")
    print("                                                             Discount:     ", supplier_discount_str)
    print("--------------------------------------------------------------------------------------")
    print("                                                          Grand Total:    ", grand_total_str)
    print("--------------------------------------------------------------------------------------")
    print("                          Pleasure doing business with you.                            ")
    print("\n")

    store_order_receipt(date, time, order_number, supplier_name, finalized_laptops, vat_str, total_amount_vat_str,
                        supplier_discount_str, grand_total_str)


def store_order_receipt(date, time, order_number, supplier_name, finalized_laptops, vat_str, total_amount_vat_str,
                        supplier_discount_str, grand_total_str):
    """
    This function is used to create a new text file saving the bill while ordering.
    :param: date, time, order_number, supplier_name, finalized_laptops, vat_str,
            total_amount_vat_str, supplier_discount_str, grand_total_str
    """

    with open(f"{supplier_name}_no.{order_number}.txt", "w") as order_receipt:
        order_receipt.write("\n")
        order_receipt.write("                       This final receipt will be saved and printed.                  \n")
        order_receipt.write("--------------------------------------------------------------------------------------\n")
        order_receipt.write("                               DynasTech  Laptop  Shop                                \n")
        order_receipt.write("                                Putalisadak, Kathmandu                                \n")
        order_receipt.write("--------------------------------------------------------------------------------------\n")
        order_receipt.write("Bill to:- " + str(supplier_name) + "\n")
        order_receipt.write("--------------------------------------------------------------------------------------\n")
        order_receipt.write("Order No. " + str(order_number) + "\n")
        order_receipt.write(date + "\n")
        order_receipt.write(time + "\n")
        order_receipt.write("--------------------------------------------------------------------------------------\n")
        order_receipt.write("S.N.     Laptop Name              Brand        Quantity       Price           Amount  \n")
        order_receipt.write("--------------------------------------------------------------------------------------\n")

        s_n = 1
        for line in finalized_laptops:
            order_receipt.write(
                f"{s_n}         {line[0]}         {line[1]}      {line[2]}             {line[3]}          {line[4]}  \n")
            s_n += 1

        order_receipt.write("--------------------------------------------------------------------------------------\n")
        order_receipt.write(
            "                                                            VAT (13%):    " + vat_str + "\n")
        order_receipt.write(
            "                                          Total Amount with VAT (13%):    " + total_amount_vat_str + "\n")
        order_receipt.write("--------------------------------------------------------------------------------------\n")
        order_receipt.write(
            "                                                             Discount:     " + supplier_discount_str + "\n")
        order_receipt.write("--------------------------------------------------------------------------------------\n")
        order_receipt.write(
            "                                                          Grand Total:    " + grand_total_str + "\n")
        order_receipt.write("--------------------------------------------------------------------------------------\n")
        order_receipt.write("                           Pleasure doing business with you.                            ")
        order_receipt.write("\n")
