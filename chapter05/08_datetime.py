from datetime import datetime, timedelta

def main():
    print("1. Current Date and Time")
    now = datetime.now()
    print(f"Current date and time: {now}")
    print(f"European format: {now.strftime('%d/%m/%y %H:%m:%S')}")

    print("\nCreate a specific date and time")
    specific_date_time = datetime(2024, 12, 25, 15, 30)     # Christmass 25/12/2024 15:30
    print(f"\nSpecific date time: {specific_date_time.strftime('%d/%m/%Y %H:%M')}")

    # Parsing a European Date String
    european_date_str = "03/12/2024 20:25"  # DD/MM/YYYY HH:MM
    parsed_date = datetime.strptime(european_date_str, '%d/%m/%Y %H:%M')
    print(f"\nParsed dete and time from string: {parsed_date.strftime('%d/%m/%Y %H:%M')}")

    # Date Arithmetic
    print("\nDate arithmetic")
    one_week_later = parsed_date + timedelta(weeks=1)
    print(f"One week later: {one_week_later.strftime('%d/%m/%Y %H:%M')}")

    # 5 days earlier
    five_days_earlier = parsed_date - timedelta(days=5)
    print(f"5 days earlier: {five_days_earlier.strftime('%d/%m/%Y %H:%M')}")

    # Comparing Dates
    print("\nComparing Dates")
    today = datetime.now()

    if parsed_date > today:
        print(f"{parsed_date.strftime('%d/%m/%Y %H:%M')} is in the future.")
    elif parsed_date < today:
        print(f"{parsed_date.strftime('%d/%m/%Y %H:%M')} is in the past.")
    else:
        print(f"{parsed_date.strftime('%d/%m/%Y %H:%M')} is now.")

    # Localized DateTime (Requires Babel)
    # pip install babel

    try:
        from babel.dates import format_datetime

        print("\nLocalized datetime example")
        print(format_datetime(now, format='full', locale='fr_FR'))
        print(format_datetime(now, format='full', locale='de_DE'))

    except ImportError:
        print("Babel not installed.")

if __name__ == "__main__":
    main()