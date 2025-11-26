def lns(words: list) -> dict:
    ans = dict.fromkeys([len(i) for i in words], '')
    for k in ans:
        ans[k] = [i for i in words if len(i) == k]
    return ans

print(lns(['hi', 'map', 'to', 'a', 'see']))

