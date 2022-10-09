# Задача №1
# Дана довільна строка. Напишіть код, який знайде в ній і віведе на екран кількість слів,
# які містять дві голосні літери підряд.

user_input = input("Enter a string with words: ")

result = user_input.split()

consonant_list =['o', 'y', 'i', 'a', 'u', 'e']

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

print("In your sentence " + str(word_count) + " words with vowels in a row.")

# Задача №2
# Є два довільних числа які відповідають за мінімальну і максимальну ціну.
# Є Dict з назвами магазинів і цінами:
# { "cito": 47.999, "BB_studio" 42.999, "momo": 49.999, "main-service": 37.245, "buy.now": 38.324,
# "x-store": 37.166, "the_partner": 38.988, "store": 37.720, "rozetka": 38.003}.
# Напишіть код, який знайде і виведе на екран назви магазинів, ціни яких попадають
# в діапазон між мінімальною і максимальною ціною. Наприклад:
#lower_limit = 35.9
#upper_limit = 37.339
#> match: "x-store", "main-service"

upper_limit = float(input("Enter the maximum price: "))

lower_limit = float(input("Enter the minimum price: "))


catalog = {
    "cito": 47.999,
    "BB_studio": 42.999,
    "momo": 49.999,
    "main-service": 37.245,
    "buy.now": 38.324,
    "x-store": 37.166,
    "the_partner": 38.988,
    "store": 37.720,
    "rozetka": 38.003,
}

for key, value in catalog.items():
    if lower_limit < value < upper_limit:
        print('The store that suits you: ', key)
    elif value < lower_limit:
        print('Sorry, there is no store that suits you in the list')

