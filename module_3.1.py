calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    tuple_new = (len(string), string.upper(), string.lower())
    return tuple_new


def is_contains(string, list_to_search):
    count_calls()
    for item in list_to_search:
        list_new = []
        list_new.append(item.lower())
    if string.lower() in list_new:
        return True
    else:
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)