print('Очки игроков')


# Условие задачи:
# scores - список очков
# Очки второго игрока += длина списка
# Добавляется новый игрок
# Очки третьего игрока += длина списка
# Выходные данные:
# scores
#

def length(player_list):  # 2) функции счетчик количества игроков - (№ 1 - 5 аргументов) ; - (№ 2 - 6 аргументов)
    players_count = 0  # 3) переменная счетчик
    for _ in player_list:  # 4) цикл for считает
        players_count += 1
    return players_count  # 5) передача данных на стр.21


# 1) список игроков - вызов функции // def length(player_list): // стр.13
scores = [8, 5, 10, 7, 6]
# 6) [8, 5, 10, 7, 6] += [8, 5 + scores , 10, 7, 6]
scores[1] += length(scores)
# 7) [8, 10 , 10, 7, 6]
scores.append(0)
# 8) [8, 10 , 10, 7 +  scores, 6, 0]
scores[3] += length(scores)
# 9) [8, 10 , 10, 13, 6, 0]
print(scores)
