from datetime import datetime
import time

class Stopwatch:
    # Initialize
    def __init__(self):
        self.state = False
        self.startTime = None
        self.endTime = None
    # Define Start
    def start(self):
        self.state = True
        self.startTime = datetime.utcnow()
    # Define End
    def stop(self):
        if self.state:
            self.state = False
            self.endTime = datetime.utcnow()
   # Define finding elapsed time
    def getElapsedTime(self):
        # if no result, return 0
        if not self.state and self.endTime is None:
            return 0
        # if no result, return time
        if self.state and self.endTime is None:
            return int((datetime.utcnow() - self.startTime).total_seconds())
        else:
            return int((self.endTime - self.startTime).total_seconds())

# Get s Variable
s = Stopwatch()
print('Elapsed time before start:', s.getElapsedTime())

# Sleep by 1
time.sleep(1)

# Run Timer
s.start()
print('Starting now')

time.sleep(2)

print('Elapsed time after start:', s.getElapsedTime())

time.sleep(2)

#End Timer
s.stop()
print('Stopping now')

time.sleep(2)

#Print Result
print('Elapsed time after stopping:', s.getElapsedTime())
