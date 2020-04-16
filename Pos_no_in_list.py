list2=[]
n=int(input("Enter number of elements you want to add in the list:\n"))
print("Input elements:\n")
for i in range (0,n):
    element=int(input())
    list2.append(element)
print("The list is:",list2)

print("The positive numbers in the list are:\n")
for j in list2 :
    if j >= 0:
        print(j)
    
