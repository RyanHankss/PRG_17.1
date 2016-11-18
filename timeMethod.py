class Time(object):
    def time_int(self):
        seconds = (self.hour * 60 * 60) + (self.minute * 60) + self.second
        print seconds


t = Time()
t.hour = 11
t.minute = 34
t.second = 33

Time.time_int(t)


# it is probably not appropriate to rewrite int_to_time as a method;
# what object you would invoke it on?

# Because int_to_time already has the object within the function.
