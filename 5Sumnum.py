#Create a function that takes an integer n as input and returns the sum of all numbers from 1 to n

def sum(n):
    sum = 0
    for i in range(1,n+1,1):
        sum = sum + i
    return sum

n = int(input("Enter the number : "))
print("Sum = ",sum(n))