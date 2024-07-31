import tkinter as tk
from tkinter import messagebox
import datetime
import time
import threading

class AlarmClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Alarm Clock")
        self.root.geometry("300x250")

        self.current_time_label = tk.Label(root, text="Current Time:")
        self.current_time_label.pack(pady=5)
        self.current_time_display = tk.Label(root, text="", font=('Helvetica', 16))
        self.current_time_display.pack(pady=5)

        self.alarm_time_label = tk.Label(root, text="Set Alarm Time (HH:MM):")
        self.alarm_time_label.pack(pady=5)
        self.alarm_time_entry = tk.Entry(root)
        self.alarm_time_entry.pack(pady=5)

        self.set_alarm_button = tk.Button(root, text="Set Alarm", command=self.set_alarm)
        self.set_alarm_button.pack(pady=5)

        self.delete_alarm_button = tk.Button(root, text="Delete Alarm", command=self.delete_alarm)
        self.delete_alarm_button.pack(pady=5)

        self.alarm_status_label = tk.Label(root, text="")
        self.alarm_status_label.pack(pady=10)

        self.alarm_time = None
        self.alarm_thread = None
        self.update_time()

    def set_alarm(self):
        alarm_time_str = self.alarm_time_entry.get()
        try:
            self.alarm_time = datetime.datetime.strptime(alarm_time_str, "%H:%M").time()
            self.alarm_status_label.config(text=f"Alarm set for {self.alarm_time.strftime('%H:%M')}")
            self.start_alarm_thread()
        except ValueError:
            messagebox.showerror("Invalid Time Format", "Please enter the time in HH:MM format.")

    def delete_alarm(self):
        self.alarm_time = None
        if self.alarm_thread and self.alarm_thread.is_alive():
            self.alarm_thread.join()
        self.alarm_status_label.config(text="Alarm deleted.")
        self.root.update()

    def update_time(self):
        now = datetime.datetime.now()
        current_time_str = now.strftime("%H:%M:%S")
        self.current_time_display.config(text=current_time_str)
        self.root.after(1000, self.update_time)

    def start_alarm_thread(self):
        if not self.alarm_thread or not self.alarm_thread.is_alive():
            self.alarm_thread = threading.Thread(target=self.check_alarm)
            self.alarm_thread.start()

    def check_alarm(self):
        while True:
            if self.alarm_time:
                now = datetime.datetime.now().time()
                if now.hour == self.alarm_time.hour and now.minute == self.alarm_time.minute:
                    self.trigger_alarm()
                    break
            time.sleep(10)

    def trigger_alarm(self):
        messagebox.showinfo("Alarm", "Wake up!")

if __name__ == "__main__":
    root = tk.Tk()
    app = AlarmClock(root)
    root.mainloop()
