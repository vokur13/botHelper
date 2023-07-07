from address_book import AddressBook
from commander import Commander

book = AddressBook()


def main():
    # Use a breakpoint in the code line below to debug your script.
    book.load()
    commander = Commander()
    commander.command_yield()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
