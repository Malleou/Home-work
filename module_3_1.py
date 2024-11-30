def count_calls():
    global calls
    calls += 1
    return calls


def string_info(string):
    str_ = (len(string), string.upper(), string.lower())
    count_calls()
    return str_



def is_contains(string, list_to_search):
    string = string.lower()
    boolean = False

    for text in list_to_search:
        text = text.lower()
        if string == text:
            boolean = True
    count_calls()
    return boolean



calls = 0
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)