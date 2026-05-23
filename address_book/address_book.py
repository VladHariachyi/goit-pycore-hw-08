from collections import UserDict
from pathlib import Path
from rich import print
import pickle

from .record import Record
from .record_fields import Birhday
from .error_handler import error_handler, AddressBookError
from .utils import get_upcoming_birthdays as upcomming_brthds, ContactUpcomingBirthday, Status


class AddressBook(UserDict):
    def __getstate__(self):
        """Generation the address book current state which to be saved

        Retunrns:
        address_book_state -- The current address book state
        """
        return self.data

    def __setstate__(self, state):
        """Retrieves the address book state

        Arguments:
        address_book_state -- The state which need to retreive 
        """
        if state:
            self.data = state
            print(f"[green3]The address book data is successfuly retreived[/green3]")
        else:
            print(f"[yellow1]Is not possible to retreive address book state due to missed data [/yellow1]")

    """The address book class definition, responsible for managing book record"""
    def add_record(self, record: Record) -> None:
        """Adds a new record to the address book

        Arguments:
        record (Record) -- New record
        """
        contact_name = record.name.value

        if contact_name:
            self.data[contact_name] = record
            return f"[green3]The contact '{contact_name}' is successfully added[/green3]"
        else:
            raise AddressBookError(f"The record has empty contact name") 

    def find(self, contact_name: str) -> Record | None:
        """Finds record by contact name

        Arguments:
        contact_name (str) -- Contact name by which need to make a search

        Returns:
        found_record (Record | None) -- Returns the record instance or "None" if not found
        """
        found_record = self.data.get(contact_name)

        return found_record

    def delete(self, contact_name: str) -> None:
        """Deletes the record from the address book by contact name

        Arguments:
        contact_name (str) -- Contact name which need to remove
        """
        if contact_name in self.data:
            del self.data[contact_name]
        else:
            raise AddressBookError(f"The contact '{contact_name}' is not found")

    @error_handler    
    def get_upcoming_birthdays(self) -> list[ContactUpcomingBirthday]:
        """Generates a list of upcoming contacts birthdays for 7 days in advance including today.
        
        Returns:
        upcomming_birthdays (list[ContactUpcomingBirthday]) -- List of upcoming birthdays
        """
        prepared_contacts_birthdays = map(
            lambda record: { 
                "name": record.name.value,
                "birthday": record.birthday.value if record.birthday is not None else None
            },
            self.data.values()
        )

        return upcomming_brthds(prepared_contacts_birthdays, Birhday.format)
        

def save_data(book: AddressBook, file_path: str) -> Status:
    """Saves the address book state to file

    Arguments:
    file_path -- The file path where should be saved the address book state

    Returns:
    status (Status ENUM) -- The status of saving address book state, possible values
    "SUCCESS" or "ERROR"
    """
    try: 
        with open(Path(__file__).parent.parent / file_path, "wb") as f:
            pickle.dump(book, f)
            return Status.SUCCESS
    except FileNotFoundError:
        return Status.ERROR


def load_data(file_path: str) -> AddressBook:
    """Creates the address book and retreive its state if exist

    Arguments:
    file_path -- The file path where the address book state is saved

    Returns:
    address_book (AddressBook) -- Returns the address book with retreived state OR 
    with clean state if state was not retreived.
    """
    try:        
        with open(Path(__file__).parent.parent / file_path, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()