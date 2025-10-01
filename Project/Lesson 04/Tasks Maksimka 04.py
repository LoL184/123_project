# task 1

def clip(text: str, max_len: int, suffix: str = "...") -> str:
    return suffix[:max_len] if max_len < len(suffix) else text[:max_len-1]+suffix if max_len < len(text) else text


# task 2

def dot(x: list[float], y: list[float]):
    return 'ValueError' if len(x) != len(y) else sum([x[i]*y[i] for i in range(len(x))])


# task 3

def slice_str(s: str, start: int = 0, end: int = None, step: int = 1) -> str:
    return 'ValueError' if step == 0 else s[start:end:step]


# task 4

def append_safe(x: int, buf: list[int] | None = None) -> list[int]:
    return [x] if buf is None else buf.append(x)


# task 5

def safe_div(a: float, b: float) -> float | None:
    return None if b == 0 else a/b


if __name__ == '__name__':

    # task 1
    assert [clip("hello", 5), clip("hello!", 5)] == ['hello', 'hell...']

    # task 2
    assert dot([1, 2, 3], [4, 5, 6]) == 32

    # task 3
    assert slice_str('abcdef', 1, 5) == 'bcde'

    # task 4
    assert append_safe(3) == [3]

    # task 5
    assert [safe_div(1, 2), safe_div(9, 0)] == [0.5, None]
