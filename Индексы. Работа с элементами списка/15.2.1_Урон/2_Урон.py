# Задача Урон
# условие задачи:
# Список из N значений урона
# Если урон < 100 И это не маг, то урон += урон Мага
# Выходные данные
# Итоговый урон монстров

monsters_count = int(input('Кол-во монстров: '))
mage_index = int(input('Номер мага в списке: '))
monsters_damage = []  # список
while True:
    if monsters_count >= mage_index:
        print('ok')
        break
    else:
        print('Ошибка ввода')
        mage_index = int(input('Номер мага в списке: '))

# с помощью цикла создали список // monsters_damage //
for monster in range(monsters_count):
    print('Урон у', monster + 1, 'монстра:', end=' ')
    damage = int(input())
    # добавили в список // monsters_damage // при помощи ~.append(damage) данные пользователя
    monsters_damage.append(damage)

    # в данном цикле // i_monster // выступает в роле индекса списка который мы создали // monsters_damage //
for i_monster in range(monsters_count):
    if monsters_damage[i_monster] < 100 and i_monster != mage_index - 1:
        monsters_damage[i_monster] += monsters_damage[mage_index - 1]

print('Итоговый урон монстров: ', monsters_damage)
