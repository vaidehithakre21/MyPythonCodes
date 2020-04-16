#Deleting different Dictionary elements:
dict1={1: 'I', 2: 'Love', 3: 'AI', 4: 'And', 5: 'ML'}
print(dict1)

key=int(input("Enter the key you want to delete:\n"))
del dict1[key]
print(dict1)

#To print entire dictionary, we can use:
#del dict1
#print(dict1)
