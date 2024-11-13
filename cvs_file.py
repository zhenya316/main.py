# посмотреть вебинар по 7 модулю, как в эксель файл записывать
import csv

with open('testcsv123.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';', fieldnames=['name', 'age', 'salary'])
    salaries = 0
    for row in reader:
        if row['salary'] == 'salary':
            continue
        salaries += int(row['salary'])
    print(salaries)
# посчитали столбик salary

person = [{'name': 'John', 'age': '13'}, {'name': 'Bob', 'age': '18'}]

with open('testcsv1234.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=['name', 'age'])
    writer.writeheader()
    writer.writerows(person)
# Записали в новый файл словарь