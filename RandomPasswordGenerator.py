import random


def shuffle(string):
    templist = list(string)
    random.shuffle(templist)
    print("Your password is: " + ''.join(templist))


def passwordgenerator(upper, lower, number, choice):
    templist = list()
    i, j, k = 0, 0, 0
    while i < upper:
        templist.append(chr(random.randint(65,90)))
        i += 1
    while j < lower:
        templist.append(chr(random.randint(97, 122)))
        j += 1
    while k < number:
        templist.append(chr(random.randint(48, 57)))
        k += 1
    if choice == "Y" or choice == "y":
        shuffle(templist)
    else:
        print("Your password is: " + ''.join(templist))


if __name__ == "__main__":
    print('')
    print("Enter the number of upper case letters you want in your password:")
    upper = int(input())
    print("Enter the number of lower case letters you want in your password:")
    lower = int(input())
    print("Enter the number of numbers you want in your password:")
    number = int(input())
    print("Do you want the order randomized? Y or N")
    choice = input()
    passwordgenerator(upper, lower, number, choice)
