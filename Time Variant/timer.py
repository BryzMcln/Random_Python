import time, os
def title():
    print("SET YOUR TIMER")

def clr():
     os.system('cls')

def set_timer():
    while True:
        try:
            clr()
            title()
            hours = int(input("Hours: "))
            minutes = int(input("Minutes: "))
            seconds = int(input("Seconds: "))
            
            total_seconds = hours * 3600 + minutes * 60 + seconds
            
            if total_seconds <= 0:
                print("Timer value should be greater than 0.")
                continue  # Restart the timer input loop
            
            print(f"Timer set for {hours} hours, {minutes} minutes, and {seconds} seconds.")
            clr()
            while total_seconds > 0:
                hours_remaining = total_seconds // 3600
                minutes_remaining = (total_seconds % 3600) // 60
                seconds_remaining = total_seconds % 60
                
                time_str = f"{hours_remaining:02}:{minutes_remaining:02}:{seconds_remaining:02}"
                print(f"Time left: {time_str}", end='\r')
                
                time.sleep(1)
                total_seconds -= 1
            
            print("\nTime's Up!")
            input("Press any key...")
            retry = input("Do you want to set another timer? (yes/no): ").strip().lower()
            if retry != 'yes':
                break  # Exit the timer loop if the user doesn't want to set another timer
        except ValueError:
            print("Invalid input. Please enter valid numbers for hours, minutes, and seconds.")

if __name__ == "__main__":
    set_timer()
