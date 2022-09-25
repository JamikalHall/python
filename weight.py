#a simple weight conversion program that takes a weight from the user, asks for lbs or kilograms, then converts that weight to the option either lbs or kgs depending on user choice.

userWeight = input("Weight: ")
poundsOrKilos = input("(L)bs or (K)gs: ")

if poundsOrKilos.upper() == "L" :
    print("Your weight is " + str(int(userWeight) / 2.205) + " kgs.")
elif poundsOrKilos.upper() == "K":
    print("Your weight is " + str(int(userWeight) * 2.205) + " lbs.")