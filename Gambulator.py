
'''***********************************************************************************************
        Create an application which asks the user for an input for a maths mark, a chemistry mark and a physics mark.
        Add the marks together, then work out the overall percentage. And print it out to the screen.
        If the percentage is below 40%, print “You failed”
        If the percentage is 40% or higher, print “D”
        If the percentage is 50% or higher, print “C”
        If the percentage is 60% or higher, print “B”
        If the percentage is 70% or higher, print “A”
***********************************************************************************************'''
import option as option

print('Welcome to Grade Calculator')
print()
print("Please enter your maths mark:")
maths_mark = int(input())
print("Please enter your chemistry mark:")
chemistry_mark = int(input())
print("Please enter your physics mark:")
physics_mark = int(input())
total_mark = maths_mark + chemistry_mark + physics_mark
print('Here is the total mark : ', total_mark)
print()
percentage_mark: int = int(total_mark / 3)
print('Here is the Percentage mark : ', percentage_mark)
print()

if percentage_mark >= 70:
    print('you are granted a A')
elif percentage_mark >= 60:
    print('You are granted a B')
elif percentage_mark >= 50:
    print('You are granted a C')
elif percentage_mark >= 40:
    print('D')
else:
    print('You suck')



