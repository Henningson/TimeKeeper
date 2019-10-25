import datetime
import time
import sys
# Basic TimeKeeper-Class for stopping and returning at specific times


class TimeKeeper:
    def __init__(self, stopping_time, returning_time):
        self.stopping_time = stopping_time if isinstance(stopping_time, datetime.time) else datetime.time(stopping_time, 0)
        self.returning_time = returning_time if isinstance(returning_time, datetime.time) else datetime.time(returning_time, 0)

    def set_stopping_time(self, stopping_time):
        self.stopping_time = stopping_time

    def set_returning_time(self, returning_time):
        self.returning_time = returning_time

    def check_time(self):
        return self.get_current_time() >= self.stopping_time

    def wait(self):
        if self.get_current_time() >= self.stopping_time:
            print("Stopping time exceeded. Stopping until " + str(self.returning_time))
            timedelta = datetime.datetime.combine(datetime.date.min, self.returning_time) - datetime.datetime.combine(datetime.date.min, self.get_current_time())
            print("Sleeping for " + str(timedelta.total_seconds()))
            sys.stdout.flush()
            time.sleep(timedelta.total_seconds())

        print("Returning the process")

    def get_current_time(self):
        return datetime.datetime.now().time()
