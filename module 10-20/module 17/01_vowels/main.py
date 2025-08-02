#  здесь код
def vowel_count(text_: str) -> list:
    """Находит гласные буквы в строке

    check_ - гласные буквы."""

    check_ = 'аоэеиыуёюя'
    vowels = [vowel for vowel in text_ if vowel in check_]
    return vowels

txt = input('Введите текс: ')
vc = vowel_count(txt)
print('Список гласных букв:', vc)
print('Длина списка:', len(vc))