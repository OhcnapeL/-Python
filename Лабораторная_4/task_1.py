
import json


INPUT_FILE = "input.json"

# TODO решите задачу
def task() -> float:
    with open(INPUT_FILE) as f:
        data = json.load(f)

        return round(sum([value["score"] * value["weight"] for value in data]), 3)


print(task())
