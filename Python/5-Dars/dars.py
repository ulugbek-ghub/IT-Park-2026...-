# num1 = int(input("1-Son kiriting "))
# num2 = int(input("2-Son kiriting "))
# num3 = int(input("3-Son kiriting "))

# if num1 >= num2 and num1 >= num3:
#     print(f"Eng katta son: {num1}")
# elif num2 >= num1 and num2 >= num3:
#     print(f"Eng katta son: {num2}")
# elif num3 >= num1 and num3 >= num2:
#     print(f"Eng katta son: {num3}")


# baho = int(input("Baho kiriting: "))
# if 90 <= baho <= 100:
#     print(f"{baho} - A'lo baho")
# elif 70 <= baho <= 89:
#     print(f"{baho} - Yaxshi baho")
# elif 60 <= baho <= 69:
#     print(f"{baho} - Qoniqarli baho")
# elif 0 <= baho <= 59:
#     print(f"{baho} - Qoinqarsiz baho")
# else:
#     print(f"{baho} - Notogri ball")


# yil = int(input("Yil kiriting, kabisami yoqmi: "))

# if yil % 4 == 0 and yil % 400 == 0:
#     print(f"{yil} - kabisa yili")
# else:
#     print(f"{yil} - kabisa yili emas")




# 4,5,6

# parol = "kod_123"
# if parol == "kod_123":
#     print("Xush kelibsiz")
# else:
#     print("Parol xato")

# a = 45
# b = 62
# if a<b:
#     print(f"eng katta son: {b}")
# else:
#     print(f"eng katta son: {a}")

xarid = 5000

if xarid >= 70000:
  print("Yetkazib berish bepul!")
else:
  dastavka_bilan = xarid + 15000
  qoldiq = 70000 - xarid
  print(f"Xaridingiz(dastavka bn) {dastavka_bilan} so'm.Yana {qoldiq} so'mlik xarid qilsangiz, yetkazib berish mut boladi")