from typing import Callable, Any
from rich import print
from functools import wraps

from .errors import AddressBookError, InputError


def error_handler(callback: Callable[..., Any]):
    """Decorator that handles the errors.

    Arguments:
    function_to_decorate (Callable) -- Function which should be decorated for error handling.

    Returns:
    decorated_function (Callable) -- The decorated function which is wrap in try..except block
    to catch and hanle error which may triggered in the provided function.
    """
   # @wraps(callback)
    def wrapper(*args, **kwargs):
        try:
            return callback(*args, **kwargs)
        except (AddressBookError, InputError) as error:
            print(f"[red]{error}[/red]")
        except KeyError as missed_key:
            print(f"[red][Missed Key Error] '{missed_key}' doest not exist[/red]")
            return None
        except IndexError:
            print(f"[red][Index error] The requested index is out of the range[/red]")
            return None
        except ValueError:
            print(f"[red][Value error] Can't process the operation due to incorrect input[/red]")
            return None
        except FileNotFoundError as e:
            print(e)
            return None
        except Exception as error:
            print(f"[red][Error] The system can't respond: {error}[/red]")

    return wrapper
