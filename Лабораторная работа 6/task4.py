import json

INPUT_FILE = "input.csv"

def csv_to_list_dict(file_, delimiter=',') -> list[dict]:
    with open(file_) as f:
        list_ = []
        for line in f:
            list_.append(line.rstrip().split(delimiter))
        list_1 = list_[0]
        list_2 = list_[1:]
        fall_list = []
        for i in list_2:
            fall_list.append(dict(zip(list_1, i)))
        return fall_list

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
# перенос строки