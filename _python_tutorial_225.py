# _python_tutorial_225

from csv import writer

with open("file1.txt", "w", newline="") as f:
    csv_writer = writer(f)
    # 2 method 1 writerow 2 writerows   
    # csv_writer.writerow(["name", "country"])
    # csv_writer.writerow(["shing yao", "japan"])
    # csv_writer.writerow(["john", "UK"])
    # csv_writer.writerow(["habibi", "UAE"])

    csv_writer.writerows([["name", "country"], ["shing yao", "japan"], ["john", "UK"], ["habibi", "UAE"]])