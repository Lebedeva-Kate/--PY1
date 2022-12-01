def delete(list_, index=None):
    if index == None:
        index = len(list_) - 1
    list_1 = list_[:index]
    list_2 = list_[index + 1:]
    list_change = list_1 + list_2
    return list_change

print(delete([0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
# получаем результат
