from datetime import datetime

d=int(input("Podaj dzień: "))
m=int(input("Podaj miesiąc: "))
y=int(input("Podaj rok: "))
print ("Do dzisiaj minęło: ")
print(datetime.today() - datetime(y,m,d))

#days=abs(today-datatime.data)



