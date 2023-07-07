from address_book import AddressBook

book = AddressBook()


def search(*args, **kwargs):
    book.search(input('Enter key: '))
