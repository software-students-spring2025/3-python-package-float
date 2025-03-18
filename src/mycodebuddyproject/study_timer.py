import time
import threading
import tkinter as tk  # Using this so we can have a popup when time is up
from tkinter import messagebox
import platform

class StudyTimer:
    def __init__(self):
        self.study_minutes = None      
        self.start_time = None        
        self.elapsed_time = 0          
        self.running = False           
        self.paused = False            
        self.timer_thread = None       
        self.completed = False         

    def _track_time(self):
        # This method runs on a separate thread.
        while self.running:
            if self.paused:
                time.sleep(1)  # If paused, sleep and loop without incrementing time.
                continue
            time.sleep(1)     
            self.elapsed_time += 1  
            if self.study_minutes is not None and self.elapsed_time >= self.study_minutes * 60:
                self.running = False
                self.completed = True  # Set the flag indicating completion.
                print(f"\nCONGRATS ON LOCKING IN FOR {self.study_minutes} MINUTES! \n Now it's time for a break")
                break


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

