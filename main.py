print("Welcome to the GC Fruit Market!")
name = input("What is your name? ")
print()

print("Welcome "+name)
print("Which Fruit would you like to buy? ")
print("1. Apple $2 ")
print("2. Grape $1 ")
print("3. Orange $3 ")
apples = 0
grapes = 0
oranges = 0
fruits = input(" > ")

if int(fruits) == 1:
    apples += 1
    print("1. You bought 1 Apple at $2 ")
elif int(fruits) == 2:
    grapes += 1
    print("2. You bought 1 Grape at $1 ")
elif int(fruits) == 3:
    oranges += 1
    print("3. You bought 1 Orange at $3 ")


while True:
    print("Would you like to buy another piece of fruit? y/n ")
    y_n = input(" > ")
    if y_n == "n":
        print("Thank you for your order! Have a nice day!")
        break
    print()

    print("Welcome "+name + " Which Fruit would you like to buy? ")
    print("1. Apple $2 ")
    print("2. Grape $1 ")
    print("3. Orange $3")

    fruits = input(" > ")

    if int(fruits) == 1:
        print("1. You bought 1 Apple at $2 ")
        apples += 1
    elif int(fruits) == 2:
        print("2. You bought 1 Grape at $1 ")
        grapes += 1
    elif int(fruits) == 3:
        print("3. You bought 1 Orange at $3 ")
        oranges += 1
print("----------RECEIPT----------")
print("Order for " + name)
print("Apple(s) at $2 a piece: " + str(apples))
print("Grape(s) at $1 a piece: " + str(grapes))
print("Orange(s) at $3 a piece: " + str(oranges))

apples_at_piece = apples * 2
grapes_at_piece = grapes * 1
oranges_at_piece = oranges * 3

print()
subtotal = float(apples_at_piece+grapes_at_piece+oranges_at_piece)
print("Sub Total; ${:.2f}".format(subtotal))


tax = 0.05 * subtotal
print("5% Tax: ${:.2f}".format(tax))

total = subtotal + tax
print("Total: ${:.2f}".format(total))









