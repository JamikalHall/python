#write a program that takes in a number and returns it in plain English

phones = {
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
    "5" : "five",
    "6" : "six",
    "7" : "seven",
    "8" : "eight",
    "9" : "nine"
}
output = ""
inputNumber = input('Please enter a phone number: ')

for character in inputNumber:
    output += phones.get(character, "!") + " "
print(output)

