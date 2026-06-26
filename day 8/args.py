# args:
# add the data sent to the functions


def addition(*abc):
    total = 0
    for i in abc:
        total += i
    print(total)


addition(1, 2, 3, 4)
