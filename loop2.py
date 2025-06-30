str1 = input("Please enter your string: ")
str2 = ""

for i in str1:
    str2 = i + str2

print(f"Original string = {str1}\nReversed string = {str2}")