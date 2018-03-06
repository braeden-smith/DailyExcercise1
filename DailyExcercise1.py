#Braeden Smith - Python Daily Excercise - 2/08/18

'''
1. Write a statement that concatenates at least two variables (you can have more than 2 for this practice).
use the string and integer functions, no arithmetic will be allowed for this exercise (i.e. - x*y), 
combine two variables for a string a variable. The key word here is CONCATENATE.
'''
str1 = 'Hello'
str2 = 'World'
str3 = '!'
print str1 + " " + str2 + str3 * 5

'''
2. Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old. Clue input()
'''
name = input("What is your name: ")
age = int(input("What is your age: "))
year = 100 - int(age)
year1 = int(year) + 2018
print 'In', year1,'you will be 100 years old.'
