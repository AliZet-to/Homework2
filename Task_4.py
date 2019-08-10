#Data input
day_number = int(input("Please input the day's number (1..7) \n"))

#Calculation workflow
if day_number == 1:
    print("Mon: Week start. Meeting with a Client.")
elif day_number == 2:
    print("Tue: Business trip to Amsterdam")
elif day_number == 3:
    print("Wed: Paper work")
elif day_number == 4:
    print("Thu: Report preparation")
elif day_number == 5:
    print("Fri: Week's finish. Retrospective.")
elif day_number == 6 or day_number == 7:
    print("Sat and Sun: Week-end.")
else:
    print("Day is not exist.")