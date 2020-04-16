#Assigning elements to lists.
list1=[]
list2=[]

lno=int(input("Which list do you want to add elements to (List 1 or List 2):\n"))

if lno == 1:
    n=int(input("Enter number of elements you want to add in the list:\n"))
    for i in range (0,n1):
        index=int(input("Enter the index you want to insert your element at:\n"))
        element=int(input())
        list1.insert(index,element)

if lno == 2:
    n2=int(input("Enter number of elements you want to add in the list:\n"))
    for i in range (0,n2):
        index=int(input("Enter the index you want to insert your element at:\n"))
        element=int(input())
        list2.insert(index,element)

print(list1)
print(list2)
