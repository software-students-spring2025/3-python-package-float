import time
import threading

class StudyTimer:
    def __init__(self):
        self.start_time = None
        self.elapsed_time = 0
        self.running = False
        self.timer_thread = None

    def _track_time(self):
        while self.running:
            time.sleep(1)
            self.elapsed_time += 1

    def start(self): # starts session time
        if self.running:
            print("Study session is already running!")
            return
        self.running = True
        self.start_time = time.time()
        self.timer_thread = threading.Thread(target=self._track_time, daemon=True)
        self.timer_thread.start()
        print("Study session started! Good luck, you got it!!")

    def stop(self): # stops / asks user for break
        if not self.running:
            print("No study session is currently running.")
            return
        self.running = False
        print(f"Study session stopped. Total time: {self.elapsed_time // 60} min {self.elapsed_time % 60} sec")
        return input("Would you like a break? (yes/no): ").strip().lower()

    def resume(self): # resumes session after break
        if self.running:
            print("Study session is already running!")
            return
        print("Resuming study session...")
        self.running = True
        self.timer_thread = threading.Thread(target=self._track_time, daemon=True)
        self.timer_thread.start()
