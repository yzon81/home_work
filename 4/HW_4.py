# Задача №1
# Дана довільна строка. Напишіть код, який знайде в ній і віведе на екран кількість слів,
# які містять дві голосні літери підряд.

user_input = input("Будь ласка введіть строку зі слів: ")

result = user_input.split()

consonant_list =['a', 'e', 'i', 'o', 'u', 'y']

word_count = 0

for word in result:
    counter = 0

    for letter in word:
        if letter in consonant_list:
            counter += 1
        else:
            counter = 0

        if counter == 2:
            word_count += 1
            break

print("У вашому реченні " + str(word_count) + " слів(слова) з голосними буквами підряд.")

#Задача №2
#Є два довільних числа які відповідають за мінімальну і максимальну ціну.
# Є Dict з назвами магазинів і цінами:
# { "cito": 47.999, "BB_studio" 42.999, "momo": 49.999, "main-service": 37.245, "buy.now": 38.324,
# "x-store": 37.166, "the_partner": 38.988, "store": 37.720, "rozetka": 38.003}.
# Напишіть код, який знайде і виведе на екран назви магазинів, ціни яких попадають в діапазон між
# мінімальною і максимальною ціною. Наприклад:
#lower_limit = 35.9
#upper_limit = 37.339
#> match: "x-store", "main-service"

lower_limit = input('Введіть нижню межу: ')
upper_limit = input('Введіть верхню межу: ')
shop_list_filter = list()
my_shop = {
    "cito": 47.999,
    "BB_studio": 42.999,
    "momo": 49.999,
    "main-service": 37.245,
    "buy.now": 38.324,
    "x-store": 37.166,
    "the_partner": 38.988,
    "store": 37.720,
    "rozetka": 38.003
}

try:
    lower_limit = float(lower_limit)
    upper_limit = float(upper_limit)
except ValueError:
    print('Ви ввели неправильне значення')
    exit()

for shop in my_shop.items():
    if upper_limit >= shop[1] >= lower_limit:
        shop_list_filter.append(shop[0])
print('match with :', str(shop_list_filter).replace('[', '').replace(']', ""))



