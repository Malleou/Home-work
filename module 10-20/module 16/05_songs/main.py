#  здесь код

def add_song(song_list: list, sum_song: int) -> (int, list):
    """Из одного списка переносит значения в другой и суммирует их"""

    new_list = []
    long_list = 0.0
    for counter in range(sum_song):
        name_song = input(f'Название {counter + 1}-й песни: ')
        for song in song_list:
            if song[0].lower() == name_song.lower():
                new_list.append(song)
                long_list += song[1]
                break
        else:
            print('Такой песни нет в вашем списке')
    return new_list, long_list



violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]
num_songs = int(input('Сколько песен выбрать? '))
new_song_list, tyme = add_song(violator_songs,num_songs)
print('Общее время звучания песен:', round(tyme, 2), 'мин.')