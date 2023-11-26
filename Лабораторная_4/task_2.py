# TODO импортировать необходимые молули

import json
import csv


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, encoding="utf8") as src_file:
        lines = [line_ for line_ in csv.DictReader(src_file)]  # TODO считать содержимое csv файла

        with open(OUTPUT_FILENAME, "w", encoding="utf8") as dir_file:

            return json.dump(lines, dir_file, indent=4, ensure_ascii=False)  # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
