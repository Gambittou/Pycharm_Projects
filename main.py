# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
string_a = "Derrick"
# print("The length of this string is = ", len(string_a))
print("The first from the right element in this string is = ", string_a[-1])
print("this string in upper case looks like ", string_a.upper())
counter = string_a.count("")
print(counter)
print("This string converted to lower case looks like this = ", string_a.lower())
string_b = "Derrick, Matt, Jessica"
print("string b, however looks like = ", string_b)
# I have split string_b by the commas and put the bits into string_c
string_c = string_b.split(",")
print("If we split string b up by the comma, it becomes three individual elements = ", string_c)
print(string_c[1], "is the 2nd name located in string b, also know as string_c and is type : - "
      , type(string_c), "and has",  len(string_c), "elements")