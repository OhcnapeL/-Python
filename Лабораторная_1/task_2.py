list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды

middle_point = len(list_players) // 2
first_team = list_players[:middle_point]
seconde_team = list_players[middle_point:]

print(first_team)
print(seconde_team)
