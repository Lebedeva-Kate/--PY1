from random import sample

def get_random_password() -> str:
    alfavit = 'ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz0123456789'
    list_of_password = sample(alfavit, 8)
    return "".join(list_of_password)

print(get_random_password())
# перенос строки
