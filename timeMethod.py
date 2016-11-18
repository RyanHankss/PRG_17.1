class Time(object):
    def time_int(self):
        seconds = (self.hour * 60 * 60) + (self.minute * 60) + self.second
        print seconds


t = Time()
t.hour = 11
t.minute = 34
t.second = 33

Time.time_int(t)
