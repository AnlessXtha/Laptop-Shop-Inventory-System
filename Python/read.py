def read_file():
    """
    This function is used to read the list of laptops from text file.
    @return: laptop_d(dictionary)
    """
    laptop_d = {}
    laptop_id = 1
    with open('Laptops.txt','r') as rf:
        for line in rf:
            line_list = []
            line = line.replace("\n", "")
            line_list.append(line.split(","))
            laptop_d.update({laptop_id: line_list})
            laptop_id = laptop_id + 1
    return laptop_d


def table_of_laptops():
    """ Function that displays the table with all the available laptops in the shop """

    print(
        "----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print(
        " S.N.    Laptop Name             Brand                   Price        Quantity               Processor             GPU                   RAM             Storage")
    print(
        "----------------------------------------------------------------------------------------------------------------------------------------------------------------------")

    s_n = 1
    with open("Laptops.txt", "r") as df:
        for line in df:
            print(" ", s_n, "\t", line.replace(",", "\t\t"))
            s_n += 1

    print(
        "----------------------------------------------------------------------------------------------------------------------------------------------------------------------")

