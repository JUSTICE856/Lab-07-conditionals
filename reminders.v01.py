usertime = int(input("What hour is it? (0-23)"))

if usertime <= 5:
    print("it's early you shuld be sleeping!")
elif usertime <= 7:
    print("Wake up, brew that cofee, get that mile run, and get that breakfast ...")
elif usertime <= 9:
    print("Time to go to work.")
elif usertime <= 12:
    print("You should be working")
elif usertime <= 13:
    print("Take your lunch break")
elif usertime <= 17:
    print("Do you feel that afternoon lull?")
elif usertime <= 19:
    print("Time to hit the gym")
elif usertime <= 21:
    print("Gotta eat that dinner")
elif usertime <= 23:
    print("Get that sLEEP. and rePEAT!")
else:
    print("you didnt type an acceptable value! (0-23)")
    
