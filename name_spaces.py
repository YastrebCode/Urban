def count_calls():
    global calls
    calls +=1

def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())

def is_contains(string, list_to_search):
    count_calls()
    string = list(string_info(string))[2]
    for i in list_to_search:
        if string == i.lower():
            return True
    return False






if __name__ == '__main__':
    calls = 0
    print(string_info('Capybara'))
    print(string_info('Armageddon'))
    print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
    print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
    print(calls)