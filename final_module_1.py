user_name = input("Введитесвое свое ФИО")
user_age =int(input("Введитесвой год своего рождения"))
from datetime import datetime #Из модуля datetime импортируй класс datetime"
current_year = datetime.now().year #присваиваем current_year текущий год
age = current_year - user_age #выесням возраст пользователя
parts =user_name.split(" ")
first_name = parts[0]
last_name = parts[1]
last_letter = last_name[-1]
print("Привет",last_name,first_name,"!")
if age >=18:
    print("Вы совершеннолетний. Доступ к управлению авто разрешен.")
else: print("Вы не совершеннолетний. Доступ к управлению авто не разрешен.")
if last_letter == "а":
    print("Женский род")
else: print("Мужской род")