import threading

class Threading:
    def __init__(self):
        self.first_done = threading.Event()
        self.second_done = threading.Event()

    def first(self):
        print("First thread is running")
        self.first_done.set()
    
    def second(self):
        self.first_done.wait()
        print("Second thread is running")
        self.second_done.set()
    
    def third(self):
        self.second_done.wait()
        print("Third thread is running")

thread = Threading()

first_thread = threading.Thread(target=thread.first)
second_thread = threading.Thread(target=thread.second)
third_thread = threading.Thread(target=thread.third)

# Start in any order
third_thread.start()
second_thread.start()
first_thread.start()

# Wait for all threads to finish
first_thread.join()
second_thread.join()
third_thread.join()