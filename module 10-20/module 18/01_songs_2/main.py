violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

# здесь код

def music_timer(music_dict: dict) -> float:
    """Подсчёт времени"""

    total_time = 0
    sum_song = int(input('Введите количество песен? '))
    for i in range(sum_song):
        song_name = input('Введите название песни: ')
        if song_name in music_dict:
            total_time += music_dict[song_name]
        else:
            print('Такой музыки не нашли :(')
    return total_time

play_time = music_timer(violator_songs)
print('Общее время звучания песен:', round(play_time, 2))
