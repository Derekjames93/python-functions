def sleep_or_work(day):
# Make sure it's a number between 0 and
    # If it's day 0 or day 6 ... sleep in!
    if day == 0 or day == 6:
        return "Sleep in"
    else:
        return "Go to work"
# This is an arbitrary Infinite loop
while True:
    # Get the day from the user
    day = int(input("Day (0-6)?"))
    message = sleep_or_work(day)
    print(message)