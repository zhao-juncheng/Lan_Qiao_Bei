import time

time_start=time.time()

y = [i for i in range(2, 50)]  # 2022040920220409
result = [1, 2, 1, 4, 5, 4, 1, 2, 9, 0, 5, 10,
          11, 14, 9, 0, 11, 18, 9, 11, 11, 15, 17, 9,
          23, 20, 25, 16, 29, 27, 25, 11, 17, 4, 29, 22,
          37, 23, 9, 1, 11, 11, 33, 29, 15, 5, 41, 46]


def lanqiao(y, result):

    def f(x):
        for a, b in zip(y, result):
            if x % a != b:
                return False
        return True

    for x in range(2022040000000000, 10 ** 17):
        if x%100000000==0:
            print(x)
        if f(x):
            return x


print(lanqiao(y, result))


time_end=time.time()
print(time_end-time_start)