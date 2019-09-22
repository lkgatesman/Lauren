#Lauren Gatesman
#Assignment 3, Problem 1
#Due September 26, 2019
#Class Section: 009

#Print title of program and ask user to input three ordered pairs
print("Valid Triangle Tester")

x1 = float(input("Enter Point #1 - x position: "))
y1 = float(input("Enter Point #1 - y position: "))
x2 = float(input("Enter Point #2 - x position: "))
y2 = float(input("Enter Point #2 - y position: "))
x3 = float(input("Enter Point #3 - x position: "))
y3 = float(input("Enter Point #3 - y position: "))
print()

#Now calculate the distance between each point (aka the length of each side of the triangle)

print('The length of each side of your test shape is:')

side1 =( (x1-x2)**2 + (y1-y2)**2 )**0.5
print('Side 1: ' + format(side1, '.2f'))

side2 =( (x2-x3)**2 + (y2-y3)**2 )**0.5
print('Side 2: ' + format(side2, '.2f'))

side3 =( (x1-x3)**2 + (y1-y3)**2 )**0.5
print('Side 3: ' + format(side3, '.2f'))

print()

#Now determine whether the points the user entered create a valid triangle
#And print out their result

if (side1 + side2) > side3:
    if (side2 + side3) > side1:
        if (side3 + side1) > side2:
            print("This is a valid triangle!")

else:
    print("This is not a valid triangle.")
    
    


           
