#Sum/Average Program
#Your first and last name:
#Your student ID:

#Build on what you did in the 'List of Names' program
#Instead of entering 10 names, enter 20 numbers
#Instead of searching for a name in the list
#   Compute the sum of all 10 numbers
#   Compute the average for all 10 numbers

#Enter a number:
#The sum of the numbers you entered is:
#The average of the numbers you entered is:


numberList = []
sumInt = 0
avgInt = 0.0

for x in range(0,20):
    num = int(input("Enter a number"))
    numberList.append(num)

print(numberList)

#for loop to sum/average 20 numbers
for x in range (0,20):
    sumInt=sumInt + numberList [x]
print("the sum is ", sumInt)
