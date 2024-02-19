from datetime import datetime
from calendar import month_name, monthcalendar, day_abbr
import time, os, keyboard


# Function to clear the console screen (for better time display)
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def datetimes():
    try:
        while True:
            now = datetime.now()
            n = now.strftime("%I:%M:%S %p")
            y, m, d = now.year, now.month, now.day
            mm = f"{month_name[m]} {y}"  # Fix the format
            tm: str = "Time"

            clear_screen()  # Clear the screen to update the time

            print(f"{tm:^30} \n{n:^30}")
            print(f"\n{mm:^30}")  # Make it centered

            # Get the calendar for the current month
            cal = monthcalendar(y, m)

            # Print the day labels (Mon - Sun)
            print("Mon Tue Wed Thu Fri Sat Sun")

            # Iterate through the weeks in the calendar
            for week in cal:
                for day in week:
                    if day == 0:
                        # Print two spaces for empty days
                        print("  ", end=" ")
                    elif day == d:
                        # Highlight the current date
                        print(f"\033[1;31m{day:2}\033[m ", end=" ")
                    else:
                        # Print other dates
                        print(f"{day:2} ", end=" ")
                print()  # Move to the next line after each week

            time.sleep(1)  # Wait for 1 second before updating the time

    except KeyboardInterrupt:
        # Catch a keyboard interrupt (Ctrl+C) to exit the loop gracefully
        pass


if __name__ == "__main__":
    datetimes()
