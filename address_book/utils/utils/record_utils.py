from datetime import datetime, timedelta

from ..models import ContactBirthdayInfo, ContactUpcomingBirthday
    

def get_upcoming_birthdays(
    contacts_birthdays: list[ContactBirthdayInfo],
    date_format: str
) -> list[ContactUpcomingBirthday]:
    """Generates a list of upcoming birthdays for 7 days in advance including today.

    Arguments:
    contacts_birthdays (list[ContactBirthdayInfo]) -- The list of contacts, birthdays of whose need to check. 
    date_format (str) -- The date format which is using for parsing the date in sting format.
    Default is "%d.%m.%Y"

    Returns:
    upcoming_birthdays (list[UpcomingBirthday]) -- The list of contacts whose need to congratulate on this week. Users who have already
    had their birthday will be congratulated next year on their birthday date. The UpcomingBirthday class instace
    consist of folloiwng properties:
        -- contact_name (str) -- Determines the contact name
        -- user.congratulation_date (str) -- Determines the scheduled congratulation date. Contacts who 
        have birthday on the weekend will be congratulated on the Monday of the next week. 
    """
    today = datetime.now().date()
    upcoming_birthdays = []

    for contact in contacts_birthdays:
        if contact["birthday"] is None:
            continue
        
        contact_name = contact["name"]
        contact_birthday = datetime.strptime(contact["birthday"], date_format).date()
        birthday_this_year = datetime(
            year=today.year,
            month=contact_birthday.month,
            day=contact_birthday.day
        ).date()

        if birthday_this_year < today:
            next_year_birthday_date = birthday_this_year.replace(year=birthday_this_year.year + 1)
            upcoming_birthdays.append(ContactUpcomingBirthday(
                contact_name, 
                datetime.strftime(next_year_birthday_date, date_format)
            ))

            continue

        upcoming_birthday_max_date = today + timedelta(days=6)
        is_date_in_range = birthday_this_year >= today and birthday_this_year <= upcoming_birthday_max_date

        if not is_date_in_range:
            continue
    
        saturday_weekday_number = 5
        sunday_weekday_number = 6
        is_birthday_on_weekend = birthday_this_year.weekday() in [saturday_weekday_number, sunday_weekday_number]
        congratulation_date = None

        if is_birthday_on_weekend:
            week_days_amount = 7
            amount_days_to_shift = week_days_amount - birthday_this_year.weekday()
            congratulation_date = birthday_this_year + timedelta(days=amount_days_to_shift)
        else:
            congratulation_date = birthday_this_year

        upcoming_birthdays.append(ContactUpcomingBirthday(
            contact_name, 
            datetime.strftime(congratulation_date, date_format)
        ))
    
    return upcoming_birthdays
