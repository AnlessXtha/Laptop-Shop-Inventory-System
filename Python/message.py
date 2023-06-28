
def welcome():
    print("------------------------------------------------------------------------------------------------------------")
    print("\t\t\t\t\t\t Welcome Admin! I hope you have a good day ahead!!!")
    print("------------------------------------------------------------------------------------------------------------")

def main_options():
    ''' Function that displays the options for the user to select their desire choices in the system '''

    print("\nOur Options:")
    print("\n1) To Sale Products")
    print("2) To Order Products")
    print("3) Exit\n")

def table_of_laptops():
    # read_file()
    print("--------------------------------------------------------------------------------------------------------------")
    print("S.N.     Laptop Name             Brand           Price          Quantity         Processor             GPU")
    print("--------------------------------------------------------------------------------------------------------------")

    s_n = 1
    with open("Laptops.txt", "r") as df:
        for line in df:
            print(s_n, "\t\t", line.replace(",","\t\t\t"))
            s_n += 1

    print("--------------------------------------------------------------------------------------------------------------")

# def table_of_