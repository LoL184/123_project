import time


# task 1

def log_call(func):
    def wr(*args, **kwargs):
        print(f"CALL {func.__name__}({args}, {kwargs})")
        result = func(*args, **kwargs)
        return result
    return wr


@log_call
def clip(text: str, max_len: int, suffix: str = "...") -> str:
    return suffix[:max_len] if max_len < len(suffix) else\
        text[:max_len-1]+suffix if max_len < len(text) else text


# task 2

def timeit_ms(func):
    def wr(*args, **kwargs):
        time_start = time.perf_counter()
        func(*args, **kwargs)
        print(f"{func.__name__}: {time.perf_counter() - time_start} ms")
    return wr


@timeit_ms
def dot(x: list[float], y: list[float]):
    return 'ValueError' if len(x) != len(y) else\
        sum([x[i]*y[i] for i in range(len(x))])


# task 3

def once(func):
    def wr(*args, **kwargs):
        def first_iter(answer=None):
            if answer is None:
                answer = func(*args, **kwargs)
            return answer
        return first_iter()
    return wr


@once
def slice_str(s: str, start: int = 0, end: int = None, step: int = 1) -> str:
    return 'ValueError' if step == 0 else s[start:end:step]


print(slice_str('222222', 0, 5))
print(slice_str('111111', 0, 2))


