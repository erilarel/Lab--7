"""Программа выдает общедоступные данные со странички игрока, если его профиль открыт для всех """

import requests
import json

arr_interfaces = ["IPlayerService", "ISteamUser", "ISteamUserStats"]

def get_info(steamid):
    key = '6C247910445AC2833FCD3A0125794AAC'
    appid = 730 #идентификатор приложения, в котором ищутся достижения (конкретное приложение)
    print(f"Информация об участнике со steamid = {steamid}\n")
    for i in arr_interfaces:
        if i == "IPlayerService":
            url4 = f"https://api.steampowered.com/IPlayerService/GetSteamLevel/v1/?key={key}&steamid={steamid}"
            data4 = requests.get(url4).json()
            level_of_player = data4['response']['player_level']

            url2 = f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={key}&steamid={steamid}"
            data2 = requests.get(url2).json()
            count_of_games = data2['response']['game_count']

            url3 = f"https://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/?key={key}&steamid={steamid}"
            data3 = requests.get(url3).json()
            arr_of_recently_games = data3['response']['games']
            names = []
            for x in range(len(arr_of_recently_games)):
                names.append(arr_of_recently_games[x]['name'])

        if i == "ISteamUser":
            url = f"http://api.steampowered.com/ISteamUser/GetFriendList/v1?key={key}&steamid={steamid}&relationship=friend"
            data = requests.get(url).json()
            count_of_friends = len(data['friendslist']['friends'])

        if i == "ISteamUserStats":
            url1 = f"https://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v1?key={key}&steamid={steamid}&appid={appid}"
            data1 = requests.get(url1).json()
            achieved_value = data1['playerstats']['achievements']
            count_of_achievements = achieved_value[0]["achieved"]

    print(f"Уровень участника: {level_of_player}")
    print(f"За всё время участник сыграл в {count_of_games} различные игры")
    print(f"Последние игры, которые посещал участник: {', '.join(names)}")
    print("Количество друзей у данного участника: ", count_of_friends)
    print(f"Количество достижений у данного участника в игре с кодом {appid}: {count_of_achievements}")

get_info(76561198036370701)