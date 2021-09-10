def import_and_create_dictionary(filename):
    """This function is used to create an expense dictionary from a file
    Every line in the file should be in the format: key , value

    the key is a user's name and the value is an expense to update the user's total expense with. 
    the value shld be a number, however it is possible that there s no value that the value is an invalid number or that the entire line is blank

    """
    expenses = {}

    f =  open(filename, "r")
    lines = f.readlines()


    for  line in lines:
        # strip whitspaces from the beginning and the end of the line
        # split into a list append on comma seperator
        lst = line.strip().split(",")

        if len(lst) <= 1:
            continue

        key = lst[0].strip()
        value = lst[1].strip()

        try:
            # cast value to float
            value = float(value)

            # add new expenses amount to the current total expenses amount
            expenses[key] = expenses.get(key, 0 ) + value

        except:
            # otherwise go t top of for loop , to the next line in ist of lines
            continue
    

    f.close()

    return expenses


def main():
    expenses = import_and_create_dictionary('file.txt')
    print('expenses: ', expenses)


if __name__ == '__main__':
    main()
