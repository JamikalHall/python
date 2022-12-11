#write a function to find the largest number in a list. it should take a list and return the largest number in that list

def find_max(list):
    compare = list[0]
    for item in list:
        if item > compare:
            compare = item
    return compare
