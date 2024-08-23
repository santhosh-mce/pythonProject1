print("A = 1, 3, 5, 7, 9")
print("B = 2, 3, 6, 7, 10 ")
print("C = 4, 7, 5, 6")
print("D = 8, 9, 10")

m = input("Enter your choice: ")

if m.upper() == "A":
    print("you guess number is 1")
elif m.upper() == "B":
    print("you guess number is 2")
elif m.upper() == "AB":
    print("you guess number is 3")
elif m.upper() == "BA":
    print("you guess number is 3")
elif m.upper() == "C":
    print("you guess number is 4")
elif m.upper() == "AC":
    print("you guess number is 5")
elif m.upper() == "CA":
    print("you guess number is 5")
elif m.upper() == "BC":
    print("you guess number is 6")
elif m.upper() == "CB":
    print("you guess number is 6")
elif m.upper() == "ABC":
    print("you guess number is 7")
elif m.upper() == "ACB":
    print("you guess number is 7")
elif m.upper() == "BAC":
    print("you guess number is 7")
elif m.upper() == "BCA":
    print("you guess number is 7")
elif m.upper() == "CAB":
    print("you guess number is 7")
elif m.upper() == "CBA":
    print("you guess number is 7")
elif m.upper() == "D":
    print("you guess number is 8")
elif m.upper() == "D":
    print("you guess number is 8")
elif m.upper() == "DA":
    print("you guess number is 9")
elif m.upper() == "AD":
    print("you guess number is 9")
elif m.upper() == "DB":
    print("you guess number is 10")
elif m.upper() == "BD":
    print("you guess number is 10")
else:
    print("you NOT guess any number ")

