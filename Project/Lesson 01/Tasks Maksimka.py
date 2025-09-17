# assert

# task 1

def using_for(a=int):
    return sum(i for i in range(a if a % 2 == 0 else a + 1) if i % 2 == 1)


def not_using_for(a=int):
    return int((((a if a % 2 == 1 else a - 1) + 1) / 2) ** 2)


assert using_for(6) == 9 and not_using_for(6) == 9 and using_for(6) == not_using_for(6)


# task 2

def using_сomprehension(a=list):
    return [i for i in a if i ** 2 < 100]


def not_using_comprehension(a=list):
    b = []
    for i in a:
        if i ** 2 < 100:
            b.append(i)
    return b


assert using_сomprehension([10, 2, 5, 6, 11]) == [2, 5, 6] \
    and not_using_comprehension([10, 2, 5, 6, 11]) == [2, 5, 6] \
    and using_сomprehension([10, 2, 5, 6, 11]) == not_using_comprehension([10, 2, 5, 6, 11])


# task 3

def check_password(s=str):
    return "OK" if len(s) >= 8 and [i for i in range(1, 10) if str(i) in s] else "Weak"


assert check_password("sfka@35s") == "OK"


# task 4

def delete_repeats(a=list):
    n = 1
    while True:
        if n >= len(a) - 1:
            break

        if a[n-1] == a[n]:
            a.pop(n)
        else:
            n += 1
    return a


assert delete_repeats([1, 1, 1, 3, 2, 2, 2, 1]) == [1, 3, 2, 1]

