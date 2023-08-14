print('error')
""" import datetime
def generate_calendar(num_days, num_hours, num_minutes, num_seconds, start_date):
    curr_datetime = start_date
    delta = datetime.timedelta(days=num_days, hours=num_hours, minutes=num_minutes, seconds=num_seconds)
    
    while curr_datetime < start_date + delta:
        if curr_datetime.weekday() == 6:  # Sunday is represented by 6 in the datetime.weekday() function
            print(curr_datetime.strftime("%A, %B %d, %Y %I:%M:%S %p") + " (Sunday)")
        else:
            print(curr_datetime.strftime("%A, %B %d, %Y %I:%M:%S %p"))
        
        curr_datetime += datetime.timedelta(seconds=1)
        
    if __name__ == "__main__":
        num_days = int(input("Enter number of days: "))
        num_hours = int(input("Enter number of hours: "))
        num_minutes = int(input("Enter number of minutes: "))
        num_seconds = int(input("Enter number of seconds: "))
        start_date_str = input("Enter start date (YYYY-MM-DD HH:MM:SS): ")
        start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d %H:%M:%S")
        
        generate_calendar(num_days, num_hours, num_minutes, num_seconds, start_date) """