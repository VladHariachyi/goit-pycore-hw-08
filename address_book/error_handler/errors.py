class AddressBookError(Exception):
    """The address book error definition"""
    def __init__(self, message: str):
        super().__init__(f"[Address Book Error] {message}")

class InputError(Exception):
    """The input error definition"""
    def __init__(self, message: str):
        super().__init__(f"[Input Error] {message}")