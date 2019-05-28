# _Python_tutorial_224_in_Hindi

from csv import DictReader

with open("file.csv", "r") as f:
    csv_reader = DictReader(f, delimiter="|")
    for row in csv_reader:
        print(row)

    for row in csv_reader:
        print(row["user_gender"])