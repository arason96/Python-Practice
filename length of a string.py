def len_of_str(str):
    length = 0
    for i in str:
        length += 1
    print("Length of the string is : ", length)


x = input("Enter the string : ")
len_of_str(x)