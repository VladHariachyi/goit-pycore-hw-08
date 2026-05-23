from typing import Callable, Any
from functools import wraps

from ...error_handler import InputError


def check_args(
    callback: Callable[[tuple[Any]], Any]
) -> Callable[[tuple[str] | None, tuple[Any]], Any]:
    """Decorator that validates whether the number of provided arguments matches the expected amount.

    Arguments:
    function_to_decorate (Callable) -- Function which should be decorated for arguments validation.

    Returns:
    decorated_function (Callable) -- The decorated function, which expects the tuple of 
    expected arguments as first argument and the tuple of received arguments. The
    order of expected arguments should match with order of received arguments for 
    correct applying them to the decorated fn.
    """
    @wraps(callback)
    def wrapper(expected_params_keys: tuple[str] | None, *args: tuple[Any]) -> Any:
        if expected_params_keys is None:
            return callback()

        if (len(args) != len(expected_params_keys)):
            raise InputError(f"Expected {len(expected_params_keys)} params, but received {len(params)}")
        
        generated_params = {key: args[index] for index, key in enumerate(expected_params_keys)}

        return callback(**generated_params)

    return wrapper