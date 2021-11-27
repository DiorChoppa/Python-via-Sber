import sys
import time

sys.setrecursionlimit(10000)

def time_decorator(ft):
    def _inner(*args, **kwargs):
        start = time.time()
        result = ft(*args, **kwargs)
        print("work time: ", time.time() - start)
        return result
    return _inner

def naive_factorial(n):
    if n == 1:
        return 1
    else:
        return n * naive_factorial(n - 1)

memo_dict = {0:1}

def memo_factorial(n):
    if n in memo_dict.keys():
        return memo_dict[n]
    else:
        val = n * memo_factorial(n - 1)
        memo_dict[n] = val
        return val

@time_decorator
def test(ft, nb_runs):
    print(ft)
    for i in range(nb_runs):
        ft(nb_runs)

@time_decorator
def main(n, choice_algorithm = "memo"):
    if choice_algorithm == "memo":
        print("run memo")
        result = memo_factorial(n)
    else:
        print("run naive")
        result = naive_factorial(n)
    print("factorial = ", result)

def main_for_test():
    for f in [naive_factorial, memo_factorial]:
        test(f, 1000)

if __name__ == '__main__':
    #main(int(sys.argv[1]), sys.argv[2])
    main_for_test()