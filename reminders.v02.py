import datetime

# now.hour = int(input("What hour is it? (0-23)"))

now = datetime.datetime.now()
print(now.year, now.month, now.day, now.hour, now.minute, now.second)

if now.hour <= 5:
    print("it's early you shuld be sleeping!")
elif now.hour <= 7:
    print("Wake up, brew that cofee, get that mile run, and get that breakfast ...")
elif now.hour <= 9:
    print("Time to go to work.")
elif now.hour <= 12:
    print("You should be working")
elif now.hour <= 13:
    print("Take your lunch break")
elif now.hour <= 17:
    print("Do you feel that afternoon lull?")
elif now.hour <= 19:
    print("Time to hit the gym")
elif now.hour <= 21:
    print("Gotta eat that dinner")
elif now.hour <= 23:
    print("Get that sLEEP. and rePEAT!")
else:
    print("you didnt type an acceptable value! (0-23)")
    
