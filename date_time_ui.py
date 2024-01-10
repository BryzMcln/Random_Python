import tkinter as tk
from datetime import datetime
from calendar import month_name, monthcalendar


class DateTimeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Date and Time Display")

        self.time_label = tk.Label(root, font=("Helvetica", 24))
        self.time_label.pack(pady=20)

        self.calendar_label = tk.Label(root, font=("Helvetica", 12), justify="left")
        self.calendar_label.pack()

        self.update_display()

    def update_display(self):
        now = datetime.now()
        current_time = now.strftime("%I:%M:%S %p")
        current_date = f"{month_name[now.month]} {now.day}, {now.year}"

        self.time_label.config(text=f"Time: {current_time}")
        self.calendar_label.config(
            text=f"Calendar:\n{current_date}\n\n{self.get_calendar(now.year, now.month)}"
        )

        self.root.after(
            1000, self.update_display
        )  # Update every 1000 milliseconds (1 second)

    def get_calendar(self, year, month):
        cal = monthcalendar(year, month)
        calendar_str = "Mon Tue Wed Thu Fri Sat Sun\n"
        for week in cal:
            for day in week:
                if day == 0:
                    calendar_str += "    "
                elif day == datetime.now().day:
                    calendar_str += f"[{day:2}] "
                else:
                    calendar_str += f"{day:2} "
            calendar_str += "\n"
        return calendar_str


if __name__ == "__main__":
    root = tk.Tk()
    app = DateTimeApp(root)
    root.mainloop()
