
# task 1

def moving_avg(a: list, k: int):
    if k <= len(a):
        mid_list = []
        for i in range(len(a)-k+1):
            mid_list.append(sum(a[i: i+k])/k)
        return mid_list
    else:
        return "You're dummy"


def run_length_encoding(inp_data):
    out_list = []
    for elem in set(inp_data):
        out_list.append((elem, inp_data.count(elem)))
    return out_list


def operations(in1, in2):
    in1, in2 = set(in1.split()), set(in2.split())
    return list(in1 & in2), list(in1 - in2), list(in1 ^ in2)






if __name__ == '__main__':

    # task 1
    assert (moving_avg([1, 0, 3, 1, 2], 2)) == [0.5, 1.5, 2.0, 1.5]

    # task 2
    a = run_length_encoding('aaabb')
    assert ('a', 3) in a and ('b', 2) in a

    # task 3
    assert operations("a b c", "b d") == (['b'], ['a', 'c'], ['a', 'd', 'c'])
