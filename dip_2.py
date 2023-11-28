Name=input("Enter your name:")
phone=int(input("enter your phone number:"))
email=input("enter your email:")
# objective
objective=input("Enter your objective:")
# qualifications
qualifications=[]
totalSize=int(input("Enter total degrees:"))
for i in range(totalSize):
degree = input("Enter your degree: ")
instituteName = input("Enter Institute Name: ")
year = input("Enter the year of completion: ")
score = input("Enter CGPA/Percentage: ")
qualifications.append({
"degree": degree,
"Institute-Name": instituteName,
"year": year,
"CGPA/Percentage": score
})
# skills
skills = input("Enter your skills separated by commas: ").split(',')
skills = [skill.strip() for skill in skills]
# projects
projects = []
num_projects = int(input("Enter the number of projects: "))
for _ in range(num_projects):
project_title = input("Enter the project title: ")
description = input("Enter a brief description of the project: ")
link = input("Enter the link to the project (if applicable): ")
projects.append({
"project_title":project_title,
"description":description,
"link":link
})
experiences=[]
totalExperiences=int(input("Enter total experience entry:"))
for i in range(totalExperiences):

title:input("enter the title:")
companyName:input("enter the company name:")
duration=input("enter total duration")
experiences.append({
"title":title,
"companyName":companyName,
"duration":duration
})
interest=[]
totalInterestEntries=int(input("Enter total interest entries:"))
for i in range(totalInterestEntries):
interestName:input("enter the interestName:")
experiences.append({
"interestName":interestName
})
print("-------------------:My CV:-------------------")
print(Name)
print("phone:",phone," ","Email:",email)
print("Objective:",objective)
print("-------------------:Qualifications:-------------------")
for edu in qualifications:
print(edu["degree"] + " - " + edu["Institute-Name"] + " (" + edu["year"] + ")")
print("CGPA/Percentage:", edu["CGPA/Percentage"])
print("-------------------:Projects:-------------------")
for project in projects:
print(project["project_title"]+" - "+project["link"])
print("Project summery:",project["description"])
print("-------------------:Experiences:-------------------")
for exper in experiences:
print("Title:",exper["title"]+" - "+exper["duration"])
print("Company Name:",exper["companyName"])
print("-------------------:Interest:-------------------")
for interes in interest:
print(interes["interestName"])
Q2. Write a program that takes the month (1...12) as input. Print whether the season is
summer,winter, spring or autumn depending upon the input month.
Ans- month_name = input("Enter a month name: ")
seasons = {
'1': 'Winter',
'2': 'Winter',
'3': 'Winter',
'4': 'Spring',
'5': 'Spring',
'6': 'Spring',
'7': 'Summer',
'8': 'Summer',
'9': 'Summer',
'10': 'autumn',
'11': 'autumn',
'12': 'autumn'
}
# Check if the entered month name is valid
if month_name in seasons:
season = seasons[month_name]
print("The season for", month_name.capitalize(), "is", season)
else:
print("Invalid month name. Please enter a valid month.")
Output- Enter a month name: 5
The season for 5 is Spring
Q3. Write a python program to check whether a year is leap year or not.
Ans- year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
print(year, "is a leap year")
else:
print(year, "is not a leap year")
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
print(year, "is a leap year")
else:
print(year, "is not a leap year")
Output- Enter a year: 1900
1900 is not a leap year
Q4. Write a program that takes a sentence as input. Compute the frequency of each
words and prints them.
Ans- sentence = input("Enter a sentence: ")
words = sentence.split()
word_frequency = {}
for word in words:
clean_word = word.strip(".,!?").lower()
if clean_word in word_frequency:
word_frequency[clean_word] += 1
else:
word_frequency[clean_word] = 1
print("Word frequencies:")
for word, frequency in word_frequency.items():
print(f"{word}: {frequency}")
Output- Enter a sentence: India India aus india
Word frequencies:
india: 3
aus: 1
Lab 2
Q1. Write a program to generate a dictionary that contains (i,sqrt(i)), where i is an
integer between 1 and n. n is a number input by the user.
Ans- import math
def generate_sqrt_dictionary(n):
sqrt_dict = {}
for i in range(1, n + 1):
sqrt_dict[i] = math.sqrt(i)
return sqrt_dict
def main():
n = int(input("Enter a value for n: "))
sqrt_dict = generate_sqrt_dictionary(n)
print("Generated dictionary:", sqrt_dict)
if __name__ == "__main__":
main()
Output- Enter a value for n: 10 Generated dictionary: {1: 1.0, 2: 1.4142135623730951, 3:
1.7320508075688772, 4: 2.0, 5: 2.23606797749979, 6: 2.449489742783178, 7:
2.6457513110645907, 8: 2.8284271247461903, 9: 3.0, 10: 3.1622776601683795}
Q2. Write a simple calculator program using functions add, sub, mul and div. The
program should accepts two numbers and an operator and calls the corresponding
function to perform the operation.
Ans- num1=int(input("Enter the first number="))
num2=int(input("Enter the second number="))
operator=input("Enter the operator=")
def calculator(num1,num2,operator):
if(operator=="+"):
print("Addition result:",num1+num2)
elif(operator=="-"):
print("Substraction result:",num1-num2)
elif(operator=="-"):
print("Multiplication result:",num1*num2)
elif(operator=='/'):
print("Division result:",num1/num2)
else:
print("wrong operator selection")
calculator(num1,num2,operator)
Output- Enter the first number=4
Enter the second number=5
Enter the operator=+
Addition result: 9
Q3. Write a function that generates a list with values that are square of number
between 1 and 20.
Ans- def generate_square_list():
square_list = [x ** 2 for x in range(1, 21)]
return square_list
squares = generate_square_list()
print(squares)
Output- [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]
Q4. Using recursion, write a program to calculate the reverse of a string
Ans- def reverse_string(s):
if len(s) == 0:
return ""
else:
return s[-1] + reverse_string(s[:-1])
input_string = input("Enter a string: ")
reversed_string = reverse_string(input_string)
print("Reversed string:", reversed_string)
Output- Enter a string: Uiet Kanpur
Reversed string: rupnaK teiU
Lab 3
Ans-1 import numpy as np
# Create an array of shape (2, 3, 4) of zeros
array_zeros = np.zeros((2, 3, 4))
# Create an array of shape (2, 3, 4) of ones
array_ones = np.ones((2, 3, 4))
# Create an array with values 0 to 999 using the "arange" function
array_range = np.arange(1000)
# Create an array from the list [12, 32, 5.5, -6.4, -2.2, 2.4] and assign it to the variable "a"
a = np.array([2, 3.2, 5.5, -6.4, -2.2, 2.4])
# Printing the value of a[4]
print(a[1:4]) # It will print -22.24
# Print the array a
print(a)
# Create a 2-D array from the provided list
array_2d = np.array([[2, 3.2, 5.5, -6.4, -22, 2.4],
[1, 22, 4, 0.1, 5.3, -9],
[3, 1, 2.1, 21, 1.1, -2]])
# Printing slices
print(array_2d[:, 3]) # Print a[:,3]
print(array_2d[1:4, 0:4]) # Print a[1:4, 0:4]
print(array_2d[1:, 2]) # Print a[1, 2]
# Create a 2-D array of shape (2, 4) containing two lists
array_2d_lists = np.array([list(range(4)), list(range(10, 14))])
# Print the shape of the array
print(array_2d_lists.shape)
# Print the size of the array
print(array_2d_lists.size)
# Print the maximum and minimum of the array
print(np.max(array_2d_lists))
print(np.min(array_2d_lists))
# Reshape the array to (2, 2, 2)
reshaped_array = np.reshape(array_2d_lists, (2, 2, 2))
# Print the transposed array
print(np.transpose(array_2d_lists))
# Print the flattened array
print(array_2d_lists.flatten())
# Convert the array to floats
array_floats = array_2d_lists.astype(float)
# Create an array counting from 1 to 20 inclusive
array_counting = np.arange(1, 21)
# Create an array of multiples of 3 greater than and less than 30
array_multiples_of_3 = np.arange(3, 30, 3)
# Create an array of equally spaced floats from 0 to 1
array_floats = np.linspace(0, 1, num=12)
# Use the "np.eye" function to create the array A
array_a = np.eye(3, k=1) + np.eye(3, k=-1)
# Use broadcasting to create the array AB
array_b = np.array([1, 2, 3])
array_ab = array_a + array_b[:, np.newaxis]
# Print the arrays
print(array_a)
print(array_b)
print(array_ab)
Output- [ 3.2 5.5 -6.4]
[ 2. 3.2 5.5 -6.4 -2.2 2.4]
[-6.4 0.1 21. ]
[[ 1. 22. 4. 0.1]
[ 3. 1. 2.1 21. ]]
[4. 2.1]
(2, 4)
8
13
0
[[ 0 10]
[ 1 11]
[ 2 12]
[ 3 13]]
[ 0 1 2 3 10 11 12 13]
[[0. 1. 0.]
[1. 0. 1.]
[0. 1. 0.]]
[1 2 3]
[[1. 2. 1.]
[3. 2. 3.]
[3. 4. 3.]]
[ ]
Ans-2 import numpy as np
# Create an array of shape (2, 3, 4) of zeros
zeros_array = np.zeros((2, 3, 4))
# Create an array of shape (2, 3, 4) of ones
ones_array = np.ones((2, 3, 4))
# Create an array with values 0 to 999 using np.arange function
arange_array = np.arange(1000)
# Create an array from the given list and assign it to the variable "a"
a = np.array([2, 3.2, 5.5, -6.4, -2.2, 2.4])
# Print a[1]
print(a[1])
# Print a[1:4]
print(a[1:4])
# Create a 2-D array from the given list and assign it to the variable "a"
a = np.array([[2, 3.2, 5.5, -6.4, -2.2, 2.4], [1, 22, 4, 0.1, 5.3, -9], [3, 1, 2.1, 21, 1.1, -2]])
# Print slices
print(a[:, 3])
print(a[1:4, 0:4])
print(a[1:, 2])
# Create a 2-D array of shape (2, 4) containing two lists and assign it to the variable "arr"
arr = np.array([list(range(4)), list(range(10, 14))])
# Print shape, size, max, and min
print(arr.shape)
print(arr.size)
print(np.max(arr))
print(np.min(arr))
# Print re-shaped array, transposed array, flattened array, and array as floats
print(arr.reshape((2, 2, 2)))
print(arr.T)
print(arr.flatten())
print(arr.astype(float))
# Create an array counting from 1 to 20 inclusive
count_array = np.arange(1, 21)
# Array of multiples of 3 greater than 0 and less than 30
multiples_of_3 = np.arange(3, 30, 3)
# Array of 8 equally spaced floats
equally_spaced_floats = np.linspace(0, 1, 8)
# Create array A and B and perform broadcasting
A = np.array([[1234], [5678]])
B = np.array([1, 2])
result = A + B
print(result)
Output- 3.2
[ 3.2 5.5 -6.4]
[-6.4 0.1 21. ]
[[ 1. 22. 4. 0.1]
[ 3. 1. 2.1 21. ]]
[4. 2.1]
(2, 4)
8
13
0
[[[ 0 1]
[ 2 3]]
[[10 11]
[12 13]]]
[[ 0 10]
[ 1 11]
[ 2 12]
[ 3 13]]
[ 0 1 2 3 10 11 12 13]
[[ 0. 1. 2. 3.]
[10. 11. 12. 13.]]
[[1235 1236]
[5679 5680]