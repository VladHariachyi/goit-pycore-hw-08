from rich import print

from ..utils import check_args
from ..error_handler import error_handler, AddressBookError
from ..address_book import AddressBook
from ..record import Record


@error_handler
@check_args
def add_contact(book: AddressBook, contact_name: str, phone_number: str) -> str:
    """Adds contact to the address book.

    Arguments:
    address_book (AddressBook) -- The address book storage
    contact_name (str) -- The new contact name
    phone_number (str) -- The new contact phone number

    Returns:
    status (str) -- Success status message
    """
    record = book.find(contact_name)
    message = f"[green3]The '{phone_number}' phone number is successfully updated for '{contact_name}'[/green3]"

    if record is None:
        record = Record(contact_name)
        book.add_record(record)
        message = f"[green3]The contact '{contact_name}' is successfully added[/green3]"

    if phone_number:
        record.add_phone(phone_number)

    return message

@error_handler
@check_args
def add_phone(book: AddressBook, contact_name: str, phone_number: str) -> str:
    """Adds phone to the existing contact.

    Arguments:
    address_book (AddressBook) -- The address book storage
    contact_name (str) -- The existing contact name
    phone_number (str) -- The new contact phone number

    Returns:
    status (str) -- Success status message
    """
    record = book.find(contact_name)

    if record is None:
        raise AddressBookError(f"The '{contact_name}' is not found")
    
    record.add_phone(phone_number)

    return f"[green3]The phone number '{phone_number}' is successfully added[/green3]"

@error_handler
@check_args
def change_contact(
    book: AddressBook, 
    contact_name: str, 
    current_phone_number: str,
    new_phone_number: str
) -> str:
    """Change contact phone number.

    Arguments:
    address_book (AddressBook) -- The address book storage
    contact_name (str) -- The existing contact name
    current_phone_number (str) -- The current contact phone number
    new_phone_number (str) -- The new contact phone number

    Returns:
    status (str) -- Success status message
    """
    record = book.find(contact_name)

    if record is None:
        raise AddressBookError(f"The '{contact_name}' is not found")
    
    record.edit_phone(current_phone_number, new_phone_number)

    return f"[green3]The phone number is successfully edited for '{contact_name}' contact[/green3]"

@error_handler
@check_args
def show_phone(book: AddressBook, contact_name: str) -> None:
    """Shows contact phone numbers.

    Arguments:
    address_book (AddressBook) -- The address book storage
    contact_name (str) -- The existing contact name
    """
    record = book.find(contact_name)

    if record is None:
        raise AddressBookError(f"The '{contact_name}' is not found")
    
    print(str(record))

@error_handler
@check_args
def remove_phone(book, contact_name: str, phone_number: str) -> str:
    """Removes contact phone number.

    Arguments:
    address_book (AddressBook) -- The address book storage
    contact_name (str) -- The existing contact name
    phone_number (str) -- The contact phone number which need to remove

    Returns:
    status (str) -- Success status message
    """
    record = book.find(contact_name)

    if record is None:
        raise AddressBookError(f"The '{contact_name}' is not found")
    
    record.remove_phone(phone_number)

    return f"[green3]The '{phone_number}' phone number is successfully removed[/green3]"

@error_handler
@check_args
def show_all(book: AddressBook) -> None:
    """Shows all contacts.

    Arguments:
    address_book (AddressBook) -- The address book storage
    """
    for record in book.data.values():
        print(str(record))

@error_handler
@check_args
def add_birthday(book: AddressBook, contact_name: str, birthday: str) -> str:
    """Adds contact birthday date.

    Arguments:
    address_book (AddressBook) -- The address book storage
    contact_name (str) -- The existing contact name
    birthday (str) -- The birthday date to add 

    Returns:
    status (str) -- Success status message
    """
    record = book.find(contact_name)

    if record is None:
        raise AddressBookError(f"The '{contact_name}' is not found")
    
    record.add_birthday(birthday)

    return f"[green3]The birthday date is successfully added for '{contact_name}' contact[/green3]"


@error_handler
@check_args
def show_birthday(book: AddressBook, contact_name: str) -> None:
    """Shows contact birthday date.

    Arguments:
    address_book (AddressBook) -- The address book storage
    contact_name (str) -- The existing contact name
    """
    record = book.find(contact_name)

    if record is None:
        raise AddressBookError(f"The '{contact_name}' is not found")
    
    if record.birthday is None:
        print(f"[gold1]The '{contact_name}' doesn't have defined the birthday date[/gold1]")
    else:
        print(f"[gold1]The '{contact_name}' has birthday at {record.birthday.value}[/gold1]")

@error_handler
@check_args
def show_upcoming_birthdays(book: AddressBook) -> None:
    """Shows contacts upcoming birthdays.

    Arguments:
    address_book (AddressBook) -- The address book storage
    """
    for upcoming_birthday in book.get_upcoming_birthdays():
        print(f"[gold1]{upcoming_birthday}[/gold1]")

@error_handler
@check_args
def remove_contact(book: AddressBook, contact_name: str) -> str:
    """Removes contact from the address book.

    Arguments:
    address_book (AddressBook) -- The address book storage
    contact_name (str) -- The existing contact name

    Returns:
    status (str) -- Success status message
    """
    book.delete(contact_name)
    return f"[green3]The contact '{contact_name}' is successfully removed[/green3]"