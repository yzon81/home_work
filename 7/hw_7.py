# Задача
# Є дікт, невідомого наповнення. В дікті присутні ключі, занченням для яких є дікти невідомого наповнення в яких можуть бути аналогічні вкладені дікти. Напишіть функцію, яка дістане всі ключі зі значеннями не-діктами з усіх рівнів вкладення, помістить на один рівень в окремий дікт і поверне цей дікт.
# Напишіть докстрінг для цієї функці.

dictionary = {
    'my_dict1':
        {
            'Andrew': '18',
            'Kirill': '20',
            'Roma': '25',
            'Dima': '33',
            'my_dict2':
                {
                    'a': '19',
                    'b': '22',
                    'c': '25',
                    'd': '28',
                    'i': '30',
                    'my_dict3':
                        {
                            'Dog': '2',
                            'Cat': '3',

                        }
                }
        }

}


def foo_my_dict(elem):
    """
    Function foo_my_dict converts a multilevel dict into a single level.
    No limit on the number of levels dict
    Store keys and values that are not dict
    :param elem: my_dict
    :type: elem: dict

    :return: dict single-level
    :rtype: dict
    """
    first_level_dict = {}
    for elem in elem.items():
        if isinstance(elem[1], dict):
            first_level_dict.update(foo_my_dict(elem[1]))
        else:
            first_level_dict[elem[0]] = elem[1]
    return first_level_dict


res = foo_my_dict(dictionary)
print(res)
