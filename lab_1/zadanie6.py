print ("Witaj użytkowniku!")
print ("Możliwe działania\n"
       " + dodawanie\n"
       " - odejmowanie\n"
       " / dzielenie\n"
       " * mnożenie\n"
       " ^ potęgowanie\n"
       " q kończy działanie programu")
switch=True
while(switch):
    a=input("Wprowadz pierwszą liczbę: ") #zabezpieczyć przed pustym
    operation=input("Wybierz działanie: ")

    if operation == "+":
        b=float(input("Wprowadz drugą liczbę: "))
        print (a+b)

    elif operation == "-":
        b=float(input("Wprowadz drugą liczbę: "))
        print (a-b)

    elif operation == "/":
        b=float(input("Wprowadz drugą liczbę: "))
        print (a/b)

    elif operation == "*":
        b=float(input("Wprowadz drugą liczbę: "))
        print (a*b)

    elif operation == "^":
        b=float(input("Wprowadz drugą liczbę: "))
        print (a**b)
    elif operation == ":q":
        switch=False
    else:
        print ("Nie rozpoznano operatora! Powtórz operacje")