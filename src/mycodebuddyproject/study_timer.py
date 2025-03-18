import time
import threading
import tkinter as tk  # Using this so we can have a popup when time is up
from tkinter import messagebox
import platform

class StudyTimer:
    def __init__(self):
        self.study_minutes = None      # Duration in minutes
        self.start_time = None         # When the session started
        self.elapsed_time = 0          # Elapsed time in seconds
        self.running = False           # Flag to indicate if the timer is active
        self.paused = False            # Flag for pause state
        self.timer_thread = None       # Background thread for tracking time
        self.completed = False         # Flag to indicate completion

    def _track_time(self):
        # This method runs on a separate thread.
        while self.running:
            if self.paused:
                time.sleep(1)  # If paused, sleep and loop without incrementing time.
                continue
            time.sleep(1)      # Wait for 1 second
            self.elapsed_time += 1  # Increment elapsed time by one second
            if self.study_minutes is not None and self.elapsed_time >= self.study_minutes * 60:
                self.running = False
                self.completed = True  # Set the flag indicating completion.
                print(f"\nCONGRATS ON LOCKING IN FOR {self.study_minutes} MINUTES! \n Now it's time for a break")
                break

    def show_popup(self):
        # This method creates a popup. It should run on the main thread.
        try:
            root = tk.Tk()
            root.withdraw()  # Hide the main Tk window.
            messagebox.showinfo("Study Timer", f"\nCONGRATS ON LOCKING IN FOR {self.study_minutes} MINUTES! \n Now it's time for a break")
            root.destroy()   # Destroy the Tk window after the popup.
        except Exception as e:
            print("Error displaying popup:", e)

    def start(self):
        if self.running:
            print("Study session is already running!")
            return

        # Ask the user for the duration in minutes.
        try:
            minutes = int(input("Enter the number of minutes you want to study: "))
            if minutes <= 0:
                print("Please enter a positive number.")
                return
            self.study_minutes = minutes
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return

        self.elapsed_time = 0
        self.running = True
        self.paused = False  # Make sure the timer starts unpaused.
        self.completed = False  # Reset the completed flag.
        self.start_time = time.time()
        self.timer_thread = threading.Thread(target=self._track_time, daemon=True)
        self.timer_thread.start()
        print("Study session started! Good luck, you got it!!")
        print("Enter 'pause' to pause the session at any time.")

    def pause(self):
        if not self.running:
            print("No study session is running.")
            return
        if self.paused:
            print("Study session is already paused.")
            return
        self.paused = True
        print("Study session paused, please enter 'resume' when you want to resume.")

    def resume(self):
        if not self.running:
            print("No study session is running.")
            return
        if not self.paused:
            print("Study session is not paused.")
            return
        self.paused = False
        print("Resuming now.")

    def cancel(self):
        if not self.running:
            print("No study session is currently running.")
            return
        self.running = False
        self.paused = False
        print("Study session canceled.")

if __name__ == "__main__":
    timer = StudyTimer()
    while True:
        command = input("Enter command (start, pause, resume, cancel, exit): ").strip().lower()
        if command == "start":
            timer.start()
        elif command == "pause":
            timer.pause()
        elif command == "resume":
            timer.resume()
        elif command == "cancel":
            timer.cancel()
        elif command == "exit":
            print("Exiting the study timer.")
            break
        else:
            print("Unknown command. Please try again.")
        
        # Check if the timer has completed (from the background thread).
        if timer.completed:
            # Call the popup on the main thread.
            timer.show_popup()
            timer.completed = False  # Reset the flag so the popup isn't shown repeatedly.
