#write a program to find the largest number in a list

largestNumber = [1, 32, 2, 554, 12] #we expect this to return 554
comparison = largestNumber[0]

for index in largestNumber: #we need to iterate through list
    if index > comparison:
        comparison = index #if the index of the list is larger than our number, then we save it. otherwise, we ignore

print(f"{comparison}")
