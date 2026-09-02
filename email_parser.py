
user_mail = input("Введите свою электронную почту")
parts = user_mail.split("@")
print("логин",parts[0])
print("домен",parts[1])
login = parts[0]
domen = parts[1]
if "." in login:
    print("В логине содержится точка!")
else:
    print("Влогине нету точки!")