# 1) Multiples of 3 and 5   2) Convert a day number of the year to a Persian (Solar Hijri) month and day

n = float(input("Enter a number: "))

if (n % 3 == 0) and (n % 5 == 0):
    print("Multiple of 3 and 5")
elif n % 3 == 0:
    print("Multiple of 3")  
elif n % 5 == 0:
    print("Multiple of 5")     
else:
    print("try again!")     



print("---------------")    



day = int(input("Enter day number (1-366): "))

if 1 <= day <= 31:
    print(day, "Farvardin")

elif 32 <= day <= 62:
    print(day - 31, "Ordibehesht")

elif 63 <= day <= 93:
    print(day - 62, "Khordad")

elif 94 <= day <= 124:
    print(day - 93, "Tir")

elif 125 <= day <= 155:
    print(day - 124, "Mordad")

elif 156 <= day <= 186:
    print(day - 155, "Shahrivar")

elif 187 <= day <= 216:
    print(day - 186, "Mehr")

elif 217 <= day <= 246:
    print(day - 216, "Aban")

elif 247 <= day <= 276:
    print(day - 246, "Azar")

elif 277 <= day <= 306:
    print(day - 276, "Dey")

elif 307 <= day <= 336:
    print(day - 306, "Bahman")

elif 337 <= day <= 366:
    print(day - 336, "Esfand")

else:
    print("Invalid day")

    