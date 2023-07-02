import random


class MyRandomSequence:
    def __iter__(self):
        self._state = 0
        return self

    def __next__(self):
        if self._state >= random.randint(1, 500):
            raise StopIteration
        self._state += 1
        return self._state


print(list(MyRandomSequence()))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
print(list(MyRandomSequence()))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]
