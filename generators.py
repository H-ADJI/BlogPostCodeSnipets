import random


def random_sequence_generator():
    start = 1
    while True:
        if start >= random.randint(1, 500):
            break
        yield start
        start += 1


for element in random_sequence_generator():
    print(element,end=" ")
print()
# 1 2 3 4 5 6 7 8 9 10 11 12 13 