from .user_events_constants import USER_EVENTS
from address_book import ADDRESS_BOOK_EVENTS, handle_event as handle_address_event


def is_user_event(event_name: str) -> bool:
    """Check if event is the user event.

    Arguments:
    event_name (str) -- The user event name.

    Returns:
    is_user_event (bool) -- The validation result.
    """
    return event_name in USER_EVENTS

def is_contact_event(event_name: str) -> bool:
    """Check if event is related to Contact Manager events.

    Arguments:
    event_name (str) -- The user event name.

    Returns:
    is_contact_event (bool) -- The validation result.
    """
    return event_name in ADDRESS_BOOK_EVENTS

def handle_event(
    event_name: str, 
    data_store: dict | None, 
    *args: tuple[str]
) -> str | None:
    """User events handler.

    Arguments:
    event_name (str) -- The user event name. Currently events for Contact Maager are supported.

    data_store (dict[str, str] | None) -- The data store which will be processed by event handlers.

    args (tuple[str]) -- The event params. 

    Returns:
    result (str | None) -- Returns result of event handler execution.
    """
    if is_contact_event(event_name):
        return handle_address_event(event_name, data_store, *args)