from pprint import pprint

list_of_dicts = [dict(zip(["bin", "dec", "hex", "oct"], [bin(num), num, hex(num), oct(num)])) for num in range(16)]
pprint(list_of_dicts)
# перенос строки
