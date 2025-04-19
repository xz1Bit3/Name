calls = 0


def count_calls ():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()

def is_contains(string, list_to_search):
    count_calls()
    for i in list_to_search:
        print(string.lower(), i.lower(), string.lower() == i)
    if string.lower() == i.lower():
        if string == i:
            return True #завершение функции
        return False

result = string_info('example')
result1 = string_info('test')
#print(result)
#print(result1)
#print(calls)
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)





