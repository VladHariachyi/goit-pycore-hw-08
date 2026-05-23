from ..address_book import AddressBook
from .event_uitls import (
    add_contact,
    show_phone,
    change_contact,
    remove_phone,
    show_all,
    add_birthday,
    show_birthday,
    show_upcoming_birthdays,
    remove_contact,
    add_phone
)
from ..error_handler import error_handler, AddressBookError


@error_handler
def handle_event(
    event_name: str, 
    addressBook: AddressBook, 
    *args
) -> str | None:
    """Contacts events handler.

    Arguments:
    event_name (str) -- The contact manager event name, supported events: "add_contact",
    "change_contact", "show_phone", "show_all_contacts", "add_birthday", "show_birthday",
    "show_upcoming_birthdays", "remove_phone", "remove_contact", "add_phone"

    addressBook (AddressBook) -- The address boo storage.

    input_data (tuple[str]) -- User input data 

    Returns:
    result (str | None) -- Returns result of event handler execution.
    """
    if addressBook is None:
        raise AddressBookError("Is not possible to handle event due to missed address book")

    match event_name:
        case "add_contact":
            return add_contact(
                ("book", "contact_name", "phone_number"),
                addressBook,
                *tuple((args if len(args) == 2 else (args + (None,))))
            )
        case "change_contact":
            return change_contact(
                ("book", "contact_name", "current_phone_number", "new_phone_number"),
                addressBook,
                *args
            )
        case "add_phone":
            return add_phone(
                ("book", "contact_name", "phone_number"),
                addressBook,
                *args
        )
        case "remove_phone":
            return remove_phone(
                ("book", "contact_name", "phone_number"),
                addressBook,
                *args
            )
        case "show_phone":
            return show_phone(
                ("book", "contact_name"),
                addressBook,
                *args
            )
        case "show_all_contacts":
            return show_all(
                ("book",),
                addressBook
            )
        case "add_birthday":
            return add_birthday(
                ("book", "contact_name", "birthday"), 
                addressBook,
                *args
            )
        case "show_birthday":
            return show_birthday(
                ("book", "contact_name"), 
                addressBook,
                *args,
            )
        case "show_upcoming_birthdays":
            return show_upcoming_birthdays(
                ("book",),
                addressBook
            )
        case "remove_contact":
            return remove_contact(
                ("book", "contact_name"),
                addressBook,
                *args,
            )