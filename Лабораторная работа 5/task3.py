from random import randint

def get_unique_list_numbers() -> list[int]:

    list_of_values = []
    while len(list_of_values) < 15:
        num = randint(-10, 10)
        if num not in list_of_values:
            list_of_values.append(num)
    return list_of_values

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
# перенос строки
