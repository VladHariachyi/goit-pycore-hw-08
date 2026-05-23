from .error_handler import AddressBookError
from .record_fields import Name, Phone, Birhday


class Record:
    """The address book record class definition, responsible for managing phone number"""
    def __init__(self, name: str):
        """Initialise the record instance fields"""
        self.phones = []
        self.name = Name(name)
        self.birthday = None

    def __str__(self) -> str:
        """Converts the class intance to the readable way when it was converted to string type
        
        Returns:
        converted_instance_to_string (str) - The string which represents class instance when 
        it was converted to string type
        """
        phones = '; '.join(phone.value for phone in self.phones)
                           
        return f"[gold1]Contact name: {self.name.value}, phones: {phones}[/gold1]"

    def add_phone(self, phone_number: str) -> None:
        """Validates and add phone number to the record phone numbers list
        
        Arguments:
        phone_number (str) - The phone number which need to add to the record
        """
        if phone_number in map(lambda phone: phone.value, self.phones):
            raise AddressBookError((
                f"Phone number '{phone_number}' already exists"
            ))

        if (Phone.is_valid(phone_number)):
            self.phones.append(Phone(phone_number))
        else:
            raise AddressBookError((
                f"Phone number '{phone_number}' is not valid, "
                f"it should consist of 10 numeric symbols"
            ))

    def remove_phone(self, phone_number: str) -> None:
        """Removes phone number from the record phone numbers list
        
        Arguments:
        phone_number (str) - The phone number which need to add to the record
        """
        found_number = self.find_phone(phone_number)

        if found_number:
            self.phones.remove(found_number)
        else:
            raise AddressBookError(f"Phone number '{phone_number}' is not found")

    def edit_phone(
        self,
        current_phone_number: str, 
        new_phone_number: str
    ) -> None:
        """Edits the existing phone number to a new one 
        
        Arguments:
        current_phone_number (str) - The phone number which need to replace
        new_phone_number (str) - The new phone number
        """
        found_number = self.find_phone(current_phone_number)

        if (not found_number):
            raise AddressBookError(f"Phone number '{current_phone_number}' is not found")
        
        if not Phone.is_valid(new_phone_number):
            raise AddressBookError((
                f"Phone number '{new_phone_number}' is not valid, "
                f"it should consist of 10 numeric symbols"
            ))

        found_number.edit(new_phone_number)

    def find_phone(self, phone_number: str) -> Phone | None:
        """Finds the phone number instance by phone number in the record
        
        Arguments:
        phone_number (str) - The phone number which need to find in record phone numbers list

        Returns:
        found_phone_number (Phone | None) - Returns the phone number instance or "None" if not found
        """
        filtered_numbers = list(filter(lambda phone: phone.value == phone_number, self.phones))
        found_number = filtered_numbers[0] if len(filtered_numbers) else None

        return found_number
    
    def add_birthday(self, birthday: str) -> None:
        """Validates and add birthday date to the record
        
        Arguments:
        birthday (str) - The birthday date which need to add to the record
        """
        if (Birhday.is_valid(birthday)):
            self.birthday = Birhday(birthday)
        else:
            raise AddressBookError((
                f"Birthday date '{birthday}' is not valid, "
                f"the supported format is '{Birhday.format}'"
            ))