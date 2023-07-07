from address_book import AddressBook

book = AddressBook()


def add(*args, **kwargs):
    book.add({'key': 'value'})
