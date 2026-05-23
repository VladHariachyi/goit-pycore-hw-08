from dataclasses import dataclass
from datetime import datetime
import re

from .error_handler import error_handler


@dataclass
class Field:
    """The data field definition"""
    value: str

    def __str__(self) -> str:
        return f"{self.value}" 


class Name(Field):
    """The contact name class definition, responsible for saving the contact name"""
    pass


class Phone(Field):
    """The phone class definition, responsible for saving, editing and validating the phone number"""
    @error_handler
    @staticmethod
    def is_valid(phone_number: str) -> bool:
        """The static class method responsible for phone number validation

        Arguments:
        phone_number (str) -- The phone number to validate

        Returns:
        is_valid (bool) -- Returns a flag which determiness if the phone number is valid
        """
        return re.match(r"\d{10}", phone_number) is not None
    
    @error_handler
    def edit(self, phone_number: str) -> None:
        """Edit phone number via replacing current phone number with a new one

        Arguments:
        phone_number (str) -- New phone number
        """
        self.value = phone_number


class Birhday(Field):
    """The birthday class definition, responsible for saving and validating the birthday date"""
    format = "%d.%m.%Y"

    @staticmethod
    def is_valid(birthday: str) -> bool:
        """The static class method responsible for birthday date validation

        Arguments:
        birthday (str) -- The birthday date to validate

        Returns:
        is_valid (bool) -- Returns a flag which determiness if the birthday date is valid
        """

        try:
            _ = datetime.strptime(birthday, Birhday.format)
            return True
        except:
            return False
