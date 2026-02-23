class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours:int, minutes:int, seconds:int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, new_h:int, new_min:int, new_sec:int):
        self.hours =  max(0, min(Time.max_hours, new_h))
        self.minutes = max(0, min(Time.max_minutes, new_min))
        self.seconds = max(0, min(Time.max_seconds, new_sec))

    def get_time(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def next_second(self):
        self.seconds = (self.seconds + 1) % 60
        if self.seconds == 0:
            self.minutes = (self.minutes + 1) % 60
            if self.minutes == 0:
                self.hours = (self.hours + 1) % 24
        return self.get_time()

# Test code
time = Time(9, 30, 59)
print(time.next_second())
time = Time(10, 59, 59)
print(time.next_second())
time = Time(23, 59, 59)
print(time.next_second())
