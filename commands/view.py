from address_book import AddressBook

book = AddressBook()


def view(*args, **kwargs):
    print(book.value_of())
