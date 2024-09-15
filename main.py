
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    numbers = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
    count = 0
    while True:
        if numbers[count] > 0:
            print(numbers[count])
        elif numbers[count] == 0:
            pass
        else:
            break
        count += 1
    del count
    del numbers
