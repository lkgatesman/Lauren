#Lauren Gatesman
#Assignment 3, Problem 3
#Due September 26, 2019
#Class Section: 009

#Print the instructions

print("Intructions: Enter the start date and birthdate for an employee to determine their age at the start.")

#Prompt user for start date of show and birth date

startdate = int(input("Enter start date MMDDYYYY: "))

birthdate = int(input("Enter birth date MMDDYYYY: "))

#Extract the year from the birthdate entered

year = int(birthdate % 10000)


#Extract the month and day from the birthdate entered

MMDD = int(birthdate / 10000)


#Extract the day from the MMDD variable

DD = int(MMDD % 100)

#Extract the month from the MMDD variable

MM = int(MMDD / 100)

#Assign a month word to the MM variable

if MM == 1:
    monthword = 'January'
if MM == 2:
    monthword = 'February'
if MM == 3:
    monthword = 'March'
if MM == 4:
    monthword = 'April'
if MM == 5:
    monthword = 'May'
if MM == 6:
    monthword = 'June'
if MM == 7:
    monthword = 'July'
if MM == 8:
    monthword = 'August'
if MM == 9:
    monthword = 'September'
if MM == 10:
    monthword = 'October'
if MM == 11:
    monthword = 'November'
if MM == 12:
    monthword = 'December'

#Assign an ending to the DD variable (1st, 2nd, etc)

if DD == 1 or DD == 21 or DD == 31:
    dayword = str(DD) + 'st'

elif DD == 2 or DD == 22:
    dayword = str(DD) + 'nd'

elif DD == 3 or DD == 23:
    dayword = str(DD) + 'rd'

else:
    dayword = str(DD) + 'th'

print("The contestant was born on " + monthword + " " + dayword + ", " + str(year) + ".")

#Extract the year and month/day from the startdate of the show

showyear = int(startdate % 10000)

showMMDD = int(startdate / 10000)

#Determine if contestant will be older than 21, 21, or less than 21 and print out whether they are eligible to compete in the show

if (showyear - year) > 21:
    print("ELIGIBLE: The contestant will be 21 by the time taping begins.")

#Now determine if the contestant is 21 years old exactly or less than 21 years old and print out their eligibility

elif (showyear - year) == 21:
    if showMMDD > MMDD:
        print("NOT ELIGIBLE: The contestant will not be 21 by the time taping begins.")

else:
    print("NOT ELIGIBLE: The contestant will not be 21 by the time taping begins.")

