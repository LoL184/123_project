# task 1

def freq_count(in_str: str):
    return tuple(sorted([{i: in_str.count(i) for i in in_str}.get(j) for j in set(list(in_str))]))


# task 2

def dict_wr(key, names, classes={}):
    if key in classes:
        classes[key].append(names)
    else:
        classes.setdefault(key, names)
    return classes


# task 3

def city_population(city_dict: dict):
    return dict([(k, [j for j in city_dict if city_dict[j] == k]) for k in city_dict.values()])


# task 4

def price_amount_dict(price_dict: dict, amount_dict: dict):
    return dict([(k, (price_dict[k], amount_dict[k])) for k in price_dict if k in amount_dict])



if __name__ == '__main__':

    # task 1
    assert freq_count('aaabbbbcccc') == (3, 4, 4)

    # task 2
    assert dict_wr('7б', ['Ваня', 'Коля']) == {'7б': ['Ваня', 'Коля']}

    # task 3
    assert city_population({'A': 1, 'B': 1, 'C': 2}) == {1: ['A', 'B'], 2: ['C']}

    # task 4
    assert price_amount_dict({'A': 1, 'B': 32}, {'A': 4, 'B': 1, 'C': 3}) == {'A': (1, 4), 'B': (32, 1)}
