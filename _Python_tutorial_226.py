# _Python_tutorial_226

from csv import DictWriter
with open("final.csv", "w", newline="") as f:
    csv_writer = DictWriter(f, fieldnames=['first_name', 'last_name', 'age'])
    csv_writer.writeheader()
    # writerow, writerows

    csv_writer.writerow({"first_name": "arif","last_name": "sanaullah","age": 2})
    csv_writer.writerow({"first_name": "abid" ,"last_name": "mukhtar" ,"age": 2})
    csv_writer.writerow({"first_name": "arifa" ,"last_name": "sana" ,"age": 2})
    csv_writer.writerow({"first_name": "ahsan", "last_name": "zainab","age": 52})
    csv_writer.writerows([
        {"first_name": "ahsan", "last_name": "zainab", "age": 21},
        {"first_name": "hassan", "last_name": "zain", "age": 22},
        {"first_name": "arifa", "last_name": "sana", "age": 2}
    ])