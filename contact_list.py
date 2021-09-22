from class_contact import Contact

SHOW_ALL_DATA = 1
UPDATE_DATA = 2

def show_menu():
    while True:
        try:
            option = int(input("""
            Choose one of the following options:
            1. Show all information
            2. Update data
            3. Check tag
            
            => Your choice: """))

            if 1 <= option <= 4:
                return option
                break
            else:
                print("\nInvalid Value. Try Again!!!\n")
        except ValueError:
            print("\nInvalid Value. Try Again!!!\n")

def check_tag(tag, list_tag):
    if tag in list_tag:
        return True
    else:
        return False

def choose_info_update():
    list_info = ["name", "phones", "emails", "address", "note", "tags"]
    print("Choose one of the following options to revise:")
    for i in range(len(list_info)):
        print(f"{i+1:3}: {list_info[i]}")
    while True:
        try:
            option = int(input("=> Your choice: "))
            if 1 <= option <= len(list_info):
                return list_info[option-1]
                break
            else:
                print("\nInvalid Value. Try Again!!!\n")
        except ValueError:
            print("\nInvalid Value. Try Again!!!\n")

def try_again(text):
    answer = input(text).upper()
    if answer == "Y" or answer == "YES":
        return True
    else:
        return False

if __name__ == '__main__':
    person = Contact("Pham The Anh", ["0969996669", "0123456789"], ["anhpt1@xxx", "pta@xyz"], "Vung Tau", "handsome",
                     ["friend", "family", "co-worker"])

    while True:
        option = show_menu()
        if option == SHOW_ALL_DATA:
            print(f"\nPesonal information of '{person.name}':".upper())
            print(f"""
                +) {"Name:":10}{person.name}
                +) {"Phone:":10}{person.phones}
                +) {"Email:":10}{person.emails}
                +) {"Address:":10}{person.address}
                +) {"Note:":10}{person.note}
                +) {"Tag:":10}{person.tags}""")
        elif option == UPDATE_DATA:
            answer = choose_info_update()
            print(f"Enter new value of {answer}: \t")
            if answer == "phones" or answer == "emails" or answer == "tags":
                print("(You may enter multiple values. Enter nothing to break)")
                #person.answer = person.revise_list()
                if answer == "phones":
                    person.phones = person.revise_list()
                elif answer == "emails":
                    person.emails = person.revise_list()
                else:
                    person.tags = person.revise_list()
            else:
                #person.answer = person.revise_individual()
                if answer == "name":
                    person.name = person.revise_individual()
                elif answer == "address":
                    person.address = person.revise_individual()
                else:
                    person.note = person.revise_individual()
        else:
            tag = input("\nEnter a tag name that you want to check: ")
            if check_tag(tag, person.tags):
                print(f"\n{person.name} is in tag '{tag}'")
            else:
                print(f"\n{person.name} does not classify in tag '{tag}'")

        answer = try_again("\nDo you want to continue? (Y/N): ")
        if answer != True:
            print("\nBYE! SEE YOU NEXT TIME!!!")
            break