#write a program that removes duplicates from a list

itemList = ['John', 'Carl', '34', '34' ,'John' , "Carl", "last one"]
uniques = []

#I have reconsidered how this program should work. initially i felt
#that I should try and do all the data manipulation on the intial
#array, however I have learned that I can just return a new modified list
#that has the results I am looking for

for item in itemList:
    if item not in uniques:
        uniques.append(item)

print(uniques)