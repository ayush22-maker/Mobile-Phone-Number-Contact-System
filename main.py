# Contact book

# import modules
import time

# Ask the user for what he need i.e. He wants to add new contact or find a contact from the added one
def use():
    user = input("What do you want to do? add or find: ")
    time.sleep(2)
    print("Processing.....")
    time.sleep(2)
    print("Processing.....")
    time.sleep(2)

    if user.lower() == "add":
        name = input(f"Enter new contact name: ")
        country_code = input(f"Enter your country code: ")
        number = int(input(f"Enter the number of {name}: "))
        Call_name = input(f"Enter the Nickname for contact{name}: ")

        time.sleep(1)
        print(f"Saving your contact...")
        time.sleep(2)

        f = open(f"contacts.{Call_name.lower()}.txt", "w")
        f.write(f"Name: {name}\nCountry Code: {country_code}\nNumber: {number}")
        f.close()
        
        print(f"New Conatact named {Call_name} saved successfully")

    else:
        find = input("Enter the Nick Name of the contact you want to find: ")
        time.sleep(2)
        print("Finding your Contcat Please Wait...")
        time.sleep(2)
        time.sleep(2)
        print(f"Your comtact is succcessfully founded here is your data\n\n")
        time.sleep(1)

        f = open(f"contacts.{find.lower()}.txt", "r")
        data = f.read()
        print(data)
        f.close()

        time.sleep(5)

        user_change = input("Do you want to change the contact data? yes or no: ")

        time.sleep(2)
        print("Processing.....")
        time.sleep(2)
        print("Processing.....")
        time.sleep(2)


        if user_change.lower() == "yes":
            f = open(f"contacts.{find}.txt", "w")
            name = input(f"Enter new contact name: ")
            country_code = input(f"Enter your country code: ")
            number = int(input(f"Enter the number of {name}: "))
            time.sleep(2)
            print("Saving your changes....")
            time.sleep(4)
            f.write(f"Name: {name}\nCountry Code: {country_code}\nNumber: {number}")
            print("Your Changes have successfully changed")
            f.close()

    print("Thanks to use our program.")
    take = input("Do you want to use our program? yes or no: ")

    if take.lower() == "yes":
        time.sleep(2)
        print("Processing your input...")
        time.sleep(2)
        use()
    else:
        print("Thanks to use of a program visit again")


use()
