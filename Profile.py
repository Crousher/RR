import csv
# константы, переменные и др. вещи которые будут нужны ниже
name = input()
lvl, S, P, I, id = 1,1,1,1,0
filename = 'PlrsInfo.csv'
# создаём идентификатор
# вычисляем кол-во пользователей и +1 к числу
# для этого читаем нашу таблицу и считаем строки
with open(filename) as file:  # ломается чтение и послед запись если не выполнять всё поболчно
    reader = csv.reader(file)   # т.е. работаем только с простым чтением и пишем всё связанное с ним
    for i in reader:
        id += 1
    Dictreader = csv.DictReader(file)  # а после переходим к др. нужным нам типам чтения
    # (здесь читаем как словарь)(ключи здесь первая строка документа)
    for i in Dictreader:
        print(i)
user ={id : {'id' : id,'name': name, 'lvl': lvl, 'S': S, 'P': P, 'I': I}}
# нижулежащая часть заполняет инвормацию о новом игроке в таблицу
with open(filename, 'a', newline='') as file:
    fieldnames =['id','name', 'lvl', 'S', 'P', 'I']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writerow(user[id])
# Блок считывания и сохранения инф в отд. файле завершён

