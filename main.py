# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules
# ChangeLog (Who,When,What):
# RRoot,1.1.2020,Created started script
# RRoot,1.1.2020,Added pseudo-code to start assignment 9
# HyojinK,12.8.2020,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #
# TODO: Import Modules
if __name__ == "__main__":
    from dataclasses import Employee as Emp
    from processing import FileProcessor as Fp
    from questions import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")


# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of employee objects when script starts

lstTable= []
lstFileData = Fp.read_data_from_file("EmployeeData.txt")
lstTable.clear()
for line in lstFileData:
    lstTable.append(Emp(line[0], line[1], line[2].strip()))
for row in lstTable:
    print(row.to_string(), type(row))

while(True):
# Show user a menu of options
    Eio.print_menu_items()

# Get user's input menu option choice
    strchoice= Eio.input_menu_options()

# Show user current data in the list of employee objects
    if strchoice == '1':
        Eio.print_current_list_items(lstTable)
# Let user add data to the list of employee objects
    try:
        if strchoice== '2':
            emp= Eio.input_employee_data()
            lstTable.append(emp)
    except Exception as e:
        print(e, ' data was not added to the list ')
# let user save current data to file
    try:
        if strchoice== '3':
            Fp.save_data_to_file('EmployeeData.txt', lstTable)
            print('saved')
    except Exception as e:
        print(e, ' data was not saved to the text file ')
#exit
    if strchoice== '4':
        Eio.exit_program()
        break

# Main Body of Script  ---------------------------------------------------- #
