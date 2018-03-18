__author__ = 'student'
print('Hello world')
a = "Welcome to Python's world!"
b = 'Welcome to Python\'s world!'
print(a[0])
print(a[0:7])
print(b)
a = input("wprowadz coś: ")
g = float(5)
print("ffff" + a)
#if a == 5.0:
#    print('pierwsze')
#else:
#    if a == 9.0 or a== 8.0:
#        print('drugie')
#    else:
#        print('trzecie')
#print('koniec')

num=12
if num == 5.0:
    print("to jest 5")
elif num == 10:
     print("to jest 10")
elif num == 15:
     print("to jest 15")
else:
    print("To nie jest : 5, 10, 15")

i=1
while i<=5:
    print(i)
    i+=1
print("Koniec")

words=["hello","world","spam","eggs"]

for word in words:
    print(word +"!")