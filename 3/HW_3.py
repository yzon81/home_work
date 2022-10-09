# #Задача №1
# #Зформуйте строку, яка містить певну інформацію про символ по його індексу в відомому слові.
# #Наприклад "The [індекс символу] symbol in [тут слово] is '[символ з відповідним порядковим номером]'".
# # Слово та номер отримайте за допомогою input() або скористайтеся константою. Наприклад (слово - "Python"
# # а номер символу 3) - "The 3 symbol in "Python" is 't' ".

user_word = input('Enter the word: ')
while True:
    word_idx = input('Enter symbol number: ')
    if word_idx.isdigit():
        word_idx = int(word_idx)
        if word_idx > len(user_word):
            print(f'The word \'{user_word}\' has less than {word_idx} symbols')
        else:
            print(f'The {word_idx} symbol in \'{user_word}\' is \'{user_word[word_idx - 1]}\' ')
            break
    else:
        print(f'{word_idx} is not a correct number')

# #Задача №2
# #Вести з консолі строку зі слів за допомогою input() (або скористайтеся константою).
# #Напишіть код, який визначить кількість слів, в цих даних.

text = input('Введіть речення: ')
result = len(text.split())
print('У цьому рядку ' + str(result) + ' слів')

#Задача 3
# Існує ліст з різними даними, наприклад
# lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який сформує новий list (наприклад lst2), який би містив всі числові
# змінні (int, float), які є в lst1. Майте на увазі, що данні в lst1 не є статичними можуть
# змінюватись від запуску до запуску.

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 4.85, 'Python', 9, 0, 'Lorem Ipsum', 1.1]

lst2 = []
for i in lst1:
    if type(i) == int or type(i) == float:
        lst2.append(i)
print(lst2)
