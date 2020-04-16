f0=0
f1=1
sum=0
terms=int(input("Enter the number of terms you want in the Fibonacci Series to be printed:\n"))
count=0
print("The Fibonacci Series is: \n")
print("0\n1")
while count < terms:
    sum=f0+f1
    f0=f1
    f1=sum
    print(sum)
    count += 1
