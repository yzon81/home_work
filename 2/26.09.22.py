# Напишіть программу "Касир в кінотеватрі", яка буде виконувати наступне:
# Попросіть користувача ввести свсвій вік (можно використати константу або input()).
# - якщо користувачу менше 7 - вивести повідомлення"Де твої батьки?"
# - якщо користувачу менше 16 - вивести повідомлення "Це фільм для дорослих!"
# - якщо користувачу більше 65 - вивести повідомлення"Покажіть пенсійне посвідчення!"
# - якщо вік користувача містить цифру 7 - вивести повідомлення "Вам сьогодні пощастить!"
# - у будь-якому іншому випадку - вивести повідомлення "А білетів вже немає!"
# P.S. На екран має бути виведено лише одне повідомлення, якщо вік користувача містить цифру 7
# то має бути виведено тільки відповідне повідомлення! Також подумайте над варіантами, коли введені невірні дані.


while True:
    user_age = int(input('Скільки тобі років?: '))
    if user_age <= 4 or user_age >= 80:
        print("Введіть правильні дані")
        continue
    break

if '7' in str(user_age):
    print('Вам сьогодні пощастить!')
elif user_age < 7:
    print('Де твої батьки?')
elif user_age < 16:
    print('Це фільм для дорослих!')
elif user_age > 65:
    print('Покажіть пенсійне посвідчення!')
else:
    print('А білетів вже немає!')