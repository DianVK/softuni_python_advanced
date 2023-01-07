class Time():
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        if hours <= Time.max_hours and minutes <= Time.max_minutes and seconds <= Time.max_seconds:
            self.hours = hours
            self.minutes = minutes
            self.seconds = seconds

    def get_time(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def next_second(self):
        if self.seconds + 1 < Time.max_seconds:
            self.seconds += 1
        else:
            self.seconds = 00
            if self.minutes + 1 < Time.max_minutes:
                self.minutes += 1
            else:
                self.minutes = 00
                if self.hours + 1 < Time.max_hours:
                    self.hours += 1
                else:
                    self.hours = 00
        return self.get_time()


time = Time(9, 30, 59)
print(time.next_second())
time = Time(10, 59, 59)
print(time.next_second())
time = Time(23, 59, 59)
print(time.next_second())
