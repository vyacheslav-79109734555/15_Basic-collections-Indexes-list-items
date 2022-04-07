worker_ID = [10, 20, 30, 40]  # список ID рабочих
x = 0

for _ in worker_ID:
    x += 1
print('Кол-во сотрудников в офисе: ', x)

for i in worker_ID:
    print('ID сотрудника: ', i)


search_ID = int(input('Какой ID ищем? '))
while True:
    for i in worker_ID:
        if i == search_ID:
            print('«Сотрудник на месте»')
        else:
            print('«Сотрудник не работает!»')
        search_ID = int(input('Какой ID ищем? '))





