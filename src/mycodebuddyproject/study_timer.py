import time
import threading
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
        self._can_tick = None  # Internal event to delay tick loop start


    def _track_time(self):
        # Wait until ticks are enabled.
        self._can_tick.wait()
        while self.running:
            # Check for completion at the start of the loop.
            if self.study_minutes is not None and self.elapsed_time >= self.study_minutes * 60:
                self.running = False
                self.completed = True
                print(f"\nCONGRATS ON LOCKING IN FOR {self.study_minutes} MINUTES! \nTurn off the alarm and take a break")
                break


            if self.paused:
                time.sleep(1)
                continue


            time.sleep(1)
            self.elapsed_time += 1


    def start(self, minutes = -1):
        if self.running:
            print("\nStudy session is already running!")
            return
        if minutes <= 0:
            try:
                minutes = int(input("\nEnter the number of minutes you want to study: "))
                if minutes <= 0:
                    print("Please enter a positive number.")
                    return
                self.study_minutes = minutes
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                return
        else:
            self.study_minutes=minutes

        self.elapsed_time = 0
        self.running = True
        self.paused = False
        self.completed = False
        self.start_time = time.time()
        self._can_tick = threading.Event()
        self.timer_thread = threading.Thread(target=self._track_time, daemon=True)
        self.timer_thread.start()


        # Use a slight delay to allow tests to observe the initial state.
        threading.Timer(0.1, self._can_tick.set).start()


        print("\nStudy session started! Good luck, you got it!!")
        print("Enter 'pause' to pause the session at any time.")


    def pause(self):
        if not self.running:
            print("No study session is running.")
            return
        if self.paused:
            print("Study session is already paused.")
            return
        self.paused = True
        print("\nStudy session paused, please enter 'resume' when you want to resume.")


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
