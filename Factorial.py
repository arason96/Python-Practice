def fact(num):
    n = 1
    if num == 1 or num == 0:
        return 1
    else:
        for i in range(num, 1, -1):
            n = n * i
        return n


if __name__ == '__main__':

    x = 0
    flag = False
    while True:
        try:
            x = int(input("input  : "))
        except ValueError:
            print("Not an integer!")
            continue
        else:
            if x < 1:
                print("Enter a positive integer")
                flag = True
                continue
            break
    if flag:
        x = fact(x)
        print(x)
    else:
        print(fact(x))