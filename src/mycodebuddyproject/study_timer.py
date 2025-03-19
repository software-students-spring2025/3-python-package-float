import time
import threading


class StudyTimer:
    def __init__(self):
        self.start_time = None
        self.elapsed_time = 0
        self.running = False
        self.timer_thread = None
        self.study_duration = 0  # Total study duration in seconds
        self.timer_expired = False
        self.break_prompt = False


    def _track_time(self):
        while self.running and self.elapsed_time < self.study_duration:
            time.sleep(1)
            self.elapsed_time += 1
        if self.elapsed_time >= self.study_duration:
            self.stop()  # Automatically stop when time is up
            self.timer_expired = True
            self.break_prompt = True


    def start(self):  # starts session time
        if self.running:
            print("Study session is already running!")
            return
        
        # Get user input for how many minutes to study
        try:
            minutes = int(input("How many minutes would you like to study for? "))
            self.study_duration = minutes * 60  # Convert minutes to seconds
        except ValueError:
            print("Please enter a valid number.")
            return

        if self.study_duration <= 0:
            print("Please enter a positive number of minutes.")
            return
        
        self.running = True
        self.start_time = time.time()
        self.elapsed_time = 0
        self.timer_thread = threading.Thread(target=self._track_time, daemon=True)
        self.timer_thread.start()
        print(f"Study session started for {minutes} minutes! Good luck, you got it!!")


    def stop(self):  # stops / asks user for break
        if not self.running:
            print("No study session is currently running.")
            return
        self.running = False
        if self.elapsed_time >= self.study_duration:
            print(f"\nBEEP! BEEP! BEEP! Timer has expired. Total time: {self.elapsed_time // 60} min {self.elapsed_time % 60} sec")
            return
        else:
            self.break_prompt = True
            print(f"Timer is stopped. Total time: {self.elapsed_time // 60} min {self.elapsed_time % 60} sec")
            return input("Would you like a break? (yes/no): ").strip().lower()


    def resume(self):  # resumes session after break
        if self.running:
            print("Study session is already running!")
            return
        print("Resuming study session...")
        self.running = True
        self.timer_thread = threading.Thread(target=self._track_time, daemon=True)
        self.timer_thread.start()

