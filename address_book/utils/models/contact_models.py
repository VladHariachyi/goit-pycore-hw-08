from typing import Protocol
from dataclasses import dataclass


class ContactBirthdayInfo(Protocol):
    """The contact birthday info type definition"""
    name: str
    birthday: str | None

@dataclass      
class ContactUpcomingBirthday:
    """The upcoming contact class birthday definition"""
    contact_name: str
    birthday: str

    def __str__(self) -> str:
        return f"{self.contact_name} will celebrate birthday at {self.birthday}" 