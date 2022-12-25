import json

INPUT_FILE = "input.csv"

def csv_to_list_dict(file_, delimiter=',') -> list[dict]:
    with open(file_) as f:
        list_ = []
        for line in f:
            list_.append(line.rstrip().split(delimiter))
        full_list = list(dict(zip(list_[0], i)) for i in list_[1:])
        return full_list
print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
# перенос строки
