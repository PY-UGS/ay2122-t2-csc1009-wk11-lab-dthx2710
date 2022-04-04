class ClockTime:
    # initialize attributes to 0 by default
    hours = 0
    minutes = 0
    seconds = 0

    def setHours(self, hours):  # set hour
        self.hours = hours

    def setMins(self, minutes):  # set minutes
        self.minutes = minutes

    def setSeconds(self, seconds):  # set seconds
        self.seconds = seconds

    def setTime(self, hours, minutes, seconds):  # set hour, minutes and seconds
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def showTime(self):  # hours:minutes:seconds
        print("The set time is: " + str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds))


newClock = ClockTime()

while True:
    try:
        hour = int(input("Enter hour in 24h format (0-23): "))
        if hour >= 0 and hour <= 23:  # hours (0-23)
            break
        print("Wrong Format")
    except Exception as e:
        print(e)

while True:
    try:
        minutes = int(input("Enter minutes in 24h format (0-59): "))
        if minutes >= 0 and minutes <= 59:  # minutes (0-59)
            break
        print("Wrong Format")
    except Exception as e:
        print(e)

while True:
    try:
        seconds = int(input("Enter seconds in 24h format (0-59): "))
        if seconds >= 0 and seconds <= 59:  # seconds (0-59)
            break
        print("Wrong Format")
    except Exception as e:
        print(e)

newClock.setTime(hours, minutes, seconds)
newClock.showTime()
