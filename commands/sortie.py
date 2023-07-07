from address_book import AddressBook

book = AddressBook()


def sortie(*args, **kwargs):
    print('sortie foo')
    book.save()
