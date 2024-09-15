def request(number):
    dividers=[]
    for i in range(3, number+1):
        if number % i == 0:
            dividers.append(i)
    count=1
    tmp=""
    for i in range(1, number + 1):
        tmp = str(tmp) + brute_forcer(number, dividers, count)
        count +=1
    return tmp

def brute_forcer(number, dividers, count):
    tmp = ""
    for i in dividers:
        if i - count > 0 and i - count > count:
            tmp=str(tmp) + " " + str(count) + " " + str((i - count)) + " | "
    return str(tmp)



if __name__ == '__main__':
    try:
        print(request(int(input("Введите число:   "))))
    except:
        print("Для особо одарённых: число - это не буква\nИ не пытайся ломать то, что работает\nРаботает - "
              "не лезь!))))")
