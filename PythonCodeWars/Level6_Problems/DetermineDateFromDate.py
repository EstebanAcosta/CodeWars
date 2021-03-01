#Author:Esteban Acosta
# What date corresponds to the nth day of the year?
# The answer depends on whether the year is a leap year or not.

# Write a function that will help you determine the date if you know the number of the day in the year, as well as whether the year is a leap year or not.
# The function accepts the day number and a boolean value isLeap as arguments, and returns the corresponding date of the year as a string "Month, day".
# Only valid combinations of a day number and isLeap will be tested.

def get_day(day, is_leap): 
    daysInMonths = {"January" : 31,
                    "February" : [28,29],
                    "March" : 31,
                    "April" : 30,
                    "May" : 31,
                    "June" : 30,
                    "July" : 31,
                    "August" : 31,
                    "September" : 30,
                    "October" : 31,
                    "November" : 30,
                    "December":31
                   }
    m = ""
    #loop through the dictionary of months 
    for month in daysInMonths:
        #get the number of days associated with that month
        days = daysInMonths.get(month)
        #if it's a leap year and it's february
        if month == "February" and is_leap == True:
            #store the second element of the list (2nd elmnt = 29 days)
            days = daysInMonths.get(month)[1]
        #if it's not a leap year and it's february
        elif month == "February" and is_leap == False:
            #store the first element of the list (1st elmnt = 28 days)
            days = daysInMonths.get(month)[0]
        #if the day is less than or equal to the days of that month
        if day <= days:
            #store the name of the month
            m = month
            #and break out of the loop
            break
        #if the day is more than the number of days in the month
        #subtract the # of days in that month from the day
        else:
            day-=days
    #return a string representation of month followed by a comma followed by the day    
    return m + ", " + str(day)
