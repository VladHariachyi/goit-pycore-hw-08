from rich import print

from user_events import handle_event, is_user_event
from address_book import load_data, save_data, Status


def parse_user_input(user_input: str) -> tuple[str]:
    """Parse the user input.

    Arguments:
    user_input (str) -- The user input.

    Returns:
    parsed_data (tuple[str]) -- Retunrs the tumple, where first item is the command name and rest items are user params.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()

    return (cmd, *args)

def main():
    """ The user manager CLI. Currently supports the Contact Managment functionality."""
    print(f"[blue1]Welcome to the assistant bot (^_^)[/blue1]")
    address_book_data_file_path = "data/address_book.bin"
    book = load_data(address_book_data_file_path)

    while(True):
        user_input = input(f"Enter a command: ")
        command, *args = parse_user_input(user_input)

        if command in ["close", "exit"]:
            print(f"[gold1]Good bye![/gold1]")
            break

        if command == "save_and_exit":
            status = save_data(book, address_book_data_file_path)
            message = None

            if status == Status.SUCCESS:
                message = f"[gold1]The data is saved to '{address_book_data_file_path}'. Good bye![/gold1]"
            else:
                message = (
                    "[red]Is not possible to save data by provided path "
                    f"'{address_book_data_file_path}', directory does not exist[/red]")
            
            print(message)
            break

        if command == "hello":
            print(f"[gold1]How can I help you?[/gold1]")
            continue

        if is_user_event(command):
            res = handle_event(command, book, *args) 

            if res is not None:
                print(res)

            continue

        print(f"[red]The '{command}' command is not supportred![/red]")


if __name__ == "__main__":
    main()
