from utils import person_data, balance_summary
from bank_account import BankAccount

persons = []

while True:
    try:
        option = input()
    except EOFError:
        break

    if option == "1":
        person = person_data()
        persons.append(person)

    elif option == "2":
        name = input()
        found = False

        for person in persons:
            if person.name == name:
                account_number = int(input())
                balance = float(input())
                person.add_account(BankAccount(account_number, balance))
                found = True
                break

        if not found:
            print("Person not found.")

    elif option == "3":
        if not persons:
            print("No data to show.")
        else:
            balance_summary(persons)

    elif option == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose 1-4.")