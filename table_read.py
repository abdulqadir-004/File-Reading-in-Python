def table_read(filename):
    try:
        #open file in read mode
        with open(filename, "r") as file:
            table_content = file.read()
            print(table_content)
    #error handling
    except FileNotFoundError:
        print("Error: File does not Exist")
    except IOError:
        print("Error Reading File")

#main block
if __name__ == "__main__":
    table_read("table.txt")