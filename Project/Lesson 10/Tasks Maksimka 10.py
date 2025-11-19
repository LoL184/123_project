# task 1

def lucky_ticket(ticket: tuple[int] | str):
    if len(ticket) != 6:
        raise ValueError('Wrong ticket code')
    return sum([int(i) for i in ticket[:3:]]) == sum([int(i) for i in ticket[3::]])


# print(lucky_ticket('304070')

# task 2

def letters_sort(words: list[str]):
    letters = sorted(set([w[0].lower() for w in words]))
    w_srt = [[w for w in words if w.lower()[0] == l] for l in letters]
    return dict(zip(letters, w_srt))


# print(letters_sort(["Apple", 'art', 'Bee']))
