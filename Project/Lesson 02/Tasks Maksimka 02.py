import math


# task 1

def moving_avg(a: list, k: int):
    if k <= len(a):
        mid_list = []
        for i in range(len(a)-k+1):
            mid_list.append(sum(a[i: i+k])/k)
        return mid_list
    else:
        return "You're dummy"


# task 2

def run_length_encoding(inp_data):
    out_list = []
    for elem in set(inp_data):
        out_list.append((elem, inp_data.count(elem)))
    return out_list


# task 3

def operations(in1, in2):
    in1, in2 = set(in1.split()), set(in2.split())
    return sorted(list(in1 & in2)), sorted(list(in1 - in2)), sorted(list(in1 ^ in2))


# task 4

def extr_del(a : list[int]):
    if a.count(min(a)) == len(a):
        a = []
    else:
        a.remove(max(a)); a.remove(min(a))
    return a


# task 5

def k_len_elem(k: int, a: list[int]):
    if k <= len(a):
        ans_set = set()
        for i in range(len(a) - k + 1):
            ans_set.add(tuple(a[i:i+k]))
        return len(ans_set)
    else:
        return "You're dummy"


# task 6

def top_k(items: list, k: int):
    items_wr = list(set(items)) # items without repeat
    if k < len(items_wr):
        count_list = []
        ans_list = []
        for elem in items_wr:
            count_list.append(items.count(elem))
        for i in range(k):
            ind = count_list.index(max(count_list))
            ans_list.append(items_wr[ind])
            count_list.pop(ind)
            items_wr.pop(ind)
        return ans_list
    elif k == len(items_wr):
        return items_wr
    else:
        return "You're dummy"


# task 7

def permetuation_possibility(a: list):
    a_wr = list(set(a))
    for elem in a_wr:
        if a.count(elem) > math.ceil(len(a)/2):
            return False
    return True


# task 8

def rotate_90(mat: list[list]):
    ans_mat = [[] for i in range(len(mat))]
    for i in range(1, len(mat)+1):
        for j in range(len(mat[i*-1])):
            ans_mat[j].append(mat[i*-1][j])
    return ans_mat

    # return tuple(zip(*mat[::-1]))   # stackoverflow variant


if __name__ == '__main__':

    # task 1
    assert (moving_avg([1, 0, 3, 1, 2], 2)) == [0.5, 1.5, 2.0, 1.5]

    # task 2
    a = run_length_encoding('aaabb')
    assert ('a', 3) in a and ('b', 2) in a

    # task 3
    assert operations("a b c", "b d") == (['b'], ['a', 'c'], ['a', 'c', 'd'])

    # task 4
    assert extr_del([5, 1, 3, 5, 2, 1]) == [3, 5, 2, 1]
    assert extr_del([1, 1, 1, 1]) == []

    # task 5
    assert k_len_elem(3, [1, 2, 1, 3, 5]) == 3
    assert k_len_elem(3, [1, 2, 1, 1, 2, 1]) == 3

    # task 6
    assert top_k(['a', 'b', 'a', 'c', 'b', 'a'], 2) == ['a', 'b']

    # task 7
    assert permetuation_possibility([1, 1, 2, 2, 3]) == True
    assert permetuation_possibility([1, 1, 1, 2]) == False

    # task 8
    assert rotate_90([[1, 2], [3, 4]]) == [[3, 1], [4, 2]]
    assert rotate_90([[3, 1, 5], [7, 0, 9], [2, 8, 6]]) == [[2, 7, 3], [8, 0, 1], [6, 9, 5]]

